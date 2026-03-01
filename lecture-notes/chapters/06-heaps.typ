== Heaps

A Heap (specifically a Binary Heap) is a complete binary tree that satisfies the *Heap Property*. Because it is "complete", it can be efficiently represented as an array rather than using nodes and pointers.

=== The Heap Property

- *Min-Heap:* The value of every parent node is less than or equal to the values of its children. The root is always the minimum element.
- *Max-Heap:* The value of every parent node is greater than or equal to the values of its children. The root is always the maximum element.

=== Array Representation

In a $0$-indexed array `H`:
- The left child of a node at index `i` is at `2i + 1`.
- The right child of a node at index `i` is at `2i + 2`.
- The parent of a node at index `i` is at `(i - 1) // 2`.

=== Time Complexity

- *Find Min/Max (`peek`):* $O(1)$ time, as it is always the root (index $0$).
- *Insert (`push`):* Adds the element to the end, then "bubbles up" until the heap property is restored. Takes $O(log n)$ time.
- *Extract Min/Max (`pop`):* Removes the root, replaces it with the last element, then "bubbles down". Takes $O(log n)$ time.
- *Heapify:* Building a heap from an unsorted array takes $O(n)$ time.

=== Common Patterns

Heaps are used primarily to implement Priority Queues.
- *Top-K Problems:* Instead of sorting the entire array ($O(n log n)$), maintain a Min-Heap of size $K$. At the end, the heap contains the $k$-largest elements in $O(n log k)$ time.
- *Streaming Algorithms:* Finding the median of a constantly growing stream using a Max-Heap for the smaller half and a Min-Heap for the larger half.
