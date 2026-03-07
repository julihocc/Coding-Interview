# Learning Guide: Problem Solving Roadmap

This guide provides a structured learning path through the repository's problems, organized to build understanding progressively from fundamental concepts to advanced techniques.

## 📚 How to Use This Guide

- **Follow the order**: Each section builds on concepts from previous sections
- **Complete all problems in a section** before moving to the next
- **Start with templates**: Use `solution_template.py` to understand the problem structure
- **Compare approaches**: Study both naive and optimized solutions to learn trade-offs
- **Run judges**: Verify your understanding by running tests frequently

---

## Phase 1: Data Structure Fundamentals (Week 1-2)

### 1.1 Linear Data Structures: Arrays

**Goal**: Master basic array manipulation and understand memory contiguity

- **Problem**: [left-rotation](data-structures/arrays/left-rotation/)
  - **Concepts**: Array indexing, modular arithmetic, in-place operations
  - **Why first**: Arrays are the foundation for all other structures
  - **Time to complete**: 1-2 hours

**Key Learning**: Understanding array mechanics is crucial for heaps, stacks, and queues.

---

### 1.2 FIFO Structures: Queues

**Goal**: Understand First-In-First-Out (FIFO) principle and its applications

#### Start Here

- **Problem**: [basic-queue](data-structures/queues/basic-queue/)
  - **Concepts**: FIFO ordering, `collections.deque`, O(1) operations
  - **Implementation focus**: Compare list vs. deque performance
  - **Time to complete**: 2-3 hours

#### Then Apply

- **Problem**: [printer-queue](data-structures/queues/printer-queue/)
  - **Concepts**: Real-world queue simulation, job management
  - **Why second**: Applies basic queue concepts to practical scenarios
  - **Time to complete**: 1-2 hours

**Key Learning**: Queues are essential for BFS, task scheduling, and real-time systems.

---

### 1.3 LIFO Structures: Stacks

**Goal**: Master Last-In-First-Out (LIFO) principle and stack applications

#### Foundation

- **Problem**: [reverse-string](data-structures/stacks/reverse-string/)
  - **Concepts**: Basic stack operations (push, pop, peek)
  - **Why first**: Simplest stack application to understand LIFO
  - **Time to complete**: 1 hour

#### Pattern Matching

- **Problem**: [balanced-brackets](data-structures/stacks/balanced-brackets/)
  - **Concepts**: Stack for validation, matching pairs
  - **Time to complete**: 2 hours

#### Expression Evaluation

- **Problem**: [evaluate-postfix](data-structures/stacks/evaluate-postfix/)
  - **Concepts**: Stack-based calculation, postfix notation
  - **Time to complete**: 2 hours

#### Optimization Techniques

- **Problem**: [min-stack](data-structures/stacks/min-stack/)
  - **Concepts**: Auxiliary stack, O(1) min tracking
  - **Time to complete**: 2-3 hours

- **Problem**: [max-stack](data-structures/stacks/max-stack/)
  - **Concepts**: Similar to min-stack, understand the pattern
  - **Time to complete**: 1-2 hours

#### Advanced Stack Patterns

- **Problem**: [previous-smaller-element](data-structures/stacks/previous-smaller-element/)
  - **Concepts**: Monotonic stack, O(n) solutions
  - **Time to complete**: 3-4 hours

- **Problem**: [daily-temperatures](data-structures/stacks/daily-temperatures/)
  - **Concepts**: Monotonic stack for future values
  - **Why last**: Most complex stack problem, requires full understanding
  - **Time to complete**: 3-4 hours

**Key Learning**: Stacks enable elegant solutions for parsing, expression evaluation, and finding ranges.

---

### 1.4 Pointer-Based Structures: Linked Lists

**Goal**: Understand nodes and pointer manipulation in singly and doubly linked lists

#### Foundation

- **Problem**: [linked-list-insert-after-head](data-structures/linked-lists/linked-list-insert-after-head/)
  - **Concepts**: Singly linked list, O(1) pointer manipulation, `push` vs `insert_after`
  - **Why first**: Simplest linked-list operation — only two pointer reassignments
  - **Time to complete**: 1-2 hours

#### Debugging Practice

- **Problem**: [linked-list-size-tracker](data-structures/linked-lists/linked-list-size-tracker/)
  - **Concepts**: Counter invariants, debugging logic errors vs syntax errors
  - **Why second**: Reinforces insert/delete mechanics while practicing bug identification
  - **Time to complete**: 1-2 hours

#### Bidirectional Traversal

- **Problem**: [doubly-linked-list-backward-display](data-structures/linked-lists/doubly-linked-list-backward-display/)
  - **Concepts**: `prev` pointers, tail pointer benefits, O(1) vs O(2n) traversal
  - **Why last**: Introduces the `prev` pointer and shows the value of maintaining a `tail`
  - **Time to complete**: 2-3 hours

**Key Learning**: Linked lists teach pointer discipline and O(1) insertions/deletions that arrays cannot match.

---

## Phase 2: Hierarchical Structures: Trees (Week 3)

### 2.1 Tree Fundamentals and DFS

**Goal**: Understand basic tree structures and Depth-First Search traversal

#### Binary Trees

- **Problem**: [binary-tree-traversal](data-structures/trees/binary-tree-traversal/)
  - **Concepts**: In-order traversal, recursive tree navigation
  - **Why first**: Fundamental tree traversal pattern
  - **Time to complete**: 2-3 hours

- **Problem**: [binary-search-tree](data-structures/trees/binary-search-tree/)
  - **Concepts**: BST properties, insertion, searching, deletion
  - **Time to complete**: 3-4 hours

- **Problem**: [check-bst-balance](data-structures/trees/check-bst-balance/)
  - **Concepts**: Balance checking, subtree heights
  - **Why advanced**: Tests recursive calculation of heights and depth bounds
  - **Time to complete**: 1-2 hours

- **Problem**: [max-height-diff-bst](data-structures/trees/max-height-diff-bst/)
  - **Concepts**: Subtree height comparisons, bottom-up tree traversal
  - **Time to complete**: 1-2 hours

- **Problem**: [kth-smallest-bst](data-structures/trees/kth-smallest-bst/)
  - **Concepts**: In-order traversal, subtree counting
  - **Time to complete**: 1-2 hours

#### N-ary Trees & DFS

- **Problem**: [planet-continents-dfs](data-structures/trees/planet-continents-dfs/)
  - **Concepts**: Depth-First Search on non-binary trees
  - **Time to complete**: 2-3 hours

---

### 2.2 Breadth-First Search (BFS)

**Goal**: Master level-by-level traversal using queues

#### Core Pattern

- **Problem**: [breadth-first-search-tree](data-structures/trees/breadth-first-search-tree/)
  - **Concepts**: Queue-based BFS traversal
  - **Why first**: Canonical BFS introduction
  - **Time to complete**: 2 hours

#### Applied BFS

- **Problem**: [rainforest-bfs](data-structures/trees/rainforest-bfs/)
  - **Concepts**: BFS applied to real-world domain (forests)
  - **Time to complete**: 1-2 hours
  
- **Problem**: [planet-network-bfs](data-structures/trees/planet-network-bfs/)
  - **Concepts**: BFS starting from arbitrary nodes
  - **Time to complete**: 1-2 hours

#### Advanced BFS

- **Problem**: [company-hierarchy-bfs](data-structures/trees/company-hierarchy-bfs/)
  - **Concepts**: Bug fixing BFS traversal on N-ary trees
  - **Time to complete**: 2 hours

- **Problem**: [family-tree-level-bfs](data-structures/trees/family-tree-level-bfs/)
  - **Concepts**: Tracking distances/levels from root using BFS
  - **Time to complete**: 2-3 hours

- **Problem**: [network-bfs](data-structures/trees/network-bfs/)
  - **Concepts**: BFS on graph-like network structures
  - **Time to complete**: 2 hours

**Key Learning**: Trees introduce non-linear relationships, where DFS explores depth and BFS uses queues to explore breadth.

---

## Phase 3: Hierarchical Structures: Heaps (Week 4)

### 2.1 Basic Heap Operations

**Goal**: Understand heap property and tree-based operations

- **Problem**: [min-heap](data-structures/heaps/min-heap/)
  - **Concepts**: Heap property, bubble-up/down, 1-indexed arrays
  - **Why first**: Establishes heap fundamentals
  - **Time to complete**: 3-4 hours

- **Problem**: [max-heap](data-structures/heaps/max-heap/)
  - **Concepts**: Inverse of min-heap, solidify understanding
  - **Time to complete**: 2-3 hours

**Key Learning**: Heaps provide O(log n) insert/delete and O(1) min/max access.

---

### 2.2 Advanced Heap Applications

- **Problem**: [top-k-heap](data-structures/heaps/top-k-heap/)
  - **Concepts**: Fixed-size heap, k-largest/smallest elements
  - **Time to complete**: 2-3 hours

- **Problem**: [median-heap](data-structures/heaps/median-heap/)
  - **Concepts**: Dual heap structure, rebalancing
  - **Why last**: Most complex - requires mastery of both heap types
  - **Time to complete**: 4-5 hours

- **Problem**: [median-finder](data-structures/heaps/median-finder/)
  - **Concepts**: Dual heap structure, streaming algorithms, real-world application
  - **Time to complete**: 3-4 hours

**Key Learning**: Heaps enable efficient priority queues, streaming algorithms, and order statistics.

---

## Phase 4: Searching Algorithms (Week 5-6)

### 3.1 Binary Search Fundamentals

**Goal**: Master the binary search template and invariants

#### Core Pattern

- **Problem**: [find-first-occurrence](algorithms/search/find-first-occurrence/)
  - **Concepts**: Binary search template, loop invariants
  - **Why first**: Canonical binary search introduction
  - **Time to complete**: 3-4 hours

#### Variations

- **Problem**: [target-index-search](algorithms/search/target-index-search/)
  - **Concepts**: Standard binary search
  - **Time to complete**: 2 hours

- **Problem**: [search-insert-position](algorithms/search/search-insert-position/)
  - **Concepts**: Finding insertion point
  - **Time to complete**: 2 hours

- **Problem**: [search-insert-position-left](algorithms/search/search-insert-position-left/)
  - **Concepts**: Left boundary search
  - **Time to complete**: 2 hours

---

### 3.2 Range Queries

**Goal**: Find ranges and boundaries efficiently

- **Problem**: [locate-first-last-position](algorithms/search/locate-first-last-position/)
  - **Concepts**: Two binary searches for range
  - **Time to complete**: 3 hours

- **Problem**: [locate-first-last-float](algorithms/search/locate-first-last-float/)
  - **Concepts**: Binary search with floating-point numbers
  - **Time to complete**: 2-3 hours

- **Problem**: [find-crossover-indices](algorithms/search/find-crossover-indices/)
  - **Concepts**: Finding transition points
  - **Time to complete**: 3 hours

---

### 3.3 Mathematical Applications

- **Problem**: [integer-cube-root](algorithms/search/integer-cube-root/)
  - **Concepts**: Binary search on answer space
  - **Time to complete**: 2-3 hours

---

### 3.4 Modified Binary Search (Advanced)

- **Problem**: [search-rotated-sorted-array](algorithms/search/search-rotated-sorted-array/)
  - **Concepts**: Binary search in rotated arrays
  - **Why advanced**: Requires identifying sorted halves
  - **Time to complete**: 4-5 hours

- **Problem**: [search-rotated-sorted-array-descending](algorithms/search/search-rotated-sorted-array-descending/)
  - **Concepts**: Descending order variation
  - **Time to complete**: 3-4 hours

**Key Learning**: Binary search reduces O(n) problems to O(log n) through divide-and-conquer.

---

## Phase 5: Sorting and Selection (Week 7-8)

### 4.1 Divide-and-Conquer Sorting

**Goal**: Master recursive sorting algorithms

#### Merge Sort

- **Problem**: [merge-sort](algorithms/sorting/merge-sort/)
  - **Concepts**: Divide-and-conquer, stable sorting, O(n log n)
  - **Why first**: Simpler than quicksort, guaranteed performance
  - **Time to complete**: 4-5 hours

- **Problem**: [merge-sort-substring](algorithms/sorting/merge-sort-substring/)
  - **Concepts**: Merge sort on array segments
  - **Time to complete**: 3 hours

#### Multiway Operations

- **Problem**: [multiway-merge](algorithms/sorting/multiway-merge/)
  - **Concepts**: Merging k sorted arrays, heap-based merging
  - **Time to complete**: 4 hours

---

### 4.2 Quicksort Family

- **Problem**: [quicksort](algorithms/sorting/quicksort/)
  - **Concepts**: In-place sorting, partitioning, pivot selection
  - **Time to complete**: 4-5 hours

- **Problem**: [quicksort-descending](algorithms/sorting/quicksort-descending/)
  - **Concepts**: Descending order variation
  - **Time to complete**: 2-3 hours

---

### 4.3 Selection Algorithms

- **Problem**: [quickselect](algorithms/sorting/quickselect/)
  - **Concepts**: Finding kth element, O(n) average time
  - **Why after quicksort**: Uses same partitioning logic
  - **Time to complete**: 3-4 hours

---

### 4.4 Advanced Applications

- **Problem**: [count-anti-inversions](algorithms/sorting/count-anti-inversions/)
  - **Concepts**: Merge sort with counting, measuring disorder
  - **Why last**: Combines sorting with problem-solving
  - **Time to complete**: 5-6 hours

**Key Learning**: Sorting algorithms are the foundation for many advanced techniques.

---

## 📊 Estimated Timeline

| Phase | Focus | Duration | Problems |
|-------|-------|----------|----------|
| 1 | Linear Data Structures | 2 weeks | 14 problems |
| 2 | Trees | 1 week | 12 problems |
| 3 | Heaps | 1 week | 5 problems |
| 4 | Binary Search | 2 weeks | 10 problems |
| 5 | Sorting & Selection | 2 weeks | 7 problems |
| **Total** | **Complete Roadmap** | **8 weeks** | **48 problems** |

---

## 🎯 Learning Milestones

### Week 2 Checkpoint: Linear Structures

- ✅ Can implement queue and stack from scratch
- ✅ Understand when to use FIFO vs LIFO
- ✅ Recognize stack patterns in problems

### Week 4 Checkpoint: Heaps

- ✅ Can maintain heap property through operations
- ✅ Understand heap vs. sorting trade-offs
- ✅ Can solve streaming/online problems

### Week 6 Checkpoint: Binary Search

- ✅ Can write bug-free binary search
- ✅ Recognize when binary search applies
- ✅ Can handle edge cases and boundaries

### Week 8 Checkpoint: Sorting

- ✅ Understand time/space trade-offs in sorting
- ✅ Can implement partition-based algorithms
- ✅ Recognize when O(n log n) is optimal

---

## 💡 Study Tips

### For Each Problem

1. **Read thoroughly**: Understand the problem statement and examples
2. **Attempt template first**: Try implementing before looking at solutions
3. **Study naive solution**: Understand the brute-force approach
4. **Analyze optimized solution**: Learn the efficient technique
5. **Compare complexities**: Understand why optimization matters
6. **Run judges**: Verify correctness and see performance differences

### When Stuck

1. **Review ALGORITHM_ANALYSIS.md**: Understand the approach
2. **Draw examples**: Visualize small test cases
3. **Check edge cases**: Empty inputs, single elements, duplicates
4. **Use debugger**: Step through solution code
5. **Compare with template**: Ensure you understand the structure

### Active Learning

- **Implement from scratch**: Don't just read solutions
- **Explain to others**: Teaching solidifies understanding
- **Solve variations**: Modify problems to test understanding
- **Time yourself**: Track improvement over time
- **Review regularly**: Revisit completed problems weekly

---

## 🔗 Concept Dependencies

```
Arrays → All other structures
Arrays → Binary Search

Queues → BFS (future topic)
Stacks → DFS (future topic)
Stacks → Expression Parsing

Linked Lists → Trees
Linked Lists → Graph adjacency lists
insert-after-head → size-tracker (same insert/delete mechanics)
size-tracker → doubly-linked-list-backward-display (adds prev pointers)

Heaps → Priority Queues
Heaps → Multiway Merge

Binary Search → Search in Sorted Arrays
Binary Search → Mathematical Problems

Merge Sort → Count Inversions
Merge Sort → Multiway Merge
Quicksort → Quickselect
```

---

## 📈 Progress Tracking

Track your progress through the roadmap:

- [ ] **Phase 1 Complete**: Linear Data Structures (14/14)
- [ ] **Phase 2 Complete**: Trees (12/12)
- [ ] **Phase 3 Complete**: Heaps (5/5)
- [ ] **Phase 4 Complete**: Binary Search (10/10)
- [ ] **Phase 5 Complete**: Sorting & Selection (7/7)

**Total Progress**: ___/48 problems completed

---

## 🎓 Next Steps After Completion

Once you've completed this roadmap, you'll be ready for:

1. **Graph Algorithms**: Advanced BFS, DFS, Dijkstra's (use tree/queue/stack knowledge)
2. **Dynamic Programming**: Build on divide-and-conquer understanding
3. **Advanced Trees**: Use heap concepts for segment trees, tries
4. **String Algorithms**: Apply binary search to pattern matching
5. **System Design**: Use queue/stack concepts for real systems

---

## 📝 Additional Resources

- **ALGORITHM_ANALYSIS.md** in each problem: Detailed complexity analysis
- **README.md** in each problem: Problem statement and examples
- **solution_template.py**: Guided implementation hints
- **utils/judge_utils.py**: Understanding the testing framework

---

## 🤝 Community Learning

Share your progress and learn from others:

1. Create solutions in `solutions/contributed/` folder
2. Compare different approaches with classmates
3. Discuss trade-offs and optimizations
4. Review each other's code for best practices

---

## ⚠️ Important Notes

- **Don't skip fundamentals**: Later problems assume earlier knowledge
- **Quality over speed**: Deep understanding beats fast completion
- **Practice regularly**: Consistency is more important than long sessions
- **Test thoroughly**: Use the judge system to verify correctness
- **Learn from failures**: Failed tests are learning opportunities

---

Good luck on your learning journey! Remember: the goal isn't just to solve problems, but to develop a deep understanding of fundamental algorithms and data structures that will serve you throughout your career.

**Happy Coding!** 🚀
