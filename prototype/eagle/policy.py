from dataclasses import dataclass
from typing import List

from .data_loader import user_can_access
from .retriever import RetrievedDoc

ACTION_KEYWORDS = [
    "send", "email", "announce", "change", "update", "delete", "approve",
    "modify", "postpone", "publish", "create", "access"
]

RESTRICTED_KEYWORDS = [
    "salary", "named staff", "compensation", "personal data", "student record",
    "grade change", "disciplinary", "confidential"
]

@dataclass
class PolicyDecision:
    decision: str
    risk_score: int
    reasons: List[str]

def classify_query(query: str) -> dict:
    q = query.lower()
    return {
        "is_action": any(k in q for k in ACTION_KEYWORDS),
        "is_restricted": any(k in q for k in RESTRICTED_KEYWORDS),
    }

def decide_policy(query: str, role: str, retrieved: List[RetrievedDoc], conflict_detected: bool) -> PolicyDecision:
    info = classify_query(query)
    risk_score = 0
    reasons = []

    if info["is_action"]:
        risk_score += 3
        reasons.append("The request appears to involve an action, not only information retrieval.")

    if info["is_restricted"]:
        risk_score += 4
        reasons.append("The request may involve restricted or sensitive information.")

    inaccessible = [d for d in retrieved if not user_can_access(role, d.access_level)]
    if inaccessible:
        risk_score += 4
        reasons.append("Some relevant sources are above the user's access level.")

    if any(d.sensitivity == "restricted" for d in retrieved):
        risk_score += 2
        reasons.append("Retrieved evidence includes restricted material.")

    if conflict_detected:
        risk_score += 2
        reasons.append("Potential conflict or outdated source detected.")

    if role in {"hr", "admin_manager"} and info["is_restricted"]:
        risk_score = max(risk_score - 3, 0)
        reasons.append("User role has elevated permission for restricted institutional information.")

    if risk_score >= 9:
        decision = "block"
    elif risk_score >= 6:
        decision = "human_approval_required"
    elif risk_score >= 3:
        decision = "confirmation_required"
    else:
        decision = "allow"

    return PolicyDecision(decision=decision, risk_score=risk_score, reasons=reasons)
