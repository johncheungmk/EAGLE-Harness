# EAGLE Harness Site Progress Update v8

This package contains updated GitHub Pages content for the EAGLE Harness repository.

## What changed

- Added `progress.html`.
- Added `dry-run-results.html` with the latest Windows 11 dry-run table.
- Updated experiment, prototype, architecture, and paper pages.
- Added clear warnings that dry-run values are not final empirical findings.

## Current dry-run summary

| System | Citation rate | Avg. sources | Avg. risk score | Conflict detection | Block rate | Human approval |
|---|---:|---:|---:|---:|---:|---:|
| standard_rag | 1.000 | 2.867 | 0.000 | 0.000 | 0.000 | 0.000 |
| agentic_rag | 1.000 | 2.867 | 0.733 | 0.000 | 0.000 | 0.000 |
| eagle | 0.933 | 2.867 | 1.267 | 0.000 | 0.067 | 0.000 |


## How to update GitHub

Copy these files into the root of `https://github.com/johncheungmk/EAGLE-Harness` and commit.

```bash
git add .
git commit -m "Update EAGLE progress pages and dry-run results"
git push
```

## Warning

Do not treat these values as final empirical results. Human-rated evaluation is still required.
