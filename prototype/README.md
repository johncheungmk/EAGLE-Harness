# EAGLE Prototype

Run locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Optional LLM API:

```bash
cp .env.example .env
# Add OPENAI_API_KEY
```

Run batch evaluation:

```bash
python run_evaluation.py
```
