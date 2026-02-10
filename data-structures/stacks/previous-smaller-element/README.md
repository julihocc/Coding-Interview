# Previous Smaller Element

## Problem Statement

Given an array of integers, for each element in the array, find the most recent previous element that is strictly smaller than it. If no such element exists, return `-1` for that position.

## Problem Description

You are given a list of integers `numbers`. For each element `numbers[i]`, you need to find the value of the most recent element `numbers[j]` where:
- `j < i` (it appears before the current element)
- `numbers[j] < numbers[i]` (it is strictly smaller)
- `j` is the largest possible index satisfying the above conditions (most recent)

If no such element exists, return `-1` for that position.

## Examples

### Example 1
```
Input: [4, 5, 2, 10, 8]
Output: [-1, 4, -1, 2, 2]

Explanation:
- Index 0 (value 4): No previous elements → -1
- Index 1 (value 5): Previous smaller is 4 at index 0
- Index 2 (value 2): No previous element < 2 → -1
- Index 3 (value 10): Previous smaller is 2 at index 2
- Index 4 (value 8): Previous smaller is 2 at index 2
```

### Example 2
```
Input: [1, 2, 3, 4, 5]
Output: [-1, 1, 2, 3, 4]

Explanation:
Each element's previous element is smaller (ascending order).
```

### Example 3
```
Input: [5, 4, 3, 2, 1]
Output: [-1, -1, -1, -1, -1]

Explanation:
No element has a previous smaller element (descending order).
```

## Real-World Applications

### Stock Price Analysis
In financial analysis, this problem helps identify the most recent day when a stock price was lower than today's price. This is useful for:
- Calculating price support levels
- Identifying buying opportunities
- Analyzing price trends and patterns

### Temperature Analysis
In weather data analysis, finding the most recent day with a lower temperature helps in:
- Understanding weather patterns
- Predicting temperature trends
- Climate change analysis

### Performance Monitoring
In system monitoring, tracking when a metric was last below the current value helps identify:
- Performance degradation patterns
- Resource utilization trends
- Anomaly detection

## Constraints

- The array can contain both positive and negative integers
- Array length: $0 \leq n \leq 10^5$
- Element values: $-10^9 \leq \text{numbers}[i] \leq 10^9$
- Must handle empty arrays and single-element arrays

## Function Signature

```python
class Solution:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers
    
    def find_previous_smaller(self) -> List[int]:
        """
        Returns a list where each element is either:
        - The most recent previous smaller element
        - -1 if no such element exists
        """
        pass
```

## Time and Space Complexity Goals

- **Naive Approach**: $O(n^2)$ time, $O(n)$ space
- **Optimized Approach**: $O(n)$ time, $O(n)$ space

See [ALGORITHM_ANALYSIS.md](ALGORITHM_ANALYSIS.md) for detailed complexity analysis and algorithm explanations.
