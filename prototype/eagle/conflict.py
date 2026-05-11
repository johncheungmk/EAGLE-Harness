from typing import List, Dict, Any
from collections import defaultdict
from .retriever import RetrievedDoc

def detect_conflicts(retrieved: List[RetrievedDoc]) -> Dict[str, Any]:
    by_topic = defaultdict(list)
    for d in retrieved:
        by_topic[d.topic].append(d)

    conflicts = []
    for topic, docs in by_topic.items():
        statuses = {d.status for d in docs}
        dates = {d.effective_date for d in docs}
        if "deprecated" in statuses and "current" in statuses:
            current_docs = [d for d in docs if d.status == "current"]
            deprecated_docs = [d for d in docs if d.status == "deprecated"]
            preferred = sorted(current_docs, key=lambda d: (d.authority_score, d.freshness_score), reverse=True)[0]
            conflicts.append({
                "topic": topic,
                "type": "current_vs_deprecated",
                "preferred_doc_id": preferred.doc_id,
                "conflicting_doc_ids": [d.doc_id for d in deprecated_docs],
                "message": f"Current and deprecated sources were retrieved for topic '{topic}'."
            })
        elif len(dates) > 1 and len(docs) > 1:
            preferred = sorted(docs, key=lambda d: (d.authority_score, d.freshness_score), reverse=True)[0]
            conflicts.append({
                "topic": topic,
                "type": "version_difference",
                "preferred_doc_id": preferred.doc_id,
                "conflicting_doc_ids": [d.doc_id for d in docs if d.doc_id != preferred.doc_id],
                "message": f"Multiple versions/effective dates were retrieved for topic '{topic}'."
            })

    return {"conflict_detected": bool(conflicts), "conflicts": conflicts}
