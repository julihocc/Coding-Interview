import random
from typing import List

# In-place quicksort with randomized pivots

def _partition(arr: List[int], low: int, high: int) -> int:
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def _quicksort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot_pos = _partition(arr, low, high)
        _quicksort(arr, low, pivot_pos - 1)
        _quicksort(arr, pivot_pos + 1, high)


def quicksort(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums

    _quicksort(nums, 0, len(nums) - 1)
    return nums
