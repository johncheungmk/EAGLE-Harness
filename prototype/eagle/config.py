from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class EagleConfig:
    documents_path: str = "data/documents.csv"
    questions_path: str = "data/questions.csv"
    logs_path: str = "outputs/eagle_logs.jsonl"
    top_k: int = 5
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
