# Find First Occurrence

Given a sorted array of integers that may contain duplicates, return the index of the first occurrence of a target value or -1 if not found.

## Example

**Input:**
```python
nums = [1, 2, 3, 4, 5]
target = 3
```
**Output:**
```python
2
```

**Explanation:**
We perform binary search on `[1,2,3,4,5]`.
- low=0, high=4 -> mid=2 -> nums[2]=3 equals target. Record result=2, then search left half.
- Update high=mid-1=1. Now low=0, high=1 -> mid=0 -> nums[0]=1 < target, so move low to mid+1=1.
- low=1, high=1 -> mid=1 -> nums[1]=2 < target, so move low to mid+1=2.
- Now low(2)>high(1), terminate. The first occurrence found is at index 2.

## Input Format

The function accepts two parameters:
1. `nums` (List[int]): An array of integers sorted in non-decreasing order.
2. `target` (int): The integer value to search for.

## Constraints

- $0 \le nums.length \le 1000$
- $-10^9 \le nums[i] \le 10^9$ for all $0 \le i < nums.length$
- $-10^9 \le target \le 10^9$
- Arrays are sorted in non-decreasing order.

## Output Format

Output a single `int`: the index (0-based) of the first occurrence of `target` in the array `nums`. If `target` does not exist in `nums`, output `-1`.

### Solution Signature
```python
def find_first_occurrence(nums: List[int], target: int) -> int:
```

## Local Testing

### Requirements
- Python 3
- `uv` (recommended)

### Running Tests
To run the Modern Virtual Judge for this problem:
```bash
uv run python hackerrank/find-first-occurrence/judge.py
```
