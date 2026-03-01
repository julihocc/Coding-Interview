= Heaps

A Heap (specifically a Binary Heap) is a complete binary tree that satisfies the *Heap Property*. Because it is "complete" (all levels are filled except possibly the last, which is filled from left to right), it can be efficiently represented as an array rather than using nodes and pointers.

== The Heap Property

Depending on the type of heap, the relationship between a parent node and its children varies:

- *Min-Heap:* The value of every parent node is less than or equal to the values of its children. The root node is always the absolute minimum element in the entire heap.
- *Max-Heap:* The value of every parent node is greater than or equal to the values of its children. The root node is always the absolute maximum element in the entire heap.

== Array Representation

In a $0$-indexed array `H`:
- The left child of a node at index `i` is at `2i + 1`.
- The right child of a node at index `i` is at `2i + 2`.
- The parent of a node at index `i` is at `(i - 1) // 2`.

== Time Complexity

Heaps are incredibly efficient at doing one specific task: maintaining access to the minimum or maximum element in a continually changing underlying dataset.

- *Find Min/Max (`peek`):* $O(1)$ time, as it is always the root (index $0$).
- *Insert (`push`):* Adds the element to the very end of the array, then "bubbles up" (swapping with its parent) until the heap property is restored. Takes $O(log n)$ time.
- *Extract Min/Max (`pop`):* Removes the root, replaces it with the very last element in the array, then "bubbles down" (swapping with the smaller/larger child) to restore the heap property. Takes $O(log n)$ time.
- *Heapify:* Building a heap from an unsorted array takes $O(n)$ time.

== Common Patterns

Heaps are used primarily to implement Priority Queues.
- *Top-K Problems:* Finding the $k$-largest elements. Instead of sorting the entire array ($O(n log n)$), push the elements into a Min-Heap of size $K$. If the heap grows larger than $K$, pop the minimum. At the end, the heap contains the $k$-largest elements in $O(n log k)$ time.
- *Streaming Algorithms:* Finding the median of a constantly growing stream of numbers using a Max-Heap for the smaller half and a Min-Heap for the larger half.
