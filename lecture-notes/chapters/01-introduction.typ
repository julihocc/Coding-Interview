= Introduction

Welcome to the *Coding Interview Practice Lecture Notes*. This book is designed to serve as a comprehensive theoretical companion to our problem repository. While the repository provides hands-on practice via a *Virtual Judge System*, these notes provide the underlying mathematical and algorithmic intuition necessary to conquer the challenges.

== The Virtual Judge System
Our repository uses a sophisticated, class-based Virtual Judge approach to test your code:
- *Stateful Initialization:* Problems often require setting up internal state (e.g., maintaining a data structure or storing the input array) inside an `__init__` method.
- *Benchmarking and Testing:* The Virtual Judge discovers your solution via reflection, compares your output across numerous test cases against optimal baselines, and benchmarks your execution time.
- *Naive vs. Optimized:* The core philosophy of this guide is to understand *why* an optimized solution is necessary. Every problem provides a starting `solution_template.py`, and you are encouraged to first think of the naive approach before designing an optimal one.

== How to Use This Book
This book is intended to be read alongside solving the problems from the repository. Each chapter covers a core concept (like Arrays, Trees, or Binary Search) and introduces the common patterns and techniques you will need to implement an optimal solution.

== Understanding Complexity Analysis
When analyzing algorithms, especially in coding interviews, we evaluate them strictly on two primary metrics:
- *Time Complexity:* A measure of how the runtime of the algorithm grows as the size of the input $n$ increases.
- *Space Complexity:* A measure of how much extra memory the algorithm requires as the input $n$ increases.

We use *Big O Notation* to describe the upper asymptotic bound of this growth rate. It ignores constants and lower-order terms, focusing purely on the dominant factor as $n$ trends towards infinity.

=== Common Time Complexities

- $O(1)$ - *Constant:* The execution time is independent of the input size. For example, retrieving an element from an array by index, or looking up a key in a hash map.
- $O(log n)$ - *Logarithmic:* The problem space is continually halved at each step. Examples include binary search or traversing a balanced binary tree.
- $O(n)$ - *Linear:* You must visit every element in the input exactly once. Example: finding the maximum value in an unsorted array.
- $O(n log n)$ - *Log-Linear:* Typical time for optimal comparison-based sorting algorithms like Merge Sort and Quicksort.
- $O(n^2)$ - *Quadratic:* Usually involves nested loops over the input. Example: Bubble Sort, or comparing every pair of elements.
- $O(2^n)$ - *Exponential:* The algorithm explores every combination or subset. Example: naive recursive Fibonacci.

Always strive to understand the complexities of both your naive brute-force and your optimized solutions!
