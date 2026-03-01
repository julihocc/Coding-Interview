Welcome to the *Coding Interview Practice Lecture Notes*. This book is a comprehensive theoretical companion to the problem repository. While the repository provides hands-on practice via a *Virtual Judge System*, these notes supply the underlying mathematical and algorithmic intuition you need to understand *why* an optimal solution works — not just *that* it does.

== The Problem Repository

The repository is organized around a set of programming challenges grouped by data structure and algorithmic concept. Each problem module follows a consistent structure:

- *`README.md`:* A narrative description of the problem, the input/output format, and the expected constraints.
- *`ALGORITHM_ANALYSIS.md`:* A detailed breakdown of both the naive and optimal approaches, their complexities, and the key insight required.
- *`solution_template.py`:* A skeleton class with the method signature pre-filled so you can focus purely on the logic.
- *`judge.py`:* The script that runs your solution against a battery of test cases.
- *`tests/cases.py`:* The test case definitions, covering edge cases and large inputs.

== The Virtual Judge System

Our repository uses a *stateful, class-based Virtual Judge* to test your code. This mirrors the object-oriented design patterns commonly seen in real-world backend engineering and in major interview platforms.

=== Stateful Initialization

Instead of writing a standalone function, your solution is a *class*. The `__init__` method is called once with the full input (e.g., an array, a graph, a set of constraints). You store any pre-computed data or data structures here that your solver methods will later use.

```python
class Solution:
    def __init__(self, nums):
        # Pre-process the input once
        self.nums = nums
        self.prefix = self._build_prefix(nums)

    def query(self, left, right):
        # Answer queries in O(1) using stored state
        return self.prefix[right + 1] - self.prefix[left]
```

This pattern rewards thinking ahead: constructing the right data structure in `__init__` can reduce a $O(n)$ per-query problem to $O(1)$.

=== Reflection and Benchmarking

The Judge discovers your class via Python's reflection system. It instantiates your class, calls the required methods with test inputs, and compares your output against a proven baseline. It also times each call to ensure your solution meets a practical performance budget.

This means two things matter equally:
1. *Correctness:* Your output must match the expected answer exactly.
2. *Efficiency:* A correct but $O(n^2)$ solution will be flagged on large inputs.

=== The Naive-First Mindset

Every `ALGORITHM_ANALYSIS.md` begins with a naive solution and then systematically improves it. You are strongly encouraged to adopt this same workflow:

1. Write the clearest, most readable brute-force solution first.
2. Reason about its complexity.
3. Identify the bottleneck (the innermost loop, the repeated work).
4. Apply the appropriate pattern (e.g., sliding window, binary search) to eliminate that bottleneck.

== How to Use This Book

This book mirrors the repository's structure. Each chapter introduces a data structure or algorithm family, explains the core operations and their complexities, and then presents the canonical *patterns* that appear repeatedly in interview problems.

Read each chapter *before* attempting the corresponding problems. Revisit the relevant sections whenever a problem feels unfamiliar. The goal is not memorization — it is developing a reliable intuition for which tool to reach for given a problem's constraints.

== Understanding Complexity Analysis

Before studying any specific data structure, you must internalize the two dimensions on which every solution is evaluated:

- *Time Complexity:* How does the running time grow as the input size $n$ increases?
- *Space Complexity:* How much additional memory does the algorithm consume beyond the input itself?

=== Big O Notation

*Big O* describes the *asymptotic upper bound* of a function's growth rate. Concretely, we say an algorithm is $O(f(n))$ if its running time is bounded above by $c dot f(n)$ for some constant $c$ and all sufficiently large $n$.

This means:
- *Constants are dropped:* $5n$ and $10n$ are both $O(n)$.
- *Lower-order terms are dropped:* $n^2 + n$ is $O(n^2)$.
- We care only about what happens as $n$ grows large, not for tiny inputs.

=== A Practical Complexity Reference

The table below summarizes the most common complexity classes, ranked from fastest to slowest:

#table(
  columns: (auto, auto, auto),
  align: (center, left, left),
  table.header([*Complexity*], [*Name*], [*Example*]),
  [$O(1)$], [Constant], [Array index lookup, hash map get],
  [$O(log n)$], [Logarithmic], [Binary search, balanced BST lookup],
  [$O(n)$], [Linear], [Single array scan, linked list traversal],
  [$O(n log n)$], [Log-Linear], [Merge Sort, Heap Sort],
  [$O(n^2)$], [Quadratic], [Bubble Sort, comparing all pairs],
  [$O(2^n)$], [Exponential], [Enumerating all subsets],
  [$O(n!)$], [Factorial], [Enumerating all permutations],
)

=== Space Complexity

Space complexity accounts for any *extra* memory your algorithm allocates beyond the input:

- *$O(1)$ space:* The algorithm uses a fixed number of variables regardless of input size. This is called *in-place*.
- *$O(n)$ space:* The algorithm stores a copy of the data or a recursive call stack proportional to the input.
- *$O(log n)$ space:* Typical of recursive algorithms that divide the input in half (the call stack depth is $log n$).

Always report space complexity excluding the input itself, unless the problem explicitly asks you to modify the input in-place.

=== How to Estimate Complexity Quickly

Before writing a single line of code, you can often estimate a target complexity from the problem's constraints ($n$ is the input size):

#table(
  columns: (auto, auto),
  align: (center, left),
  table.header([*Constraint*], [*Expected Complexity*]),
  [$n <= 20$], [$O(2^n)$ or $O(n!)$],
  [$n <= 500$], [$O(n^2)$ or $O(n^2 log n)$],
  [$n <= 10^4$], [$O(n^2)$ at most],
  [$n <= 10^5$], [$O(n log n)$ or $O(n)$],
  [$n <= 10^6$], [$O(n)$ or $O(n log n)$ very tight],
  [$n <= 10^9$], [$O(log n)$ or $O(1)$],
)

Using this table you can immediately rule out algorithms that are too slow and narrow your search to the right class of solution before you begin.

== A General Problem-Solving Framework

Regardless of the specific problem, the following process gives you a structured way to approach any coding challenge:

1. *Understand the problem completely.* Re-read the problem statement. Write out a concrete example by hand. Identify edge cases (empty input, single element, all duplicates, maximum constraints).

2. *State the naive approach.* What is the most obvious brute-force solution? What is its complexity? Why is it too slow?

3. *Identify the bottleneck.* Where is the unnecessary repeated work? Is there a nested loop scanning a structure that has already been seen? Is there a re-computation that could be cached?

4. *Apply a known pattern.* Which technique from your repertoire addresses this bottleneck? The following chapters each introduce one family of patterns:
  - *Sliding window / two pointers* → eliminate inner array scans
  - *Hash maps* → convert $O(n)$ lookups to $O(1)$
  - *Binary search* → eliminate half the search space per step
  - *Monotonic structures* → maintain order information incrementally
  - *Divide and conquer / recursion* → break the problem into independent sub-problems

5. *Write clean code.* Name variables clearly. Handle edge cases explicitly. Prefer clarity over cleverness.

6. *Test and analyze.* Verify on your hand-traced examples. Confirm the final time and space complexity.
