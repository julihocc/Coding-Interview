# Copilot Instructions: Google Interview Practice

## Project Overview

This is a **coding interview practice repository** implementing a **Virtual Judge System** for algorithm and data structure problems. Solutions are **class-based with init-based stateful design** — test data is stored in `__init__()` for reusability, and methods operate on instance attributes. Each problem has multiple solution approaches (naive vs. optimized) that are automatically tested and benchmarked.

## Core Architecture: Class-Based Stateful Solutions

**Key Design Pattern:** All solutions (algorithms and data structures) are now classes, not functions.
- **Init-based state:** Constructor stores problem inputs; methods operate on `self.attribute`
- **Descriptive names:** Class names reflect strategy (e.g., `BinarySearchFinder`, `RandomizedQuickselect`, `InPlaceRandomizedQuicksort`)
- **No method parameters for input:** Data passed to `__init__`, not method args
- **Single method per problem:** Main method name varies by problem (e.g., `find_first_occurrence()`, `quickselect()`, `insert()`)

**Quick reference:**
- [utils/judge_utils.py](utils/judge_utils.py) — `load_classes_with_method()` discovers classes by method name
- [algorithms/search/find-first-occurrence](algorithms/search/find-first-occurrence) — algorithm example (init stores nums, method takes target)
- [data-structures/heaps/min-heap](data-structures/heaps/min-heap) — data structure example (init sets up state, methods manipulate heap)

## Solution Patterns

### Algorithm Problems (Search/Sorting)

**Solution Structure (Init-Based Stateful):**
```python
# algorithms/search/find-first-occurrence/solutions/reference/optimized.py
class BinarySearchFinder:
    def __init__(self, nums: List[int]):
        self.nums = nums  # Store data in init for reusability
    
    def find_first_occurrence(self, target: int) -> int:
        # Operate on self.nums, method takes only remaining args
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

**Judge Pattern (Instantiate with data, call method):**
```python
from utils.judge_utils import load_classes_with_method, run_tests

def run_case_logic(SolutionClass, case):
    instance = SolutionClass(list(case.nums))  # Init with test data
    result = instance.find_first_occurrence(case.target)  # Call method
    return result == case.expected

solutions = load_classes_with_method(solutions_dir, 'find_first_occurrence')
run_tests(solutions, TEST_CASES, run_case_logic)
```

### Data Structure Problems (Heaps, Arrays)

**Solution Structure (Class with helper methods):**
```python
# data-structures/heaps/min-heap/solutions/reference/optimized.py
class MinHeap:
    def __init__(self):
        self.H = [None]  # 1-indexed array

    def insert(self, elt):
        self.H.append(elt)
        self._bubble_up(len(self.H) - 1)

    def delete_min(self):
        if self.size() == 1:
            return self.H.pop()
        min_val = self.H[1]
        self.H[1] = self.H.pop()
        self._bubble_down(1)
        return min_val

    def min_element(self):
        return self.H[1] if self.size() > 0 else None

    def size(self):
        return len(self.H) - 1

    def _bubble_up(self, idx):
        while idx > 1:
            parent = idx // 2
            if self.H[parent] <= self.H[idx]:
                break
            self.H[parent], self.H[idx] = self.H[idx], self.H[parent]
            idx = parent

    def _bubble_down(self, idx):
        # Implementation of sift-down for heap property
        pass
```

**Judge Pattern (Instantiate, call methods with test data):**
```python
def run_case_logic(MinHeap, case):
    h = MinHeap()
    for x in case.elements:
        h.insert(x)
    return h.min_element() == case.expected_min
```

## Template Guidance System

All 11 problem templates (6 algorithms + 5 data structures) now include **comprehensive guidance**:

- **Method docstrings** with expected behavior and examples
- **Helper method stubs** showing algorithm decomposition (e.g., `_partition()`, `_bubble_up()`, `_helper()`)
- **Implementation hints** suggesting strategy options ("Linear scan vs. Binary search")
- **Time/space complexity notes** for context
- **Edge case guidance** embedded in docstrings

### Template Examples

**Quickselect (algorithm):**
```python
def _partition(self, left: int, right: int, pivot_index: int) -> int:
    """Partition array around a pivot...
    1. Swap pivot to right boundary (use _swap helper)
    2. Iterate left to right, moving smaller elements left
    3. Swap pivot to final position
    4. Return final position
    """

def _swap(self, i: int, j: int) -> None:
    """Swap two elements in self.nums by their indices."""
```

**MedianHeap (data structure):**
```python
def _rebalance(self):
    """Rebalance the two heaps to maintain median property.
    Ensures: len(lower) >= len(upper) and len(lower) - len(upper) <= 1
    """
```

Templates guide users to implement solutions without revealing the algorithm.

## File Structure & Validation

**Per-Problem Organization:**
```
problem-name/
  ├── judge.py              # Test runner using load_classes_with_method()
  ├── README.md             # Problem description
  ├── PSEUDOCODE.md         # Algorithm pseudocode guide
  ├── solutions/
  │   ├── __init__.py
  │   ├── template.py       # Guiding scaffold (not tested)
  │   ├── reference/
  │   │   ├── __init__.py
  │   │   ├── naive.py      # Reference implementation
  │   │   └── optimized.py  # Reference implementation
  │   └── contributed/      # User submissions (not validated on main)
  └── tests/
      ├── __init__.py
      └── cases.py          # TestCase dataclass + TEST_CASES list
```

**Main Branch Validation (tools/validate_main_branch.py):**
- ✅ Allowed in `solutions/reference/`: `naive.py`, `optimized.py`, `__init__.py`
- ✅ Allowed in `solutions/`: `template.py`, `__init__.py`
- ❌ Rejected: `solution_v1.py`, `my_solution.py`, `hints.py` on main
- ✅ Allowed in `solutions/contributed/`: Any filename (no main validation)

## Development Workflows

### Running Judges
```bash
# Single judge
python algorithms/search/find-first-occurrence/judge.py

# Data structure judge
python data-structures/heaps/min-heap/judge.py

# Output format
=== REFERENCE SOLUTIONS ===
Solution          | Case      | Status | Time (s)
--------------------------------------------------
LinearScanFinder  | Example   | PASS   | 0.000022
BinarySearchFinder| Example   | PASS   | 0.000009
```

### Adding a New Algorithm Problem
1. Create `algorithms/[category]/[problem]/` folder
2. Implement `tests/cases.py` with `TestCase` dataclass and `TEST_CASES` list
3. Add to `solutions/reference/`: `naive.py`, `optimized.py` (export classes matching judge's method name)
4. Create `judge.py` calling `load_classes_with_method(solutions_dir, 'method_name')`
5. Write `solutions/template.py` with guiding docstrings and helper stubs
6. Test: `python algorithms/[category]/[problem]/judge.py`

### Adding a New Data Structure Problem
1. Create `data-structures/[category]/[problem]/` folder
2. Similar structure but focus on class methods: `__init__()`, core operations, helpers
3. Template shows expected method signatures and rebalancing/maintenance logic
4. Test against operations that verify internal invariants

## Project-Specific Rules for Agents

**Critical Patterns:**
- **Init-based state, not method params:** All solutions store input data in `__init__`, methods operate on `self.attribute`
- **Class names reflect strategy:** `BinarySearchFinder` (not `Solution`), `RandomizedQuickselect` (not `Selector`)
- **Copy mutable inputs:** Use `list(case.nums)` when passing to judge to avoid cross-test mutations
- **Preserve sys.path pattern:** All judges use the 3-level directory traversal for imports (required by test runner)
- **Method signatures match judge expectations:** Judge calls `instance.method_name(args)` — args only what's not in `__init__`
- **No function wrappers:** Classes export directly, no `solve()` function

**Template Philosophy:**
- Templates are **guiding scaffolds**, not implementations
- Show helper methods (e.g., `_partition()`, `_bubble_up()`) as stubs with docstrings
- Provide algorithm hints ("Use binary search with left refinement") in docstrings
- Include examples in expected behavior sections
- Never reveal the solution algorithm in template hints

**Configuration:**
- Do not modify `pyproject.toml`, `utils/judge_utils.py`, or CI config without explicit instruction
- Keep `__init__.py` files in solution folders (required for imports)
- All problems use same judge discovery mechanism: `load_classes_with_method(dir, method_name)`

## Key Files to Reference

- **Test Runner:** [utils/judge_utils.py](utils/judge_utils.py) — `load_classes_with_method()`, `run_tests()`
- **Validation:** [tools/validate_main_branch.py](tools/validate_main_branch.py) — main branch policy enforcement
- **Algorithm Example (Init-Based):** [algorithms/search/find-first-occurrence/judge.py](algorithms/search/find-first-occurrence/judge.py)
- **Data Structure Example:** [data-structures/heaps/min-heap/judge.py](data-structures/heaps/min-heap/judge.py)
- **Template Example:** [algorithms/sorting/quickselect/solutions/template.py](algorithms/sorting/quickselect/solutions/template.py)
- **Reference Implementation:** [algorithms/search/find-first-occurrence/solutions/reference/optimized.py](algorithms/search/find-first-occurrence/solutions/reference/optimized.py)
