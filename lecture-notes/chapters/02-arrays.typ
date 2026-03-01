== Arrays

Arrays are the most fundamental data structure. They represent a collection of elements identified by an index or key, stored in *contiguous memory locations*.

=== Memory Contiguity
Because array elements are stored contiguously in memory, arrays provide $O(1)$ time complexity for random access. If you know the index of an element, the computer can instantly calculate its exact memory address.

However, this contiguity comes with a trade-off:
- *Insertion and Deletion* (except at the end of the array) take $O(n)$ time because all subsequent elements must be shifted over.
- *Fixed Size:* In many lower-level languages, traditional arrays have a fixed size. Dynamic arrays (like Python's `list`) handle resizing under the hood.

=== Common Patterns

==== Two Pointers
The two-pointer technique is incredibly versatile, especially for sorted arrays or when you need to find a pair of elements.
- *Opposite Ends:* Start one pointer at the beginning and one at the end, moving them inwards based on a condition (e.g., reversing an array, checking for a palindrome).
- *Same Direction:* Use a "fast" and a "slow" pointer to remove duplicates in place or to find subarrays.

==== Sliding Window
A specific variation of two pointers used to solve problems looking for a contiguous subarray that meets certain criteria (e.g., "longest substring with $K$ distinct characters").
- The "window" expands by moving the right pointer and contracts by moving the left pointer, keeping track of the current state inside the window.

==== Prefix Sums
Prefix sums involve creating a new array where the element at index $i$ stores the sum of all elements from index $0$ to $i$ in the original array.
- This allows you to answer range sum queries in $O(1)$ time after an $O(n)$ pre-computation step.
