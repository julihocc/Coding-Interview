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
This directory contains a standard Python `unittest` suite.

To run the tests using `uv`:
```bash
uv run python -m unittest hackerrank/left-rotation/test_solution.py
```

To run with standard python:
```bash
python -m unittest hackerrank/left-rotation/test_solution.py
```

### Adding Test Cases
The test suite automatically finds input files in `tests/input/` and compares them with expected outputs in `tests/output/`.
You can add more test cases by adding `inputXX.txt` and `outputXX.txt` files to the `tests` directory.

## Included Tests
The `test_solution.py` suite includes:
- **Sample Cases**: Verifies against the problem description's sample input/output.
- **Edge Cases**:
    - Rotation by `d = 0` (no change).
    - Rotation by `d = n` (full cycle, no change).
    - Rotation by `d > n` (should behave as `d % n`).
    - Single element arrays.
    - Large values of `d`.
