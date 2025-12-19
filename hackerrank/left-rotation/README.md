# Arrays: Left Rotation

## Problem Description
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array `[1, 2, 3, 4, 5]`, then the array would become `[3, 4, 5, 1, 2]`.

Given an array `a` of `n` integers and a number, `d`, perform `d` left rotations on the array and return the updated array.

## Input Format
The first line contains two space-separated integers `n` and `d`, the size of `a` and the number of left rotations.
The second line contains `n` space-separated integers, each an `a[i]`.

### Constraints
- $1 \le n \le 10^5$
- $1 \le d \le n$
- $1 \le a[i] \le 10^6$

## Output Format
Print a single line of `n` space-separated integers denoting the final state of the array after performing `d` left rotations.

### Solution Signature
```python
def rotLeft(a: List[int], d: int) -> List[int]:
```

### Sample Input
```
5 4
1 2 3 4 5
```

### Sample Output
```
5 1 2 3 4
```

## Local Testing

### Requirements
- Python 3
- `uv` (recommended) or standard python

### Running Tests
This directory contains a **Modern Virtual Judge** system that automatically runs all solutions against defined test cases.

To run the judge using `uv`:
```bash
uv run python hackerrank/left-rotation/judge.py
```

To run with standard python:
```bash
python hackerrank/left-rotation/judge.py
```

### Adding Test Cases
Test cases are defined as pure Python dataclasses in `tests/cases.py`. To add a new test case:
1. Open `tests/cases.py`.
2. Add a new `TestCase` object to the `TEST_CASES` list.

Example:
```python
TestCase(
    id="My New Case",
    n=3,
    d=1,
    a=[1, 2, 3],
    expected=[2, 3, 1]
)
```

### Adding Solutions
The judge system automatically discovers any new Python file in the `solutions/` directory. 
1. Create a new `.py` file in `solutions/` (e.g., `solutions/my_algo.py`).
2. Implement the `rotLeft(a, d)` function.
3. Run the judge, and your solution will be automatically tested and benchmarked.
