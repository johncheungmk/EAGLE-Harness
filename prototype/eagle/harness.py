import json
from pathlib import Path
from dataclasses import asdict
from typing import Dict, Any

from .config import EagleConfig
from .data_loader import load_documents, user_can_access
from .retriever import EvidenceRetriever
from .conflict import detect_conflicts
from .policy import decide_policy
from .generator import generate_answer
from .evidence_graph import build_evidence_graph

class EagleHarness:
    def __init__(self, config: EagleConfig | None = None):
        self.config = config or EagleConfig()
        self.documents = load_documents(self.config.documents_path)
        self.retriever = EvidenceRetriever(self.documents)
        Path(self.config.logs_path).parent.mkdir(parents=True, exist_ok=True)

    def answer(self, query: str, role: str = "student", mode: str = "eagle") -> Dict[str, Any]:
        retrieved = self.retriever.retrieve(query, role=role, top_k=self.config.top_k)

        if mode == "standard_rag":
            conflict_report = {"conflict_detected": False, "conflicts": []}
            policy = decide_policy(query, role, [], conflict_detected=False)
            policy.decision = "allow"
            policy.risk_score = 0
            policy.reasons = ["Standard RAG baseline does not enforce EAGLE governance."]
        elif mode == "agentic_rag":
            conflict_report = detect_conflicts(retrieved)
            policy = decide_policy(query, role, [], conflict_detected=conflict_report["conflict_detected"])
            policy.reasons.append("Agentic RAG baseline has partial risk awareness but does not enforce evidence-level access filtering.")
        else:
            conflict_report = detect_conflicts(retrieved)
            policy = decide_policy(query, role, retrieved, conflict_detected=conflict_report["conflict_detected"])
            retrieved = [d for d in retrieved if user_can_access(role, d.access_level)]

        answer = generate_answer(
            query=query,
            role=role,
            retrieved=retrieved,
            policy=policy,
            conflict_report=conflict_report,
            api_key=self.config.openai_api_key,
            model=self.config.openai_model,
        )

        graph = build_evidence_graph(query, answer, retrieved, policy, conflict_report)

        result = {
            "query": query,
            "role": role,
            "mode": mode,
            "answer": answer,
            "retrieved": [asdict(d) for d in retrieved],
            "policy": asdict(policy),
            "conflict_report": conflict_report,
            "evidence_graph": graph,
        }
        self._log(result)
        return result

    def _log(self, result: Dict[str, Any]) -> None:
        with open(self.config.logs_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(result, ensure_ascii=False) + "\\n")
