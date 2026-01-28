# Repository Structure Guide

This document outlines the standard structure for problem modules in this repository. All new problem modules MUST follow this structure.

## Directory Structure

Each problem module (e.g., `algorithms/search/your-problem-name`) must contain:

```
your-problem-name/
├── README.md                 # Problem statement and function signature
├── ALGORITHM_ANALYSIS.md     # Detailed analysis of algorithms (time/space complexity)
├── judge.py                  # Entry point for running tests
├── tests/
│   ├── __init__.py           # Makes tests a package
│   └── cases.py              # Test cases definition
└── solutions/
    ├── __init__.py           # Makes solutions a package
    ├── solution_template.py  # Starter code for users
    ├── solution_recursive.py # Recursive implementation
    ├── solution_iterative.py # Iterative implementation
    ├── solution_naive.py     # Naive/Brute-force implementation
```

## File Details

### `judge.py`

Must import `run_judge_from_file` from `utils.judge_utils` and `TEST_CASES` from `tests.cases`.
Must define a `run_case_logic(SolutionClass, case)` function.

### `solutions/solution_*.py`

Each solution file must define a class named `Solution`.
The file name should reflect the approach (e.g., `solution_recursive.py`, `solution_iterative.py`).
**Important**: The class naming convention inside the file must be `Solution` to be compatible with the test runner.

### `solutions/solution_template.py`

Must also define a `Solution` class with the method signature but empty implementation (or raising `NotImplementedError` or returning a default).

### `tests/cases.py`

Must define a `dataclass` named `TestCase` and a list named `TEST_CASES`.

## Common Mistakes

- Missing `__init__.py` in `solutions/` or `tests/`.
- Naming the solution class something other than `Solution`.
- Missing `ALGORITHM_ANALYSIS.md`.
