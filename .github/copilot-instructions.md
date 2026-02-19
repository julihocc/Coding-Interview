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
  ├── queues/          # basic-queue, printer-queue (FIFO applications)
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
    ├── solution_template.py  # Starter code with NotImplementedError
    ├── solution_naive.py     # Brute-force approach
    ├── solution_optimized.py # Efficient approach
    ├── solution_iterative.py # Variant approach (optional)
    ├── solution_recursive.py # Variant approach (optional)
    ├── contributed/          # Community solutions (optional)
    └── reference/            # Legacy pattern: naive.py, optimized.py (optional)
```

**Critical invariants**:
- Solution class **must** be named `Solution` (not problem-specific names)
- Test class **must** be named `TestCase` with `TEST_CASES` list
- `judge.py` must define `run_case_logic(SolutionClass, case)` function
- All `.py` files in solutions/ must have a `Solution` class (excludes `__init__.py`, `solution_template.py`)
- `contributed/` folder holds community solutions without validation requirements

### Algorithm Solution Pattern (e.g., find-first-occurrence)

```python
from typing import List

class Solution:
    """Descriptive docstring of algorithm strategy."""
    
    def __init__(self, nums: List[int]):
        """Store test data once for all method calls."""
        self.nums = nums
    
    def find_first_occurrence(self, target: int) -> int:
        """Find index of first occurrence of target.
        
        Args:
            target: Value to search for
        
        Returns:
            Index of first occurrence, or -1 if not found
        """
        # Implementation
        pass
```

**Judge call pattern**:
```python
# In judge.py
def run_case_logic(SolutionClass, case):
    """Test a single case."""
    instance = SolutionClass(case.nums)  # Initialize with test data
    result = instance.find_first_occurrence(case.target)  # Call method with only problem params
    return result == case.expected

# In main judge invocation
from utils.judge_utils import run_judge_from_file
run_judge_from_file(__file__, TEST_CASES, run_case_logic)
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

### Queue Pattern (e.g., basic-queue)

```python
from collections import deque

class Solution:
    """Queue operations with O(1) enqueue/dequeue."""
    
    def __init__(self):
        self.queue = deque()  # Use deque for O(1) operations
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        return self.queue.popleft() if self.queue else None
    
    def peek(self):
        return self.queue[0] if self.queue else None
```

## Developer Workflows

### Running Tests

```bash
# Run all solutions against all test cases for one problem
python algorithms/search/find-first-occurrence/judge.py

# Data structure examples
python data-structures/heaps/min-heap/judge.py
python data-structures/queues/basic-queue/judge.py

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

**Enforced naming rules**:
- **solutions/ root**: Only `solution_naive.py`, `solution_optimized.py`, `solution_template.py`, `__init__.py` allowed
- **Variant solutions**: `solution_iterative.py`, `solution_recursive.py` also permitted
- **Legacy reference/ subfolder**: `naive.py`, `optimized.py` for backward compatibility
- **Allowed subdirectories**: `reference/`, `contributed/`, `__pycache__/`
- **Disallowed**: Any other `.py` files, random subfolders, or misnamed solution files
- **Test files**: Must reside in `tests/` root (not nested in solutions/)

**Run validation**: `python tools/validate_main_branch.py`

This ensures all PRs maintain consistent structure and prevents accidental invalid patterns.

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

- `load_classes(dir, class_name, subfolder='reference', file_pattern="*.py")` → list of (name, class) tuples. Pass `subfolder=None` to load from directory root.
- `load_classes_with_method(dir, method_name, subfolder='reference')` → finds classes defining a specific method (useful when class names vary)
- `run_judge_from_file(__file__, test_cases, run_case_logic)` → execute judge with formatted output and timing
- `run_tests(solutions, test_cases, runner_func, section_name, report_dir)` → generic test runner with report generation

## Common Patterns to Recognize

1. **Reflection-based discovery**: No hardcoded imports; judges find solutions dynamically
2. **Data initialization in init**: All array/list problems store data in `__init__()` to enable stateful method calls
3. **Heap problems use 1-indexed arrays**: `self.H = [None]` is standard to simplify parent/child index math
4. **Queue problems use collections.deque**: `self.queue = deque()` for O(1) enqueue/dequeue operations
5. **No external file I/O**: All solutions are pure functions/classes; test data passed via constructor
6. **Method naming reflects problem**: `find_first_occurrence()`, `delete_min()`, `enqueue()`, etc., not generic names

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
