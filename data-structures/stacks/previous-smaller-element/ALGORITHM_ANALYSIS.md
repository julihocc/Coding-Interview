# Algorithm Analysis: Previous Smaller Element

## Problem Overview

Given an array of integers, find the most recent previous element that is strictly smaller than each element. This is a classic application of **monotonic stacks** for efficient sequential data processing.

## Approach 1: Naive Solution (Brute Force)

### Algorithm

For each element at index `i`, scan backwards through all previous elements to find the first (most recent) element that is smaller.

### Pseudocode

```
function findPreviousSmallerNaive(numbers):
    result = []
    
    for i from 0 to length(numbers) - 1:
        found = -1
        for j from i - 1 down to 0:
            if numbers[j] < numbers[i]:
                found = numbers[j]
                break
        result.append(found)
    
    return result
```

### Complexity Analysis

**Time Complexity:** $O(n^2)$
- Outer loop: $n$ iterations
- Inner loop: worst case $i$ iterations for each $i$
- Total: $\sum_{i=0}^{n-1} i = \frac{n(n-1)}{2} = O(n^2)$

**Space Complexity:** $O(n)$
- Result array: $O(n)$
- No additional data structures

### Why It's Inefficient

For each element, we re-examine elements we've already seen. This leads to redundant comparisons, especially in arrays with many elements. For example:
- Array: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` (ascending)
- For element at index 9, we compare with all 9 previous elements
- Total comparisons: $0 + 1 + 2 + ... + 9 = 45$

## Approach 2: Optimized Solution (Monotonic Stack)

### Key Insight

**Observation:** If we've seen elements `a` and `b` where `a` appears before `b` and `a ≥ b`, then `a` can NEVER be the "previous smaller element" for any future element.

**Why?** For any future element `x`:
- If `x > b`, then `b` is closer and smaller than `a` (or equal)
- If `x ≤ b`, then `x ≤ b ≤ a`, so neither qualifies

This means we can **discard** larger elements as we progress, maintaining only potentially useful candidates in a stack.

### Algorithm

Use a **monotonic increasing stack** (elements in stack are in increasing order from bottom to top):

1. Initialize empty stack and result list
2. For each element in the array:
   - Pop all elements from stack that are ≥ current element (they're useless now)
   - The top of stack (if exists) is the previous smaller element
   - Push current element onto stack (potential candidate for future elements)

### Pseudocode

```
function findPreviousSmallerOptimized(numbers):
    result = []
    stack = []
    
    for num in numbers:
        // Remove elements that can't be previous smaller
        while stack is not empty AND stack.top() >= num:
            stack.pop()
        
        // Top of stack is the answer (or -1 if empty)
        if stack is empty:
            result.append(-1)
        else:
            result.append(stack.top())
        
        // Add current element for future elements
        stack.push(num)
    
    return result
```

### Step-by-Step Example

Input: `[4, 5, 2, 10, 8]`

| Step | Element | Stack Before | Action | Stack After | Result |
|------|---------|--------------|--------|-------------|--------|
| 1 | 4 | [] | Stack empty → -1, push 4 | [4] | [-1] |
| 2 | 5 | [4] | 4 < 5 → append 4, push 5 | [4, 5] | [-1, 4] |
| 3 | 2 | [4, 5] | Pop 5, pop 4 (both ≥ 2), -1, push 2 | [2] | [-1, 4, -1] |
| 4 | 10 | [2] | 2 < 10 → append 2, push 10 | [2, 10] | [-1, 4, -1, 2] |
| 5 | 8 | [2, 10] | Pop 10 (≥ 8), 2 < 8 → append 2, push 8 | [2, 8] | [-1, 4, -1, 2, 2] |

Output: `[-1, 4, -1, 2, 2]` ✓

### Complexity Analysis

**Time Complexity:** $O(n)$
- Each element is pushed exactly once: $n$ pushes
- Each element is popped at most once: $≤ n$ pops
- Total operations: $≤ 2n = O(n)$

**Space Complexity:** $O(n)$
- Stack: worst case $O(n)$ (e.g., ascending array `[1, 2, 3, 4, 5]`)
- Result array: $O(n)$
- Total: $O(n)$

### Why It Works: The Invariant

**Stack Invariant:** At any point, the stack contains elements in **strictly increasing order** from bottom to top, representing all potentially useful candidates for future elements.

**Proof of Correctness:**
1. When we see element `x`, all elements ≥ `x` are popped
2. After popping, the top of stack (if exists) is the largest element < `x` that appeared before `x`
3. This is exactly the "most recent previous smaller element"

## Comparison

| Aspect | Naive | Optimized |
|--------|-------|-----------|
| Time Complexity | $O(n^2)$ | $O(n)$ |
| Space Complexity | $O(n)$ | $O(n)$ |
| Best Case Time | $O(n)$ (descending) | $O(n)$ |
| Worst Case Time | $O(n^2)$ (ascending) | $O(n)$ |
| Comparisons (n=1000) | ~500,000 | ~2,000 |

## Edge Cases

1. **Empty array**: `[]` → `[]`
2. **Single element**: `[5]` → `[-1]`
3. **All ascending**: `[1, 2, 3]` → `[-1, 1, 2]`
4. **All descending**: `[3, 2, 1]` → `[-1, -1, -1]`
5. **All equal**: `[5, 5, 5]` → `[-1, -1, -1]`
6. **Duplicates**: `[4, 5, 5, 2]` → `[-1, 4, 4, -1]`

## Related Problems

- **Next Greater Element**: Similar but looks forward and finds greater elements
- **Daily Temperatures**: Find days until warmer temperature
- **Stock Span Problem**: Count consecutive days with lower/equal stock prices
- **Largest Rectangle in Histogram**: Uses monotonic stack for boundary finding

## Implementation Notes

- Use `list` as stack in Python (with `append`/`pop`)
- Stack stores actual values, not indices (could store indices for more complex variants)
- The >= comparison is important (not just >), as equal elements should also be removed
- Empty stack check before accessing `stack[-1]`
