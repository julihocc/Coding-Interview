# Copilot Instructions for Google Interview Interview Repository

## Architecture: Virtual Judge System

This codebase implements a **Virtual Judge System** for algorithm and data structure problems. The core pattern is **class-based solutions** where:

- Solutions are stateful classes initialized with test data in `__init__()`
- Algorithms use class methods to reduce argument count via state storage
- Judges dynamically discover and instantiate all solution classes via reflection
- Test cases are dataclass-based for portability and clarity

**Key insight**: The `__init__()` pattern enables the judge to populate static data once, then call methods with only problem-specific parameters.

## Repository Structure & Patterns

### Canonical Paths

```
algorithms/
  ├── search/          # Binary search variants (9 problems)
  └── sorting/         # O(n log n) algorithms (quicksort, merge-sort, quickselect)

data-structures/
  ├── arrays/          # left-rotation (function-based, not class)
  ├── heaps/           # min/max/median heaps, top-k selection
  └── stacks/          # monotonic stacks, max/min tracking

utils/
  └── judge_utils.py   # load_classes(), load_solutions(), run_judge_from_file()

tools/
  └── validate_main_branch.py  # CI: enforces file naming + structure
```

### Standard Problem Module Structure

Every problem directory follows this layout:

```
problem-name/
├── README.md                 # Problem statement + function signature
├── ALGORITHM_ANALYSIS.md     # Time/space complexity analysis
├── judge.py                  # Entry point: calls run_judge_from_file()
├── tests/
│   ├── __init__.py
│   └── cases.py             # @dataclass TestCase + TEST_CASES list
└── solutions/
    ├── __init__.py
    ├── solution_template.py # Starter code with NotImplementedError
    ├── solution_naive.py    # Brute-force approach
    ├── solution_optimized.py # Efficient approach (may also have solution_recursive.py)
    └── contributed/         # (optional) Community solutions
```

**Critical invariants**:
- Solution class **must** be named `Solution` (not problem-specific names)
- Test class **must** be named `TestCase` with `TEST_CASES` list
- `judge.py` must define `run_case_logic(SolutionClass, case)` function

### Algorithm Solution Pattern (e.g., find-first-occurrence)

```python
class Solution:
    """Descriptive docstring of algorithm strategy."""
    
    def __init__(self, nums: List[int]):
        """Store test data """
        self.nums = nums
    
    def find_first_occurrence(self, target: int) -> int:
        # Implementation
        pass
```

**Judge call pattern**:
```python
instance = Solution(case.nums)
result = instance.find_first_occurrence(case.target)
assert result == case.expected
```

### Data Structure Pattern (e.g., min-heap)

```python
class Solution:
    """Heap operations with O(log n) insert/delete."""
    
    def __init__(self):
        self.H = [None]  # 1-indexed array (always)
    
    def insert(self, elt):
        self.H.append(elt)
        self._bubble_up(len(self.H) - 1)
    
    def delete_min(self):
        # Remove root, move last to root, bubble down
        pass
    
    def _bubble_up(self, idx):
        # Helper: recursive or iterative
        pass
```

## Developer Workflows

### Running Tests

```bash
# Run all solutions against all test cases for one problem
python algorithms/search/find-first-occurrence/judge.py

# Test a single solution file
python algorithms/search/find-first-occurrence/solutions/solution_naive.py

# Run pytest for entire codebase (if test files exist)
pytest --cov=. --cov-report=html
```

### Adding New Problems

1. Create problem directory: `algorithms/category/problem-name/`
2. Follow standard structure (README.md, ALGORITHM_ANALYSIS.md, judge.py, tests/, solutions/)
3. `judge.py` must call `run_judge_from_file(__file__, TEST_CASES, run_case_logic)`
4. Define `run_case_logic(SolutionClass, case)` that instantiates the class and compares results

### Code Style & Validation

- Follow **Google Python Style Guide**: max 80 chars, `snake_case` for functions, `PascalCase` for classes
- Type annotations required for all public APIs
- Docstrings mandatory: one-liner + Args/Returns/Raises sections
- Line length: 80 characters maximum
- Import order: standard library → third-party → project imports

### CI Validation (validate_main_branch.py)

PR validation enforces:
- Solution files ONLY: `solution_naive.py`, `solution_optimized.py`, `solution_template.py`, `__init__.py`
- Legacy support: `reference/` subfolder with `naive.py`, `optimized.py`
- **Disallowed**: mystery files, misnamed classes, random subfolders
- Test files in `tests/` root, not in solutions/

Run validation: `python tools/validate_main_branch.py`

## Testing & Assertions

### Test Case Structure (uses dataclass)

```python
from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    target: int
    nums: List[int]
    expected: int

TEST_CASES = [
    TestCase(id="example", target=3, nums=[1,2,3], expected=2),
    TestCase(id="edge_empty", target=5, nums=[], expected=-1),
]
```

### Judge Response Pattern

- Solutions discovered dynamically (excludes `__init__.py`, `solution_template.py`, `hints.py`)
- For each solution × test case: instantiate, call method, compare result
- Output includes execution time for performance analysis
- Framework handles failed tests gracefully

## Key Utilities (utils/judge_utils.py)

- `load_classes(dir, class_name, subfolder='reference')` → list of (name, class) tuples
- `run_judge_from_file(__file__, test_cases, run_case_logic)` → execute judge
- `test_solution(SolutionClass, test_cases, run_case_logic)` → test one solution

## Common Patterns to Recognize

1. **Reflection-based discovery**: No hardcoded imports; judges find solutions dynamically
2. **Data initialization in init**: All array/list problems store data in `__init__()` to enable stateful method calls
3. **Heap problems use 1-indexed arrays**: `self.H = [None]` is standard to simplify parent/child index math
4. **No external file I/O**: All solutions are pure functions/classes; test data passed via constructor
5. **Method naming reflects problem**: `find_first_occurrence()`, `delete_min()`, etc., not generic names

## When Creating New Solutions

- Start from `solution_template.py`: copy, rename to `solution_naive.py` or `solution_optimized.py`
- Template includes docstrings with algorithm hints but NOT implementations
- Naive solution: brute-force, easy to understand
- Optimized solution: efficient algorithm (binary search, heap operations, etc.)
- Every new solution must pass all test cases in TEST_CASES

## Debugging & Troubleshooting

- **Import errors**: Verify `__init__.py` exists in `solutions/` and `tests/`
- **Class not found**: Ensure class is named exactly `Solution`
- **Test failures**: Check `run_case_logic()` correctly instantiates SolutionClass with test data
- **Name errors**: Review that solution file is not in ignore list (`solution_template.py` excluded from judges)

## Tech Stack

- **Python 3.14+** (requires-python in pyproject.toml)
- **pytest** for testing framework
- **ruff** for linting
- **uv** recommended for environment/dependency management
