import streamlit as st
import pandas as pd
from eagle.harness import EagleHarness

st.set_page_config(page_title="EAGLE Harness Prototype", layout="wide")

st.title("EAGLE Harness Prototype")
st.caption("Evidence-Aware Governed Lifecycle Engine for LLM Agents")

@st.cache_resource
def load_harness():
    return EagleHarness()

harness = load_harness()

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    query = st.text_area("Question", value="Which password policy is valid now?", height=100)

with col2:
    role = st.selectbox("User role", ["external", "student", "staff", "lecturer", "it_staff", "hr", "admin_manager"], index=3)

with col3:
    mode = st.selectbox("Mode", ["standard_rag", "agentic_rag", "eagle"], index=2)

if st.button("Run"):
    result = harness.answer(query=query, role=role, mode=mode)

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Policy decision")
    st.json(result["policy"])

    st.subheader("Conflict report")
    st.json(result["conflict_report"])

    st.subheader("Retrieved evidence")
    rows = []
    for d in result["retrieved"]:
        rows.append({
            "doc_id": d["doc_id"],
            "title": d["title"],
            "topic": d["topic"],
            "status": d["status"],
            "access_level": d["access_level"],
            "sensitivity": d["sensitivity"],
            "retrieval": round(d["retrieval_score"], 3),
            "authority": round(d["authority_score"], 3),
            "freshness": round(d["freshness_score"], 3),
            "evidence": round(d["evidence_score"], 3),
        })
    st.dataframe(pd.DataFrame(rows), use_container_width=True)

    st.subheader("Evidence graph JSON")
    st.json(result["evidence_graph"])
