import pandas as pd
from eagle.harness import EagleHarness

def simple_metric(result: dict) -> dict:
    answer = result["answer"].lower()
    retrieved = result["retrieved"]
    policy = result["policy"]
    conflict_report = result["conflict_report"]

    return {
        "has_citation": int("[" in answer and "]" in answer),
        "num_sources": len(retrieved),
        "risk_score": policy["risk_score"],
        "decision": policy["decision"],
        "conflict_detected": int(conflict_report["conflict_detected"]),
        "blocked": int(policy["decision"] == "block"),
        "human_approval_required": int(policy["decision"] == "human_approval_required"),
    }

def main():
    harness = EagleHarness()
    questions = pd.read_csv(harness.config.questions_path)

    rows = []
    for _, q in questions.iterrows():
        for mode in ["standard_rag", "agentic_rag", "eagle"]:
            result = harness.answer(query=q["question"], role=q["role"], mode=mode)
            metrics = simple_metric(result)
            rows.append({
                "question": q["question"],
                "role": q["role"],
                "expected_category": q["expected_category"],
                "mode": mode,
                "answer": result["answer"],
                **metrics,
            })

    df = pd.DataFrame(rows)
    df.to_csv("outputs/evaluation_summary.csv", index=False)
    print(df.groupby("mode")[["has_citation", "num_sources", "risk_score", "conflict_detected", "blocked", "human_approval_required"]].mean())
    print("\\nSaved outputs/evaluation_summary.csv")

if __name__ == "__main__":
    main()
