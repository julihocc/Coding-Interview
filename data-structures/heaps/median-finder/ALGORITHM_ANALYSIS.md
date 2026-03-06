# Heap-based Median Finder - Algorithm Analysis

## Time Complexity

- **`addNum(num)`:** O(log n)
  - When adding a new number, we perform `heappush` and sometimes `heappop` operations on the heaps. Because the heaps contain at most `n` elements, adjusting the heap takes logarithmic time.
- **`findMedian()`:** O(1)
  - We simply access the root of the heaps (`small[0]` and/or `large[0]`), which takes constant time.

## Space Complexity

- **Overall:** O(n)
  - We store all the incoming `n` numbers in the two heaps. Thus, the space complexity is proportional to the number of elements in the data stream.
