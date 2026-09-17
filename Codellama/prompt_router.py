"""Task-specific prompt construction for a local coding model."""

from __future__ import annotations

from dataclasses import dataclass

TASKS = {
    "Explain": "Explain the code's control flow, data flow, complexity and assumptions.",
    "Debug": "Find the most likely defect, explain the failure mode and provide a minimal patch.",
    "Generate tests": "Write focused tests covering normal behavior, boundaries and failure cases.",
    "Refactor": "Improve clarity and maintainability without changing observable behavior.",
    "Security review": "Identify concrete security risks, their impact and safer code changes.",
}


@dataclass(frozen=True)
class RoutedPrompt:
    task: str
    prompt: str


def build_prompt(task: str, language: str, code: str, context: str = "") -> RoutedPrompt:
    if task not in TASKS:
        raise ValueError(f"Unsupported task: {task}")
    if not code.strip():
        raise ValueError("Code is required.")
    instruction = TASKS[task]
    prompt = f"""You are a careful senior {language} engineer.
Task: {instruction}
Project context: {context or "Not provided"}

Code:
```{language}
{code}
```

Return:
1. Findings
2. Reasoning
3. Proposed code or tests
4. Remaining risks
Do not claim that you executed the code."""
    return RoutedPrompt(task=task, prompt=prompt)
