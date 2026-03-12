# Coding Interview Practice

A repository of coding interview problems and solutions implementing a **Virtual Judge System** for algorithm and data structure problems. Each problem features multiple solution approaches (Naive vs. Optimized) that are automatically tested and benchmarked.

## 🎓 For Students

**New to this repository?** Start with the [**Learning Guide**](LEARNING_GUIDE.md) - a structured 7-week roadmap that takes you from data structure fundamentals to advanced algorithms. The guide organizes all 35 problems in optimal learning order with:

- 📚 Progressive difficulty levels
- ⏱️ Time estimates for each problem
- 🎯 Clear learning objectives
- 🔗 Concept dependencies
- ✅ Progress tracking checklist

## 🤝 For Contributors

**Want to add problems to this repository?** Check out the [**Contributing Guide**](CONTRIBUTING.md) - a comprehensive guide to AI-assisted problem creation:

- 🤖 AI prompting templates for each file type
- 📋 Step-by-step contribution workflow
- ✅ Validation checklists
- 💡 Example conversation flows
- 🎯 Pattern-consistent integration

## Architecture: Virtual Judge System

This repo uses a **class-based solution pattern** where solutions are implemented as reusable classes with:

- **Init-based stateful design:** Test data stored in `__init__()` for reusability across method calls
- **Descriptive class names:** Names reflect the strategy (e.g., `BinarySearchFinder`, `RandomizedQuickselect`)
- **Comprehensive templates:** Guiding method structures with docstrings showing helper methods and algorithm hints
- **Automatic judge discovery:** Judges load classes via reflection and instantiate them with test data

## Repository Structure

```text
google-interview/
├── algorithms/
│   ├── search/
│   │   ├── find-first-occurrence/
│   │   │   ├── solutions/
│   │   │   │   ├── solution_template.py  # Guiding template with method stubs
│   │   │   │   ├── solution_naive.py     # LinearScanFinder class
│   │   │   │   └── solution_optimized.py # BinarySearchFinder class
│   │   │   ├── tests/cases.py            # Test case dataclasses
│   │   │   ├── judge.py                  # Virtual judge for this problem
│   │   │   ├── README.md                 # Problem description
│   │   │   └── PSEUDOCODE.md             # Algorithm pseudocode
│   │   ├── find-crossover-indices/
│   │   ├── integer-cube-root/
│   │   ├── locate-first-last-float/
│   │   ├── locate-first-last-position/
│   │   ├── search-insert-position/
│   │   ├── search-insert-position-left/
│   │   ├── search-rotated-sorted-array/
│   │   ├── search-rotated-sorted-array-descending/
│   │   └── target-index-search/
│   └── sorting/
│       ├── multiway-merge/
│       ├── quickselect/
│       └── quicksort/
├── data-structures/
│   ├── arrays/
│   │   └── left-rotation/                # Function-based problem
│   ├── heaps/
│   │   ├── min-heap/                     # Class-based data structure
│   │   ├── max-heap/
│   │   ├── median-heap/
│   │   ├── median-finder/                # Real-world data stream median
│   │   └── top-k-heap/
│   ├── linked-lists/
│   │   ├── linked-list/                  # Singly linked list fundamentals
│   │   ├── doubly-linked-list/           # Doubly linked list fundamentals
│   │   ├── circular-linked-list/         # Circular linked list
│   │   ├── doubly-linked-list-backward-display/ # Backward traversal after deletion
│   │   ├── linked-list-size-tracker/     # Debugging: size counter bug fix
│   │   └── linked-list-insert-after-head/ # O(1) insert after head
│   ├── queues/
│   │   ├── basic-queue/                  # FIFO queue implementation
│   │   ├── printer-queue/                # Real-world queue application
│   │   ├── queue-interleaving/           # Interleave approach
│   │   ├── interleave-two-queues/        # Interleave two queues
│   │   └── moving-average-from-data-stream/ # Sliding window
│   ├── stacks/
│   │   ├── max-stack/                    # O(1) max tracking
│   │   ├── min-stack/                    # O(1) min tracking
│   │   └── daily-temperatures/           # Monotonic stack
│   └── trees/
│       ├── binary-tree-traversal/        # In-order traversal
│   │   ├── binary-search-tree/           # BST Insert, Search, Delete
│   │   ├── check-bst-balance/            # Balance checking
│   │   ├── max-height-diff-bst/          # Max subtree height diff
│   │   ├── kth-smallest-bst/             # K-th smallest element
│   │   ├── planet-continents-dfs/        # DFS traversal
│       ├── breadth-first-search-tree/    # BFS practice in Python
│       ├── rainforest-bfs/               # BFS applied to forests
│       ├── planet-network-bfs/           # Planetary network BFS
│       ├── company-hierarchy-bfs/        # BFS on team tree chart with bug fix
│       ├── family-tree-level-bfs/        # BFS level calculation on family tree
│       └── network-bfs/                  # Network concept BFS
│   └── graphs/
│       ├── adjacency-matrix/             # Graph connectivity and representation
│       └── detect-cycle/                 # Cycle detection in undirected graphs
├── utils/
│   └── judge_utils.py                    # Utilities: load_classes(), load_solutions(), run_tests()
└── tools/
    └── validate_main_branch.py           # CI policy enforcement
```

## Problem Patterns

### 1. Algorithm Problems (Search & Sorting)

**Pattern:** Class-based solutions with method calls

**Solution structure:**

```python
# Example: find-first-occurrence/solutions/solution_optimized.py
class BinarySearchFinder:
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def find_first_occurrence(self, target: int) -> int:
        # Binary search implementation
        pass
```

**Judge pattern:**

```python
# Judge instantiates with test data, calls method with reduced args
instance = BinarySearchFinder(list(case.nums))
result = instance.find_first_occurrence(case.target)
```

### 2. Data Structure Problems (Heaps, Stacks, Queues, Arrays)

**Pattern:** Class-based implementations with structural helpers

**Solution structure (Heap example):**

```python
# Example: heaps/min-heap/solutions/solution_optimized.py
class MinHeap:
    def __init__(self):
        self.H = [None]  # 1-indexed array
    
    def insert(self, elt):
        # Insert and bubble-up
        pass
    
    def delete_min(self):
        # Remove min and bubble-down
        pass
    
    def _bubble_up(self, idx):
        # Helper for maintaining heap property
        pass
```

**Judge pattern:**

```python
# Judge instantiates, inserts test data, verifies structure
h = MinHeap()
for x in case.elements:
    h.insert(x)
assert h.min_element() == case.expected_min
```

## Solution Templates

All templates now include **comprehensive guidance** without revealing solutions:

### Algorithms (Search/Sort)

Templates show:

- **Main method docstring** with expected behavior and examples
- **Helper method stubs** (e.g., `_partition()`, `_helper()`, `_swap()`)
- **Implementation hints** showing strategy options
- **Time/space complexity notes**

Example: Quickselect template guides users to implement:

- `quickselect(k)` – main selection logic
- `_partition(left, right, pivot_index)` – split around pivot
- `_swap(i, j)` – element exchange helper

### Data Structures (Heaps, Stacks, Queues, Arrays)

Templates show:

- **Data structure initialization** guidance
- **Core operation methods** with docstrings
- **Helper operations** (e.g., `_bubble_up()`, `_bubble_down()`)
- **Rebalancing logic** for complex structures

Example: MedianHeap template guides users to implement:

- `insert(elt)` – add element and rebalance
- `get_median()` – retrieve median efficiently
- `_rebalance()` – maintain heap balance invariants

Example: Queue template guides users to implement:

- `enqueue(element)` – add element to end (O(1))
- `dequeue()` – remove from front (O(1))
- `peek()` – view front without removing

## Getting Started

### For Structured Learning

📖 **Follow the [Learning Guide](LEARNING_GUIDE.md)** for a curated 7-week learning path through all problems, organized from fundamentals to advanced topics.

### Prerequisites

- **Python 3.10+**
- **uv** (Recommended for dependency management)

### Installation

```bash
git clone https://github.com/julihocc/google-interview.git
cd google-interview
uv sync
```

## Running Judges (Virtual Judge System)

Each problem directory contains a `judge.py` that automatically:

1. **Discovers** all solution classes via reflection
2. **Loads** test cases from `tests/cases.py`
3. **Executes** every solution against every test case
4. **Reports** results (PASS/FAIL) with execution time

### Run Individual Judges

```bash
# Algorithm example: Binary search problem
python algorithms/search/find-first-occurrence/judge.py

# Data structure example: Heap problem
python data-structures/heaps/min-heap/judge.py

# Stack example: Max Stack
python data-structures/stacks/max-stack/judge.py

# Queue example: Basic Queue
python data-structures/queues/basic-queue/judge.py

# Sorting example
python algorithms/sorting/quickselect/judge.py
```

### Run Individual Solutions

You can also run any solution file directly to test it against the cases. This is useful for debugging a specific implementation without running all other solutions.

```bash
# Run specific solution implementation
python algorithms/search/find-first-occurrence/solutions/solution_naive.py
```

### Sample Output

```text
=== REFERENCE SOLUTIONS ===
Solution        | Case            | Status     | Time (s)
------------------------------------------------------------
LinearScanFinder | Example         | PASS       | 0.000022
BinarySearchFinder | Example         | PASS       | 0.000009
LinearScanFinder | Sample 1        | PASS       | 0.000021
BinarySearchFinder | Sample 1        | PASS       | 0.000006

=== CONTRIBUTED SOLUTIONS ===
No solutions found.
```

## Creating Solutions

### From Algorithm Template

1. **Rename the class** to reflect your strategy:

   ```python
   class MySearchStrategy(YourStrategyFinder):
       pass
   ```

2. **Implement required methods** shown in template stubs:
   - Main method (e.g., `find_first_occurrence(target)`)
   - Helper methods (e.g., `_helper()` for binary search)

3. **Use template guidance:**
   - Expected behavior section explains what to do
   - Implementation hints suggest strategies
   - Helper methods show algorithm decomposition

### From Data Structure Template

1. **Initialize internal state** (e.g., heap array, dual heaps)
2. **Implement core operations** with helper methods
3. **Follow template docstrings** for method contracts
4. **Test by running judge** to verify against test cases

### Example: Complete Quickselect Solution

```python
# solutions/contributed/my_quickselect.py
import random
from typing import List

class RandomizedQuickselect:
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def quickselect(self, k: int) -> int:
        return self._select(0, len(self.nums) - 1, k)
    
    def _select(self, left: int, right: int, k: int) -> int:
        if left == right:
            return self.nums[left]
        
        pivot_index = random.randint(left, right)
        pivot_index = self._partition(left, right, pivot_index)
        
        if k == pivot_index:
            return self.nums[k]
        elif k < pivot_index:
            return self._select(left, pivot_index - 1, k)
        else:
            return self._select(pivot_index + 1, right, k)
    
    def _partition(self, left: int, right: int, pivot_index: int) -> int:
        pivot_value = self.nums[pivot_index]
        self._swap(pivot_index, right)
        store_index = left
        
        for i in range(left, right):
            if self.nums[i] < pivot_value:
                self._swap(store_index, i)
                store_index += 1
        
        self._swap(right, store_index)
        return store_index
    
    def _swap(self, i: int, j: int) -> None:
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
```

Run `python algorithms/sorting/quickselect/judge.py` to test!

## Contributing New Problems

We welcome new algorithm and data structure challenges! Follow this guide to ensure your problem integrates properly with the Virtual Judge System.

### 1. Structure the Problem Directory

Create a new directory in the appropriate category (e.g., `algorithms/dp/climbing-stairs/`) with this exact structure:

```text
problem-name/
├── solutions/
│   ├── solution_naive.py     # Brute force / easy baseline
│   ├── solution_optimized.py # Optimal solution
│   └── solution_template.py  # Starter code for users
├── tests/
│   └── cases.py              # Test case definitions
├── judge.py                  # Problem-specific judge script
└── README.md                 # Problem statement
```

### 2. Define Test Cases

In `tests/cases.py`, define a `TestCase` dataclass and a list of cases.

```python
from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    nums: List[int]
    target: int
    expected: int
    name: str = "Test Case"
```

### 3. Create the Template

In `solutions/solution_template.py`, define the class structure. **Crucially**, solutions must be class-based with `__init__` for state setup and a method for the logic.

```python
# solutions/solution_template.py
from typing import List

class ClimbingStairsSolver:
    def __init__(self, n: int):
        self.n = n

    def solve(self) -> int:
        """
        Calculates the number of distinct ways to climb to the top.
        """
        pass
```

### 4. Implement Reference Solutions

Create `solutions/solution_naive.py` (e.g., recursion) and `solutions/solution_optimized.py` (e.g., DP) inheriting from or implementing the same interface as the template.

### 5. Configure the Judge

Copy `judge.py` from an existing problem and adapt it:

1. Update imports to point to your new `TestCase`.
2. Update the `run_test_case` function to instantiate your class and call the method.
3. Update `load_solutions` call if necessary (usually auto-dectected if following patterns).

### 6. Add Documentation

Create a `README.md` in the problem directory with:

- **Problem Statement**: Clear description.
- **Input/Output**: Data types and constraints.
- **Examples**: Walkthroughs of simple cases.

## Submitting Solutions

### Main Branch Policy

The `main` branch accepts only **curated reference solutions**:

- ✅ Allowed: `solution_naive.py`, `solution_optimized.py`, `__init__.py`
- ❌ Not allowed: `my_solution.py`, `solution_v1.py`, etc.

CI blocks PRs to `main` with non-conforming files via `tools/validate_main_branch.py`.

### Contributing Alternative Solutions

Use the `contributed` branch for personal/experimental implementations:

```bash
# Create or switch to contributed branch
git checkout -b contributed
git push -u origin contributed

# Add your solution
mkdir -p algorithms/search/find-first-occurrence/solutions/contributed
cp my_solution.py algorithms/search/find-first-occurrence/solutions/contributed/

# Commit and open PR targeting contributed branch
git add .
git commit -m "Add my quicksearch implementation"
git push origin contributed
# Open PR: contributed ← your-feature-branch
```

## License

MIT
