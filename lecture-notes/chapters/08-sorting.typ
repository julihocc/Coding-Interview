= Sorting

Sorting is an operation that arranges a list of elements into ascending or descending sequence. It is often a necessary precursor to other algorithms, particularly searching.

General-purpose comparison sorts are bounded by an absolute theoretical limit of $O(n log n)$ time complexity in the worst/average case.

== Key Terminology
- *In-place:* Sorts the array modifying the original input without allocating an entirely new array (uses $O(1)$ or $O(log n)$ extra memory space).
- *Stable Sort:* If two elements have equal keys, a stable sort will always maintain their relative original order from the unsorted array.

== Fundamental $O(n log n)$ Sorts

=== Merge Sort
Merge sort employs the classic *Divide and Conquer* paradigm.
1. *Divide:* Recursively split the array exactly in half until all sub-arrays contain only one element.
2. *Conquer/Merge:* Iteratively merge the smaller sorted sub-arrays into larger sorted arrays, ensuring the result is always sorted.
- *Time Complexity:* $O(n log n)$ guaranteed in all cases.
- *Space Complexity:* $O(n)$ space. It requires temporary arrays during the merge step, so it is *not in-place*. However, standard Merge Sort is a *stable* sort.

=== Quicksort
Quicksort also uses divide and conquer, but does all the heavy lifting during the divide step (partitioning) rather than the merge step.
1. Choose a "pivot" element from the array.
2. *Partition:* Rearrange the array so that all elements smaller than the pivot come before it, and all elements larger come after it. The pivot is now in its final, permanently sorted position.
3. Recursively apply the above steps to both resulting sub-arrays.
- *Time Complexity:* $O(n log n)$ on average. In the absolute worst-case, it devolves to $O(n^2)$. Randomizing the pivot selection practically eliminates this risk.
- *Space Complexity:* $O(log n)$ on the recursion call stack. It is an *in-place* sort, but it is *not stable*.

== Quickselect
Not technically a full sorting algorithm, but it uses Quicksort's partitioning logic to find the $k$-th smallest (or largest) element in an unsorted array.
- Instead of recursively sorting both halves, `quickselect` only recurses on the half that *must* contain the $k$-th element.
- *Time Complexity:* $O(n)$ average time, outperforming the $O(n log n)$ required to fully sort the array. Worst case is $O(n^2)$.
