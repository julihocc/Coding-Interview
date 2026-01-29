# Merge Sort - Substring Comparison

## Problem Statement

Given a list of strings, sort them based on their first 3 characters only. If a string has fewer than 3 characters, use the entire string for comparison.

This is a variation of the classic merge sort algorithm where the comparison operation is customized to only consider a substring (the first 3 characters) rather than the entire string.

## Algorithms

- **Naive:** Use Python's built-in `sorted()` function with a custom key function that extracts the first 3 characters. Complexity: $O(n \log n)$ time, $O(n)$ extra space.
- **Merge Sort (recursive):** Classic divide-and-conquer merge sort with modified comparison logic in the merge operation. Guaranteed $O(n \log n)$ time complexity with $O(n)$ extra space.
- **Merge Sort (iterative):** Bottom-up merge sort with custom substring comparison. Same $O(n \log n)$ time complexity with $O(n)$ extra space.

## Function Signature

```python
from typing import List

def merge_sort_substring(strings: List[str]) -> List[str]:
    ...
```

## Examples

```python
# Example 1
Input: ["apple", "application", "app", "banana", "band"]
Output: ["app", "apple", "application", "banana", "band"]
# "app", "apple", "application" all start with "app"
# "banana" and "band" both start with "ban"

# Example 2
Input: ["zebra", "zero", "alpha", "alphabet"]
Output: ["alpha", "alphabet", "zebra", "zero"]
# "alpha" and "alphabet" both start with "alp"
# "zebra" starts with "zeb", "zero" starts with "zer"
```

## Notes

- The comparison should only consider the first 3 characters
- Strings with fewer than 3 characters should use their full length
- The sort should be stable (preserve relative order of equal elements)
- Original strings remain unchanged in the output
