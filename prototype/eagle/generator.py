from typing import List, Optional
from .retriever import RetrievedDoc
from .policy import PolicyDecision

def _format_sources(retrieved: List[RetrievedDoc]) -> str:
    lines = []
    for i, d in enumerate(retrieved, start=1):
        lines.append(
            f"[{i}] {d.title} ({d.doc_id}, {d.status}, effective {d.effective_date}, "
            f"authority={d.authority_score:.2f}, freshness={d.freshness_score:.2f}): {d.text}"
        )
    return "\n".join(lines)

def generate_answer(query: str, role: str, retrieved: List[RetrievedDoc], policy: PolicyDecision, conflict_report: dict, api_key: Optional[str] = None, model: str = "gpt-4o-mini") -> str:
    if policy.decision == "block":
        return (
            "I cannot provide this information or perform this action because the policy engine classified the request "
            "as too risky or outside the user's access permission. Reasons: "
            + "; ".join(policy.reasons)
        )

    if api_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            prompt = f"""
You are an institutional AI assistant operating inside the EAGLE Harness.

User role: {role}
User question: {query}

Policy decision: {policy.decision}
Risk score: {policy.risk_score}
Policy reasons: {policy.reasons}

Conflict report:
{conflict_report}

Evidence sources:
{_format_sources(retrieved)}

Instructions:
- Answer only using accessible and authoritative evidence.
- Cite sources using [1], [2], etc.
- If there is a conflict, prefer current approved policy and explain the conflict.
- If policy requires confirmation or human approval, do not perform the action. Explain what approval is needed.
- Do not reveal restricted information to unauthorised roles.
"""
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You produce concise, evidence-grounded institutional answers."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
            )
            return resp.choices[0].message.content
        except Exception as e:
            return fallback_answer(query, retrieved, policy, conflict_report, error=str(e))

    return fallback_answer(query, retrieved, policy, conflict_report)

def fallback_answer(query: str, retrieved: List[RetrievedDoc], policy: PolicyDecision, conflict_report: dict, error: str | None = None) -> str:
    parts = []
    if error:
        parts.append(f"LLM API fallback used because: {error}")

    if policy.decision == "human_approval_required":
        parts.append("This request requires human approval before action is taken.")
    elif policy.decision == "confirmation_required":
        parts.append("This request may proceed only after user confirmation or appropriate review.")

    if conflict_report.get("conflict_detected"):
        parts.append("A potential source conflict was detected. Current, higher-authority sources should be preferred.")

    if retrieved:
        best = retrieved[0]
        parts.append(f"Based on the strongest evidence, {best.text} [1]")
    else:
        parts.append("No relevant evidence was found.")

    parts.append("\\nSources:")
    for i, d in enumerate(retrieved, start=1):
        parts.append(f"[{i}] {d.title} ({d.doc_id}, {d.status}, effective {d.effective_date})")

    return "\\n".join(parts)
