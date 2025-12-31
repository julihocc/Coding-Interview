# Copilot Instructions: Google Interview Practice

## Project Overview

This is a **coding interview practice repository** implementing a **Virtual Judge System** for algorithm problems. Each problem has multiple solution approaches (naive vs. optimized) that are automatically tested and benchmarked.

## Architecture Pattern: Virtual Judge System

This repo is a Virtual Judge for algorithm interview problems. Each problem has a local `judge.py`, a `README.md`, a `solutions/` folder with multiple approaches (`naive.py`, `optimized.py`, etc.), and `tests/cases.py` providing dataclass-based test input/expected pairs.

**Quick links:** 
- [utils/judge_utils.py](utils/judge_utils.py#L1) — test discovery & runner
- [algorithms/search/find-crossover-indices/judge.py](algorithms/search/find-crossover-indices/judge.py#L1) — function-based judge example
- [data-structures/heaps/min-heap/judge.py](data-structures/heaps/min-heap/judge.py#L1) — class-based judge example

## Two Judge Patterns

### 1. Function-Based Judges (Algorithms)
Used for: **Search** and **Sorting** problems

**Solution Structure:**
```python
# algorithms/search/find-first-occurrence/solutions/naive.py
def solve(arr, target):
    """Find first occurrence of target in sorted array."""
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1
```

**Judge Pattern:**
```python
from utils.judge_utils import load_solutions, run_tests

def run_case_logic(sol_func, case):
    """Test function solution."""
    result = sol_func(list(case.arr), case.target)
    return result == case.expected

solutions = load_solutions(solutions_dir, 'solve')
run_tests(solutions, TEST_CASES, run_case_logic)
```

### 2. Class-Based Judges (Data Structures)
Used for: **Heaps** and other data structure problems

**Solution Structure:**
```python
# data-structures/heaps/min-heap/solutions/naive.py
class MinHeap:
    def __init__(self):
        self.H = [None]  # 1-indexed array
    
    def insert(self, elt):
        self.H.append(elt)
        self.bubble_up(len(self.H) - 1)
    
    def min_element(self):
        return self.H[1]
    
    # ... other methods
```

**Judge Pattern:**
```python
from utils.judge_utils import load_classes, run_tests

def run_case_logic(MinHeap, case):
    """Test class solution."""
    h = MinHeap()
    for x in case.elements:
        h.insert(x)
    return h.min_element() == case.expected_min

solutions = load_classes(solutions_dir, 'MinHeap')
run_tests(solutions, TEST_CASES, run_case_logic)
```

## Architecture & Data Flow

- Per-problem `judge.py` loads `TEST_CASES` from `tests/cases.py`
- Calls `load_solutions()` (for functions) or `load_classes()` (for classes) to discover solution callables
- `run_tests()` runs each solution against each case, timing and reporting results
- Input lists are copied (e.g. `list(case.a)`) to ensure isolation between test runs

## Important Patterns & Conventions

**File Structure:**
- Problem folder contains: `judge.py`, `README.md`, `PSEUDOCODE.md`, `solutions/`, `tests/`
- Solution files: `naive.py`, `optimized.py` (one implementation per file)
- No `hints.py` or solution code in `template.py`

**For Function-Based Solutions:**
- Export exactly one function named `solve` (or other name specified in judge)
- Wrap function if needed to match judge expectations

**For Class-Based Solutions:**
- Export exactly one class by name (e.g., `MinHeap`, `MedianMaintainingHeap`)
- No `solve()` wrapper function
- Class methods should match the interface used in the judge

**Global Import Pattern:**
All `judge.py` files use this sys.path trick:
```python
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))
from utils.judge_utils import load_solutions, load_classes, run_tests
```

## How to Run Tests

- From repo root, run single judge: `python algorithms/search/find-crossover-indices/judge.py`
- Or: `python data-structures/heaps/min-heap/judge.py`
- CI/quick-run uses `uv run python <path>` (uv is optional convenience wrapper)

## Adding a New Problem

### For Algorithm (Function-Based)
1. Copy existing search/sorting problem folder structure
2. Implement `tests/cases.py` with `TestCase` dataclass and `TEST_CASES` list
3. Add solutions: `solutions/naive.py`, `solutions/optimized.py` (export `solve` function)
4. Create `judge.py` that calls `load_solutions(solutions_dir, 'solve')`
5. Define `run_case_logic(sol_func, case)` to test the function
6. Run judge to verify

### For Data Structure (Class-Based)
1. Copy existing heap problem folder structure
2. Implement `tests/cases.py` with `TestCase` dataclass and `TEST_CASES` list
3. Add solutions: `solutions/naive.py`, `solutions/optimized.py` (export the class, no wrapper)
4. Create `judge.py` that calls `load_classes(solutions_dir, 'ClassName')`
5. Define `run_case_logic(ClassName, case)` to test the class
6. Run judge to verify

## Project-Specific Rules for Agents

- Do not change `pyproject.toml` or global project settings without explicit instruction
- Preserve the `sys.path` import pattern in all `judge.py` files
- Keep solution function/class signatures and type hints intact
- Use `list(case.<field>)` when forwarding mutable inputs to solutions to avoid cross-test mutation
- Templates show structure only (class/function signatures with TODOs), not implementations
- Validate files: only `naive.py`, `optimized.py`, `__init__.py`, `template.py` allowed in `solutions/`
- No `hints.py` files in repository (validation script enforces this)

## Key Files to Reference

- [utils/judge_utils.py](utils/judge_utils.py) — contains `load_solutions()`, `load_classes()`, `run_tests()`
- [tools/validate_main_branch.py](tools/validate_main_branch.py) — enforces file naming and structure
- Function-based example: [algorithms/search/find-crossover-indices/judge.py](algorithms/search/find-crossover-indices/judge.py)
- Class-based example: [data-structures/heaps/min-heap/judge.py](data-structures/heaps/min-heap/judge.py)

---

For questions about specific patterns or need more detailed examples, review the examples linked above or ask.
