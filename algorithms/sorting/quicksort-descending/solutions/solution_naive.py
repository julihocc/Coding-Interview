from typing import List


class Solution:
    """Use built-in sort to return a sorted copy in descending order."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def quicksort(self) -> List[int]:
        return sorted(self.nums, reverse=True)
