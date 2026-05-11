import networkx as nx
from typing import List, Dict, Any
from .retriever import RetrievedDoc
from .policy import PolicyDecision

def build_evidence_graph(query: str, answer: str, retrieved: List[RetrievedDoc], policy: PolicyDecision, conflict_report: Dict[str, Any]) -> Dict[str, Any]:
    g = nx.DiGraph()
    g.add_node("query", type="query", text=query)
    g.add_node("answer", type="answer", text=answer)
    g.add_edge("query", "answer", relation="produced")

    for d in retrieved:
        doc_node = f"doc:{d.doc_id}"
        g.add_node(
            doc_node,
            type="document",
            title=d.title,
            topic=d.topic,
            authority_score=d.authority_score,
            freshness_score=d.freshness_score,
            evidence_score=d.evidence_score,
            access_level=d.access_level,
            sensitivity=d.sensitivity,
            status=d.status,
            effective_date=d.effective_date,
            owner=d.owner,
        )
        g.add_edge("query", doc_node, relation="retrieved")
        g.add_edge(doc_node, "answer", relation="supports_or_contextualises")

    g.add_node("policy", type="policy_decision", decision=policy.decision, risk_score=policy.risk_score, reasons=policy.reasons)
    g.add_edge("policy", "answer", relation="governs")

    if conflict_report.get("conflict_detected"):
        g.add_node("conflict", type="conflict_report", conflicts=conflict_report["conflicts"])
        g.add_edge("conflict", "answer", relation="qualifies")

    return nx.node_link_data(g)
