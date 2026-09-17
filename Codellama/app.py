"""Local CodeLlama workbench powered by Ollama."""

import requests
import streamlit as st

from prompt_router import TASKS, build_prompt

st.set_page_config(page_title="Local CodeLlama Workbench", layout="wide")
st.title("Local CodeLlama Workbench")
st.caption("One local model, five explicit software-engineering workflows")

with st.sidebar:
    endpoint = st.text_input("Ollama endpoint", "http://localhost:11434")
    model = st.text_input("Model", "codellama")
    task = st.selectbox("Task", list(TASKS))
    language = st.selectbox("Language", ["python", "javascript", "typescript", "cpp", "java", "sql"])

context = st.text_input("Project context", placeholder="CLI parser, FastAPI route, data pipeline…")
code = st.text_area("Code", height=360, placeholder="Paste code here")

if st.button("Run local review", type="primary", disabled=not code):
    try:
        routed = build_prompt(task, language, code, context)
        response = requests.post(
            f"{endpoint.rstrip('/')}/api/generate",
            json={"model": model, "prompt": routed.prompt, "stream": False},
            timeout=180,
        )
        response.raise_for_status()
        st.subheader(task)
        st.markdown(response.json()["response"])
        with st.expander("Prompt sent to local model"):
            st.code(routed.prompt)
    except requests.RequestException as exc:
        st.error(f"Could not reach Ollama: {exc}")
    except (KeyError, ValueError) as exc:
        st.error(str(exc))
