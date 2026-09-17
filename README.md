# Local CodeLlama Engineering Workbench

A privacy-oriented coding assistant that routes source code into five explicit engineering workflows and runs entirely against a local Ollama endpoint.

## Distinct use case

This repository is not a general chat application and does not use hosted RAG. It is a **local code-review workbench** for:

- explanation
- debugging
- test generation
- behavior-preserving refactoring
- security review

Each workflow receives a different system instruction and produces a predictable four-part response.

## Architecture

~~~mermaid
flowchart LR
    A["Source code"] --> B["Task router"]
    B --> C["Structured prompt"]
    C --> D["Local Ollama / CodeLlama"]
    D --> E["Findings, patch and risks"]
~~~

## Run

~~~bash
ollama pull codellama
ollama serve
git clone https://github.com/sandeep848/codellama-dynamic-prompt-handler.git
cd codellama-dynamic-prompt-handler
pip install -r Codellama/requirements.txt
streamlit run Codellama/app.py
~~~

No cloud API key is required and pasted code stays on the machine hosting Ollama.

## Test

~~~bash
pytest
~~~

## Key distinction

The routing layer is deterministic and inspectable. The application shows the exact prompt sent to the model and explicitly states that generated feedback has not been executed.
