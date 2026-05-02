import subprocess
import sys
import os
import pytest

SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "app",
    "program.py"
)

@pytest.mark.parametrize("input_val, expected", [
    (1, "Result: 2"),
    (5, "Result: 10"),
    (10, "Result: 20"),
])
def test_program_output(input_val, expected):
    result = subprocess.run(
        [sys.executable, SCRIPT_PATH, str(input_val)],
        capture_output=True,
        text=True
    )

    output = result.stdout.strip()
    
    assert result.returncode == 0
    assert output == expected