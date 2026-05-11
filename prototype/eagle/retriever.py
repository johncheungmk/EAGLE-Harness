from dataclasses import dataclass
from typing import List
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@dataclass
class RetrievedDoc:
    doc_id: str
    title: str
    topic: str
    text: str
    retrieval_score: float
    authority_score: float
    freshness_score: float
    evidence_score: float
    access_level: str
    sensitivity: str
    status: str
    effective_date: str
    owner: str

class EvidenceRetriever:
    def __init__(self, documents: pd.DataFrame):
        self.documents = documents.reset_index(drop=True)
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(self.documents["text"].fillna(""))

    def retrieve(self, query: str, role: str, top_k: int = 5) -> List[RetrievedDoc]:
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.matrix).ravel()
        rows = []

        for idx, sim in enumerate(sims):
            row = self.documents.iloc[idx].to_dict()
            evidence_score = (
                0.5 * float(sim)
                + 0.3 * float(row["authority_score"])
                + 0.2 * float(row["freshness_score"])
            )
            rows.append(RetrievedDoc(
                doc_id=row["doc_id"],
                title=row["title"],
                topic=row["topic"],
                text=row["text"],
                retrieval_score=float(sim),
                authority_score=float(row["authority_score"]),
                freshness_score=float(row["freshness_score"]),
                evidence_score=float(evidence_score),
                access_level=row["access_level"],
                sensitivity=row["sensitivity"],
                status=row["status"],
                effective_date=row["effective_date"],
                owner=row["owner"],
            ))

        rows.sort(key=lambda x: x.evidence_score, reverse=True)
        return rows[:top_k]
