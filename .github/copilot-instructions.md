# Copilot Instructions: Google Interview Practice

## Project Overview

**Virtual Judge System** for algorithm & data structure interview problems. Solutions use **class-based patterns** with solutions naming per problem (e.g., `solution_naive.py`, `solution_optimized.py`) exporting a unified `Solution` class. Each problem auto-runs all solutions against test suites with timing/benchmarking.

## Core Architecture: Solution Loading & Judging

**Current Implementation:**
- **Solution discovery:** `load_classes()` in [utils/judge_utils.py](utils/judge_utils.py) scans `solution_*.py` files for a `Solution` class
- **Judge pattern:** Each problem's `judge.py` calls `run_judge_from_file(__file__, TEST_CASES, run_case_logic)` — simplified boilerplate
- **Test structure:** `tests/cases.py` defines `@dataclass TestCase` with unique `id` field; judges reference `case.id` for reporting
- **Init-based state:** Test data passed to `__init__`, core logic operates on `self.attribute`

**Key files:**
- [utils/judge_utils.py](utils/judge_utils.py) — `load_classes()`, `run_judge_from_file()`, `run_tests()` with μs-scale timing
- [algorithms/search/find-first-occurrence/judge.py](algorithms/search/find-first-occurrence/judge.py) — pattern example
- [algorithms/search/find-first-occurrence/tests/cases.py](algorithms/search/find-first-occurrence/tests/cases.py) — TestCase pattern

## Solution Pattern: Init-Based Stateful Class Design

**All problems:**
- Store test data in `__init__()` for reusability across method calls
- Core logic operates on `self.attribute`
- Export single class named `Solution` (not strategy-named descriptors)
- Method names vary per problem (e.g., `find_first_occurrence()`, `insert()`, `quickselect()`)

**Example (Algorithm):**
```python
# algorithms/search/find-first-occurrence/solutions/solution_optimized.py
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums  # Data in init
    
    def find_first_occurrence(self, target: int) -> int:
        # Operate on self.nums, remaining args to method
        low, high = 0, len(self.nums) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if self.nums[mid] == target:
                result = mid
                high = mid - 1
            elif self.nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result
```

**Example (Data Structure):**
```python
# data-structures/heaps/min-heap/solutions/solution_optimized.py
class Solution:
    def __init__(self):
        self.H = [None]  # 1-indexed heap array
    
    def insert(self, elt):
        self.H.append(elt)
        self._bubble_up(len(self.H) - 1)
    
    def delete_min(self):
        min_val = self.H[1]
        self.H[1] = self.H.pop()
        self._bubble_down(1)
        return min_val
    
    def _bubble_up(self, idx):
        while idx > 1:
            parent = idx // 2
            if self.H[parent] <= self.H[idx]:
                break
            self.H[parent], self.H[idx] = self.H[idx], self.H[parent]
            idx = parent
```

**Judge Pattern:**
```python
from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    instance = SolutionClass(case.nums)  # Init with test data
    result = instance.find_first_occurrence(case.target)  # Call method
    return result == case.expected

if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
```

## Test Case & Judge Structure

**TestCase Pattern** (`tests/cases.py`):
```python
from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str  # Unique identifier for reporting (e.g., "Example", "Edge case")
    target: int  # Input-specific fields vary by problem
    nums: List[int]
    expected: int

TEST_CASES = [
    TestCase(id="Example", target=3, nums=[1, 2, 3, 4, 5], expected=2),
    TestCase(id="Not found", target=10, nums=[1, 2, 3], expected=-1),
]
```

**Judge Boilerplate** (`judge.py`):
```python
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    instance = SolutionClass(case.nums)
    result = instance.find_first_occurrence(case.target)
    return result == case.expected

if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
```

**Report Output:**
```
Solution   | Case      | Status | Time (μs)
-----------+-----------+--------+----------
solution   | Example   | PASS   | 0.1
solution   | Not found | PASS   | 0.1
```

## File Structure & Validation

**Per-Problem Organization:**
```
problem-name/
  ├── judge.py              # Test runner using run_judge_from_file()
  ├── README.md             # Problem description
  ├── PSEUDOCODE.md         # Algorithm pseudocode guide
  ├── solutions/
  │   ├── solution_naive.py       # First implementation approach
  │   ├── solution_optimized.py   # Optimized approach (both export Solution class)
  │   └── solution_template.py    # Guiding template (not auto-tested)
  └── tests/
      └── cases.py          # TestCase dataclass + TEST_CASES list
```

**Main Branch Validation** ([tools/validate_main_branch.py](tools/validate_main_branch.py)):
- ✅ Allowed: `solution_*.py` files in `solutions/` (all test reference implementations)
- ✅ Allowed: `solution_template.py` (guidance, not tested)
- ❌ Rejected on main: Non-standard filenames like `my_solution.py`, `hints.py`
- ✅ Allowed: contributed/ folder (future user submissions)

## Development Workflows

### Running Judges
```bash
# Single judge
python algorithms/search/find-first-occurrence/judge.py

# Data structure judge
python data-structures/heaps/min-heap/judge.py

# Output format (solutions auto-discovered and tested):
Solution   | Case      | Status | Time (μs)
-----------+-----------+--------+----------
solution   | Example   | PASS   | 0.1
solution   | Not found | PASS   | 0.1
```

### Adding a New Problem
1. Create `[category]/[problem]/` folder with `solutions/` and `tests/` subfolders
2. Write `tests/cases.py`: define `TestCase` dataclass with `id` field and `TEST_CASES` list
3. Implement `solutions/solution_naive.py` and `solutions/solution_optimized.py` (both export `Solution` class)
4. Create `solutions/solution_template.py` with guidance (docstrings, helper stubs, hints)
5. Create `judge.py`: call `run_judge_from_file(__file__, TEST_CASES, run_case_logic)`
6. Test: `python [category]/[problem]/judge.py`

## Project-Specific Rules for Agents

**Critical Patterns:**
- **Single `Solution` class:** Export `Solution` (not strategy-named), all files in `solutions/` folder
- **Init-based state:** Store test data in `__init__()`, methods operate on `self.attribute` only
- **Copy mutable inputs:** Judge passes `case.nums` directly; implementations should not mutate
- **Preserve sys.path pattern:** 3-level directory traversal for imports (required by `run_judge_from_file()`)
- **Method signatures match judge:** `run_case_logic()` instantiates with test data, calls method with remaining args
- **No function wrappers:** Classes export directly, no `solve()` wrapper

**Template Philosophy:**
- Templates are **guiding scaffolds**, not implementations
- Show helper methods (e.g., `_partition()`, `_bubble_up()`) as stubs with docstrings
- Provide algorithm hints ("Use binary search") in docstrings, never reveal solution
- Include edge case guidance and expected behavior examples
- Tests should not reference template files

**Configuration:**
- Do not modify `pyproject.toml`, `utils/judge_utils.py`, or CI workflows without explicit instruction
- All problems use: `run_judge_from_file(__file__, TEST_CASES, run_case_logic)`
- Judge auto-discovers and tests all `solution_*.py` files (except `solution_template.py`)

**Testing Individual Solutions:**
- Solutions can be tested directly: `python algorithms/search/find-first-occurrence/solutions/solution_naive.py`
- Each solution's `__main__` block uses `test_solution()` helper for isolated testing
- Preferred for development: test individual solutions before running full judge

**Documentation Standards:**
- `ALGORITHM_ANALYSIS.md`: Complexity analysis, pseudocode (CLRS style), step-by-step walkthroughs
- `PSEUDOCODE.md`: Alternative format for algorithm guides (used in some data structures)
- `README.md`: Problem statement, examples, constraints
- Use LaTeX for math: `$O(n)$` inline, `$$...$$` for blocks

## Key Files to Reference

- **Solution class pattern:** [algorithms/search/find-first-occurrence/solutions/solution_naive.py](algorithms/search/find-first-occurrence/solutions/solution_naive.py)
- **Judge pattern:** [algorithms/search/find-first-occurrence/judge.py](algorithms/search/find-first-occurrence/judge.py)
- **Test case pattern:** [algorithms/search/find-first-occurrence/tests/cases.py](algorithms/search/find-first-occurrence/tests/cases.py)
- **Test runner:** [utils/judge_utils.py](utils/judge_utils.py) — `run_judge_from_file()`, `load_classes()`, `test_solution()`
- **Validation rules:** [tools/validate_main_branch.py](tools/validate_main_branch.py) — main branch policy
- **Data structure example:** [data-structures/heaps/min-heap/solutions/solution_optimized.py](data-structures/heaps/min-heap/solutions/solution_optimized.py)
- **Algorithm analysis example:** [algorithms/search/find-first-occurrence/ALGORITHM_ANALYSIS.md](algorithms/search/find-first-occurrence/ALGORITHM_ANALYSIS.md)




