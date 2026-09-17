import pytest

from prompt_router import TASKS, build_prompt


@pytest.mark.parametrize("task", list(TASKS))
def test_each_task_has_distinct_instruction(task):
    routed = build_prompt(task, "python", "print('hello')")
    assert TASKS[task] in routed.prompt
    assert routed.task == task


def test_requires_code():
    with pytest.raises(ValueError):
        build_prompt("Debug", "python", "")
