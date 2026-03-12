# Project Guidelines

## Architecture
- This repository uses a virtual judge pattern for interview problems.
- Most algorithm solutions are class-based and stateful: test data is stored in `__init__()`, then methods accept only problem parameters.
- Judges dynamically discover solution classes using reflection utilities in `utils/judge_utils.py`.
- Canonical judge flow:
  1. Define `run_case_logic(SolutionClass, case)`.
  2. Instantiate `SolutionClass(...)` using case data.
  3. Compare method output with expected.
  4. Call `run_judge_from_file(__file__, TEST_CASES, run_case_logic)`.

## Build And Test
- Python requirement: `>=3.14` (see `pyproject.toml`).
- Set up dependencies (recommended): `uv sync`.
- Run a problem judge: `python path/to/problem/judge.py`.
- Lint/format: `ruff check .` and `ruff format .`.
- Optional broad tests: `CI=true pytest --cov=. --cov-report=html`.
- Validate branch policy before PRs to main: `python tools/validate_main_branch.py`.

## Conventions
- Keep the standard problem structure:
  - `README.md`
  - `ALGORITHM_ANALYSIS.md`
  - `judge.py`
  - `tests/cases.py`
  - `solutions/`
- Solution class name must be exactly `Solution`.
- Test class in `tests/cases.py` must be `TestCase` with `TEST_CASES`.
- In `solutions/`, preferred filenames are:
  - `solution_template.py`
  - `solution_naive.py`
  - `solution_optimized.py`
  - optional: `solution_iterative.py`, `solution_recursive.py`
- Legacy layout is still accepted by validation (`template.py` + `reference/{naive.py,optimized.py}`).
- Do not add arbitrary Python files under `solutions/`; validation enforces strict names.

## Code Style
- Follow Google Python style conventions used by the repository.
- Keep lines at or under 80 characters.
- Use type annotations for public APIs.
- Include concise docstrings for public classes/methods.
- Preserve import order: standard library, third-party, local.

## High-Value Pitfalls
- Missing `__init__.py` in `tests/` or `solutions/` can break imports/discovery.
- Misnaming `Solution` or solution filenames causes judge/CI discovery failures.
- Avoid hardcoded solution imports in judges; rely on loader utilities.
- Exclude templates from execution through `load_classes(..., file_pattern="solution_*.py", subfolder=None)`.
