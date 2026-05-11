<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Human Review Results | EAGLE Harness</title>
  <meta name="description" content="Human review results for the EAGLE Harness IT helpdesk chatbot prototype.">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="site-header">
  <nav class="nav">
    <a class="brand" href="index.html">EAGLE Harness</a>
    <button class="nav-toggle" aria-label="Toggle navigation">☰</button>
    <div class="nav-links">
      <a href="architecture.html">Architecture</a>
      <a href="experiment.html">Experiment</a>
      <a href="prototype.html">Prototype</a>
      <a href="human-review-results.html">Human Review Results</a>
      <a href="dry-run-results.html">Dry-run Metrics</a>
      <a href="paper.html">Paper</a>
    </div>
  </nav>
</header>

<main class="page">
  <h1>Human Review Results</h1>
  <p class="lead">
    This page reports the preliminary two-reviewer human evaluation of the EAGLE Harness IT helpdesk chatbot prototype.
    The evaluation covers 45 student-facing IT helpdesk questions answered by three systems: Standard RAG, Agentic RAG,
    and EAGLE Harness.
  </p>

  <section class="section callout">
    <h2>Interpretation note</h2>
    <p>
      These results are preliminary expert-review results from a limited IT helpdesk corpus. They strengthen the project
      beyond a dry-run smoke test, but they do not replace a full evaluation with stronger baselines, hybrid retrieval,
      claim-level verification, red-team tests, and production latency/cost analysis.
    </p>
  </section>

  <section class="section">
    <h2>Evaluation setup</h2>
    <table>
      <tbody>
        <tr><th>Question set</th><td>45 IT helpdesk questions</td></tr>
        <tr><th>Systems compared</th><td>Standard RAG, Agentic RAG, EAGLE Harness</td></tr>
        <tr><th>Generated answers</th><td>135 answers</td></tr>
        <tr><th>Human reviewers</th><td>2 reviewers</td></tr>
        <tr><th>Total human ratings</th><td>270 answer-level reviews</td></tr>
        <tr><th>Rating scale</th><td>1 = poor / wrong / unsafe; 5 = excellent</td></tr>
      </tbody>
    </table>
  </section>

  <section class="section">
    <h2>Normalized mean scores by system</h2>
    <p>
      Scores are normalized to the range 0–1 by dividing the 1–5 human rating by 5.
    </p>
    <table><thead><tr><th>System</th><th>Correctness</th><th>Groundedness</th><th>Citation precision</th><th>Completeness</th><th>Usefulness</th><th>Risk handling</th><th>Ratings</th></tr></thead><tbody><tr><td>Standard RAG</td><td>0.787</td><td>0.916</td><td>0.831</td><td>0.778</td><td>0.780</td><td>0.920</td><td>90</td></tr>
<tr><td>Agentic RAG</td><td>0.804</td><td>0.916</td><td>0.831</td><td>0.778</td><td>0.767</td><td>0.924</td><td>90</td></tr>
<tr><td>EAGLE Harness</td><td>0.844</td><td>0.938</td><td>0.871</td><td>0.831</td><td>0.820</td><td>0.951</td><td>90</td></tr></tbody></table>
  </section>

  <section class="section">
    <h2>Mean scores by system on the original 1–5 scale</h2>
    <table><thead><tr><th>System</th><th>Correctness</th><th>Groundedness</th><th>Citation precision</th><th>Completeness</th><th>Usefulness</th><th>Risk handling</th><th>Ratings</th></tr></thead><tbody><tr><td>Standard RAG</td><td>3.933</td><td>4.578</td><td>4.156</td><td>3.889</td><td>3.900</td><td>4.600</td><td>90</td></tr>
<tr><td>Agentic RAG</td><td>4.022</td><td>4.578</td><td>4.156</td><td>3.889</td><td>3.833</td><td>4.622</td><td>90</td></tr>
<tr><td>EAGLE Harness</td><td>4.222</td><td>4.689</td><td>4.356</td><td>4.156</td><td>4.100</td><td>4.756</td><td>90</td></tr></tbody></table>
  </section>

  <section class="section">
    <h2>Inter-rater agreement check</h2>
    <p>
      Exact agreement is the proportion of rows where the two reviewers gave the same score for a metric.
      Groundedness shows lower agreement than the other dimensions, which is expected because reviewers may interpret
      source support differently.
    </p>
    <table><thead><tr><th>Metric</th><th>Mean absolute difference</th><th>Exact agreement rate</th></tr></thead><tbody><tr><td>Correctness</td><td>0.000</td><td>1.000</td></tr>
<tr><td>Groundedness</td><td>0.370</td><td>0.733</td></tr>
<tr><td>Citation precision</td><td>0.000</td><td>1.000</td></tr>
<tr><td>Completeness</td><td>0.000</td><td>1.000</td></tr>
<tr><td>Usefulness</td><td>0.022</td><td>0.978</td></tr>
<tr><td>Risk handling</td><td>0.089</td><td>0.919</td></tr></tbody></table>
  </section>

  <section class="section">
    <h2>Download result files</h2>
    <ul>
      <li><a href="docs/human_review_completed_combined_2reviewers.csv">Combined answer-level human review file</a></li>
      <li><a href="docs/human_review_summary_by_mode_2reviewers.csv">Human review summary by mode, 1–5 scale</a></li>
      <li><a href="docs/human_review_summary_by_mode_2reviewers_normalized.csv">Human review summary by mode, normalized 0–1 scale</a></li>
      <li><a href="docs/human_review_interrater_check.csv">Inter-rater agreement check</a></li>
      <li><a href="docs/evaluation_summary3.csv">Automatic governance dry-run metrics</a></li>
    </ul>
  </section>

  <section class="section">
    <h2>What these results support</h2>
    <p>
      The preliminary human review suggests that EAGLE performs better than the two baselines in this limited IT helpdesk
      pilot, especially for correctness, completeness, citation precision, usefulness, and risk handling. However, the
      result should be interpreted as a prototype evaluation rather than final production evidence.
    </p>
  </section>
</main>

<footer><p>© EAGLE Harness Project. Preliminary research prototype.</p></footer>
<script src="assets/js/main.js"></script>
</body>
</html>
