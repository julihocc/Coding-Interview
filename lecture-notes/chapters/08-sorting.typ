== Sorting

Sorting arranges a list of elements into ascending or descending sequence. General-purpose comparison sorts are bounded by a theoretical limit of $O(n log n)$ time complexity.

=== Key Terminology
- *In-place:* Sorts the array without allocating an entirely new array (uses $O(1)$ or $O(log n)$ extra space).
- *Stable Sort:* If two elements have equal keys, a stable sort maintains their relative original order.

=== Merge Sort
Merge sort employs the classic *Divide and Conquer* paradigm.
1. *Divide:* Recursively split the array in half until all sub-arrays contain one element.
2. *Conquer/Merge:* Iteratively merge the smaller sorted sub-arrays into larger sorted arrays.
- *Time Complexity:* $O(n log n)$ guaranteed in all cases.
- *Space Complexity:* $O(n)$ — not in-place. However, it is a *stable* sort.

=== Quicksort
Quicksort does all the work in the divide step (partitioning) rather than the merge step.
1. Choose a "pivot" element.
2. *Partition:* Rearrange so all elements smaller than the pivot come before it, larger after it. The pivot is now in its final sorted position.
3. Recursively apply to both sub-arrays.
- *Time Complexity:* $O(n log n)$ on average. Worst-case is $O(n^2)$ (mitigated by random pivot selection).
- *Space Complexity:* $O(log n)$ on the call stack. It is *in-place* but *not stable*.

=== Quickselect
Uses Quicksort's partitioning logic to find the $k$-th smallest (or largest) element without fully sorting the array.
- Only recurses on the half that must contain the $k$-th element.
- *Time Complexity:* $O(n)$ average, $O(n^2)$ worst case.
