import streamlit as st
from services.analyzer import analyze_document
from services.negotiator import generate_reply
from services.timeline import build_timeline
from services.scorer import score_case
from utils.file_parser import parse_file

st.set_page_config(page_title="Exit Assistant AI", layout="wide")
st.title("AI Employment Exit Assistant")

tab1, tab2, tab3, tab4 = st.tabs([
    "Analyzer",
    "Reply",
    "Timeline",
    "Score"
])

with tab1:
    st.subheader("Upload Document")

    uploaded = st.file_uploader(
        "Upload PDF / Image / Text",
        type=["pdf","png","jpg","jpeg","webp","txt"]
    )

    manual = st.text_area("atau paste teks manual")

    if st.button("Analyze"):

        text = ""

        if uploaded:
            text = parse_file(uploaded)

        if manual:
            text += manual

        if text.strip()=="":
            st.warning("No input")
        else:
            result = analyze_document(text)
            st.markdown(result)


with tab2:
    ctx = st.text_area("Situation")
    if st.button("Generate"):
        st.write(generate_reply(ctx))

with tab3:
    data = st.text_area("Events")
    if st.button("Build"):
        st.write(build_timeline(data))

with tab4:
    facts = st.text_area("Facts")
    if st.button("Evaluate"):
        st.write(score_case(facts))
