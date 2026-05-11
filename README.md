# EAGLE Harness GitHub Site

**EAGLE** = Evidence-Aware Governed Lifecycle Engine for Trustworthy Knowledge-Intensive LLM Agents.

This repository contains a ready-to-host GitHub Pages site plus a runnable Python prototype.

## Why host this on GitHub Pages?

GitHub Pages is suitable because it can publish static project documentation directly from a repository branch or via GitHub Actions. The official GitHub documentation states that Pages can publish when changes are pushed to a branch, and the source can be either the repository root or the `/docs` folder.

## Repository structure

```text
.
├── index.html
├── architecture.html
├── experiment.html
├── prototype.html
├── paper.html
├── docs/
│   └── implementation-guide.html
├── assets/
│   ├── css/style.css
│   └── js/main.js
├── prototype/
│   ├── app.py
│   ├── run_evaluation.py
│   ├── requirements.txt
│   ├── data/
│   └── eagle/
└── .github/workflows/pages.yml
```

## Option A: Deploy from branch

1. Create a new GitHub repository, for example `eagle-harness`.
2. Upload all files in this package to the repository root.
3. Go to **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch `main` and folder `/root`.
6. Save.

Your site will be available at:

```text
https://YOUR-USERNAME.github.io/eagle-harness/
```

## Option B: Deploy using GitHub Actions

This package includes:

```text
.github/workflows/pages.yml
```

To use it:

1. Push the repository to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **GitHub Actions**.
4. Push to `main` or manually run the workflow.

## Run the prototype locally

```bash
cd prototype
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Important publishing warning

Do not upload private institutional documents, personal data, student data, HR records, salary records, unpublished policies, API keys, `.env` files, or confidential evaluation logs to a public GitHub repository.

Use anonymised, public, or synthetic datasets for the public site.
