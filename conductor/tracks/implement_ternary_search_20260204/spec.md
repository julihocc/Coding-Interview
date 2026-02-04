# Specification: Implement Ternary Search Algorithm

## Introduction
This specification outlines the implementation of the Ternary Search algorithm, a divide and conquer algorithm that can be used to find an element in a sorted array or to find the minimum or maximum of a unimodal function. It is similar to binary search but divides the array into three parts instead of two.

## Problem Statement
The goal is to implement the Ternary Search algorithm for finding a target element within a sorted array of integers. Additionally, the implementation should be robust enough to be integrated into the existing judge system, allowing for testing and performance analysis against other search algorithms.

## Requirements

### Functional Requirements
- **F.1**: The algorithm must correctly identify the index of the target element if it exists in the sorted array.
- **F.2**: The algorithm must return -1 if the target element is not found in the array.
- **F.3**: The implementation must adhere to the existing `Solution` class structure in `algorithms/search/` solutions.
- **F.4**: The implementation must be compatible with the current `judge.py` and `judge_utils.py` for testing.

### Non-Functional Requirements
- **N.1 - Performance**: The algorithm should have a time complexity of O(log n) for searching in a sorted array, similar to binary search.
- **N.2 - Code Quality**: The code must be clean, readable, and follow the Python code style guidelines (`conductor/code_styleguides/python.md`).
- **N.3 - Testability**: The solution must be easily testable with unit tests and integrate seamlessly with the existing test framework.

## Algorithm Details

### Ternary Search for Sorted Array
1.  Initialize `left = 0` and `right = array.length - 1`.
2.  While `left <= right`:
    a. Calculate `mid1 = left + (right - left) / 3`.
    b. Calculate `mid2 = right - (right - left) / 3`.
    c. If `array[mid1] == target`, return `mid1`.
    d. If `array[mid2] == target`, return `mid2`.
    e. If `target < array[mid1]`, search in the left third: `right = mid1 - 1`.
    f. Else if `target > array[mid2]`, search in the right third: `left = mid2 + 1`.
    g. Else (`array[mid1] < target < array[mid2]`), search in the middle third: `left = mid1 + 1`, `right = mid2 - 1`.
3.  Return -1 (target not found).

## Integration with Judge System
The new Ternary Search solution will be added to `algorithms/search/ternary-search/solutions/` as `solution_ternary.py`. A new `judge.py` and `tests/cases.py` will be created specifically for ternary search, following the existing patterns in other search algorithm directories.
