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

## Advanced Pattern: Dual-Heap Strategy (Median Heap)

The **MedianMaintainingHeap** demonstrates managing two interrelated heaps to efficiently track a median:

**Architecture:**
```python
class MedianMaintainingHeap:
    def __init__(self):
        self.lower = []  # max-heap via negatives for elements below median
        self.upper = []  # min-heap for elements above median
    
    def insert(self, elt):
        # Step 1: Insert into appropriate heap
        if not self.lower or elt <= -self.lower[0]:
            heapq.heappush(self.lower, -elt)  # Negate for max-heap behavior
        else:
            heapq.heappush(self.upper, elt)
        
        # Step 2: Rebalance to maintain: len(lower) >= len(upper) and diff <= 1
        self._rebalance()
    
    def get_median(self):
        # If uneven: return element from larger heap (always lower)
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        # If even: return average of both roots
        return (-self.lower[0] + self.upper[0]) / 2
    
    def _rebalance(self):
        # Move excess from lower to upper, or from upper to lower
        if len(self.lower) > len(self.upper) + 1:
            mv = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, mv)
        elif len(self.upper) > len(self.lower):
            mv = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -mv)
```

**Key Insight:** The invariant `len(lower) >= len(upper)` ensures O(1) median access. Always rebalance after every insert to maintain this property.

**When adding similar problems:** Use the dual-structure pattern whenever you need to maintain two conflicting orderings (e.g., top-k smallest with overflow heap, or lower/upper half of sorted data).

## Adding a New Problem Type: Complete Walkthrough

### Scenario: Implement "Find Peak in Mountain Array"
**Expected:** A problem where we need to find a peak element using binary search.

### Step 1: Create Directory Structure
```bash
mkdir -p algorithms/search/find-peak-in-mountain/solutions/reference
mkdir -p algorithms/search/find-peak-in-mountain/solutions/contributed
mkdir -p algorithms/search/find-peak-in-mountain/tests
touch algorithms/search/find-peak-in-mountain/solutions/__init__.py
touch algorithms/search/find-peak-in-mountain/solutions/reference/__init__.py
```

### Step 2: Write Test Cases (`tests/cases.py`)
```python
from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    arr: List[int]
    expected: int
    name: str

TEST_CASES = [
    TestCase([1, 3, 2], 1, "Example"),
    TestCase([1, 2, 3, 1], 2, "Peak at end of rise"),
    TestCase([3, 4, 5, 1, 2], 2, "Peak before drop"),
]
```

### Step 3: Write Reference Solutions
```python
# solutions/reference/naive.py
class LinearSearchPeakFinder:
    def __init__(self, arr: List[int]):
        self.arr = arr
    
    def find_peak(self) -> int:
        for i in range(1, len(self.arr) - 1):
            if self.arr[i] > self.arr[i-1] and self.arr[i] > self.arr[i+1]:
                return i
        # Handle edge cases (peak at boundaries)
        return 0 if self.arr[0] > self.arr[-1] else len(self.arr) - 1

# solutions/reference/optimized.py
class BinarySearchPeakFinder:
    def __init__(self, arr: List[int]):
        self.arr = arr
    
    def find_peak(self) -> int:
        left, right = 0, len(self.arr) - 1
        while left < right:
            mid = (left + right) // 2
            if self.arr[mid] > self.arr[mid + 1]:
                right = mid  # Peak is on left side (including mid)
            else:
                left = mid + 1  # Peak is on right side
        return left
```

### Step 4: Create Template (`solutions/template.py`)
```python
"""TEMPLATE: Find Peak in Mountain Array

Implement a class whose name reflects the strategy (e.g., BinarySearchPeakFinder).
Judges instantiate your class with arr in __init__ and call the method.
"""

class YourPeakFinder:
    """Rename and implement this class to match your approach.
    
    Example strategies: LinearSearchPeakFinder, BinarySearchPeakFinder
    """

    def __init__(self, arr: List[int]):
        """Initialize with the mountain array.
        
        Args:
            arr: A mountain array (increases then decreases).
        """
        self.arr = arr

    def find_peak(self) -> int:
        """Find index of peak element in the mountain.
        
        Expected behavior:
        - Return the index where arr[index] > arr[index-1] and arr[index] > arr[index+1]
        - For O(log n), use binary search to narrow down the peak location
        
        Args:
            None (data in self.arr)
            
        Returns:
            The index of the peak element.
        """
        # TODO: Implement peak-finding strategy
        pass
```

### Step 5: Create Judge (`judge.py`)
```python
import os
import sys
from typing import List

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_classes_with_method, run_tests
from tests.cases import TEST_CASES

solutions_dir = os.path.join(current_dir, "solutions")

def run_case_logic(SolutionClass, case):
    instance = SolutionClass(list(case.arr))
    result = instance.find_peak()
    return result == case.expected

solutions = load_classes_with_method(solutions_dir, 'find_peak')
run_tests(solutions, TEST_CASES, run_case_logic, case_name_attr='name')
```

### Step 6: Test
```bash
python algorithms/search/find-peak-in-mountain/judge.py
```

**Expected Output:**
```
=== REFERENCE SOLUTIONS ===
Solution              | Case              | Status | Time (s)
----------------------------------------------------------------
LinearSearchPeakFinder| Example           | PASS   | 0.000015
BinarySearchPeakFinder| Example           | PASS   | 0.000009
LinearSearchPeakFinder| Peak at end...    | PASS   | 0.000003
BinarySearchPeakFinder| Peak at end...    | PASS   | 0.000002
```

## Debugging & Testing Workflow

### Running Individual Judges
```bash
# Run all tests for a problem
python algorithms/search/find-first-occurrence/judge.py

# Capture output to file for inspection
python algorithms/search/find-first-occurrence/judge.py > results.txt
```

### Debugging a Failing Solution
If a solution fails a test case:

1. **Print intermediate state:**
   ```python
   # In your solution, add debug output
   def find_peak(self) -> int:
       left, right = 0, len(self.arr) - 1
       print(f"Array: {self.arr}, searching for peak...")
       while left < right:
           mid = (left + right) // 2
           print(f"left={left}, right={right}, mid={mid}, arr[mid]={self.arr[mid]}")
           # ... rest of logic
   ```

2. **Test locally with print:**
   ```python
   # Create minimal test
   from solutions.reference.optimized import BinarySearchPeakFinder
   finder = BinarySearchPeakFinder([1, 3, 2])
   result = finder.find_peak()
   print(f"Result: {result}, Expected: 1")
   ```

3. **Verify TestCase structure:**
   - Check `tests/cases.py` that `TestCase` has all required fields
   - Ensure `TEST_CASES` list is properly formatted
   - Verify field names match what judge expects (e.g., `arr`, `expected`, `name`)

### Common Issues & Fixes

**"TypeError: takes no arguments"**
- **Cause:** Method signature doesn't match judge expectations
- **Fix:** Verify `__init__` takes test data, method takes only remaining args
- **Example:** Judge does `instance.find_peak()`, so method must have 0 args (data in self)

**"KeyError: 'expected'"**
- **Cause:** TestCase missing required field
- **Fix:** Check `tests/cases.py` has all fields the judge expects

**"ModuleNotFoundError: No module named 'solutions'"**
- **Cause:** sys.path not set correctly in judge.py
- **Fix:** Ensure judge uses 3-level directory traversal (from problem dir → algorithms/data-structures → root)

**Inconsistent results across runs**
- **Cause:** Solutions modifying mutable input (list/dict)
- **Fix:** Ensure judge passes copies: `list(case.arr)` not `case.arr`
- **Also fix:** Solutions should not mutate input unless explicitly testing in-place behavior

### Verifying Judge Correctness
```bash
# Run all problem judges in sequence (quick validation)
for dir in algorithms/search/*/; do
    echo "Testing $dir"
    python "$dir/judge.py" || exit 1
done

# Run with timing
time python data-structures/heaps/min-heap/judge.py
```

### Manual Verification Pattern
```python
# Manual test to verify solution logic before running judge
from solutions.reference.optimized import MinHeap

h = MinHeap()
test_elements = [5, 3, 7, 1]
for x in test_elements:
    h.insert(x)

assert h.min_element() == 1, "Expected min to be 1"
assert h.size() == 4, "Expected size to be 4"
assert h.delete_min() == 1, "Expected delete_min to return 1"
assert h.size() == 3, "Expected size to be 3 after deletion"
print("✓ All manual tests passed!")
```
