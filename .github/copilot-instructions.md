# Copilot Instructions: Google Interview Practice

## Project Overview

This is a **coding interview practice repository** implementing a **Virtual Judge System** for algorithm problems. Each problem has multiple solution approaches (naive vs. optimized) that are automatically tested and benchmarked.

## Architecture Pattern: Virtual Judge System

# Copilot Instructions: Google Interview Practice

This repo is a Virtual Judge for algorithm interview problems. Each problem has a local
`judge.py`, a `README.md`, a `solutions/` folder with multiple approaches (`naive.py`, `optimized.py`, etc.),
and `tests/cases.py` providing dataclass-based test input/expected pairs.

**Quick links:** [utils/judge_utils.py](utils/judge_utils.py#L1),
[algorithms/search/find-crossover-indices/judge.py](algorithms/search/find-crossover-indices/judge.py#L1)

**Architecture & data flow**
- Per-problem `judge.py` loads `TEST_CASES` from `tests/cases.py` and uses
    `utils.judge_utils.load_solutions()` to discover solution callables.
- `run_tests()` in `utils/judge_utils.py` runs each solution against each case, timing and
    reporting results. Input lists are copied (e.g. `list(case.a)`) to ensure isolation.

**Important patterns & conventions**
- Problem template: a `judge.py`, `README.md`, `solutions/` and `tests/` directory.
- Filenames: prefer `naive.py`, `optimized.py`, `original.py` for multiple implementations.
- Each solution file should export exactly one function with the name `judge.py` expects.
- `judge.py` uses this sys.path trick to import project-level utils:
    ```python
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))
    from utils.judge_utils import load_solutions, run_tests
    ```

**How tests and judges run**
- From the repo root run a single judge: `python algorithms/search/find-crossover-indices/judge.py`
- CI/quick-run examples use `uv run python <path>` in docs; `uv` is a convenience wrapper used
    by contributors but normal `python` works too.

**Adding a new problem**
1. Copy an existing problem folder (follow the template).
2. Implement `tests/cases.py` with a `TestCase` dataclass and a `TEST_CASES` list.
3. Add solutions to `solutions/` (one function per file). Keep function names in sync with `judge.py`.
4. Update `judge.py` to call `load_solutions(<solutions_dir>, '<function_name>')` and validate via `run_case_logic()`.
5. Run the new `judge.py` from the repo root to verify behavior and timings.

**Project-specific rules for agents**
- Do not change `pyproject.toml` or global project settings without explicit instruction.
- Preserve the `sys.path` import pattern in `judge.py` files — tests rely on this layout.
- Keep solution function signatures and type hints intact; tests use these to call functions.
- Use `list(case.<field>)` when forwarding lists to solutions to avoid cross-test mutation.

**Key files to inspect when making changes**
- [utils/judge_utils.py](utils/judge_utils.py#L1) — test discovery & runner
- [main.py](main.py#L1) — repo entry (if present)
- Example problem judge: [algorithms/search/find-crossover-indices/judge.py](algorithms/search/find-crossover-indices/judge.py#L1)

If anything here is unclear or you want me to expand examples (e.g., show a minimal
`judge.py` or a compliant `solutions/naive.py`), tell me which area to expand.

---
Please review these edits and tell me if you'd like more examples or stricter rules.
```bash
