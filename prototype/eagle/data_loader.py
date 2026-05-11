import pandas as pd
from datetime import datetime

AUTHORITY_SCORE = {
    "approved_policy": 1.00,
    "official_guide": 0.90,
    "faq": 0.75,
    "old_policy": 0.30,
    "draft": 0.25,
}

ACCESS_RANK = {
    "public": 0,
    "student": 1,
    "staff": 2,
    "lecturer": 3,
    "it_staff": 4,
    "hr_only": 5,
    "restricted": 5,
}

ROLE_RANK = {
    "external": 0,
    "student": 1,
    "staff": 2,
    "lecturer": 3,
    "it_staff": 4,
    "hr": 5,
    "admin_manager": 5,
}

def load_documents(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["authority_score"] = df["authority"].map(AUTHORITY_SCORE).fillna(0.5)
    df["freshness_score"] = df.apply(_freshness_score, axis=1)
    return df

def _freshness_score(row) -> float:
    if str(row.get("status", "")).lower() in {"deprecated", "obsolete"}:
        return 0.0
    try:
        effective = datetime.strptime(str(row["effective_date"]), "%Y-%m-%d")
        age_days = max((datetime.now() - effective).days, 0)
        if age_days <= 365:
            return 1.0
        if age_days <= 3 * 365:
            return 0.75
        return 0.4
    except Exception:
        return 0.5

def user_can_access(role: str, access_level: str) -> bool:
    role_score = ROLE_RANK.get(role, 0)
    access_score = ACCESS_RANK.get(access_level, 5)
    if access_level == "hr_only":
        return role in {"hr", "admin_manager"}
    return role_score >= access_score
