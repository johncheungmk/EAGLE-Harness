# EAGLE Harness

**EAGLE** = **Evidence-Aware Governed Lifecycle Engine** for trustworthy knowledge-intensive LLM agents.

EAGLE reframes an LLM agent harness as a governance-centric runtime for institutional knowledge work. The project includes a GitHub Pages site, a runnable Python/Streamlit prototype, and preliminary IT helpdesk chatbot evaluation materials.

## Project website

GitHub Pages site:

```text
https://johncheungmk.github.io/EAGLE-Harness/
```

Main repository:

```text
https://github.com/johncheungmk/EAGLE-Harness
```

## What is included

```text
.
├── index.html
├── architecture.html
├── experiment.html
├── dry-run-results.html
├── human-review-results.html
├── prototype.html
├── paper.html
├── docs/
│   ├── dry_run_metrics_aggregate.csv
│   ├── evaluation_summary3.csv
│   ├── human_review_completed_combined_2reviewers.csv
│   ├── human_review_summary_by_mode_2reviewers.csv
│   ├── human_review_summary_by_mode_2reviewers_normalized.csv
│   └── human_review_interrater_check.csv
├── assets/
│   ├── css/style.css
│   └── js/main.js
├── prototype/
│   ├── app.py
│   ├── run_evaluation.py
│   ├── requirements.txt
│   ├── data/
│   └── eagle/
└── LICENSE
```

## Main features

- Evidence-aware retrieval and ranking
- Authority and freshness-aware evidence scoring
- Evidence graph logging
- Policy and risk decision layer
- Risk-aware action handling
- Standard RAG, Agentic RAG, and EAGLE comparison modes
- Preliminary human review results for an IT helpdesk chatbot prototype

## Human review results

The repository includes a preliminary two-reviewer human evaluation of the IT helpdesk chatbot prototype:

- 45 IT helpdesk questions
- 3 systems: Standard RAG, Agentic RAG, and EAGLE Harness
- 135 generated answers
- 2 reviewers
- 270 answer-level reviews

Result page:

```text
human-review-results.html
```

Downloadable CSV files are stored in:

```text
docs/
```

## Run the prototype locally

```bash
cd prototype
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Run evaluation

```bash
cd prototype
python run_evaluation.py
```

## Important publishing warning

Do **not** upload private institutional documents, personal data, student data, HR records, salary records, unpublished policies, API keys, `.env` files, or confidential evaluation logs to a public GitHub repository.

Use only anonymised, public, or synthetic datasets for the public site.

## Current status

This repository is a research prototype. The current evaluation should be interpreted as a preliminary prototype and human-review study, not a full production validation. Future work should include stronger retrieval baselines, claim-level verification, red-team testing, latency/cost measurement, and policy-engine integration.

## License

This project is released under the MIT License.
