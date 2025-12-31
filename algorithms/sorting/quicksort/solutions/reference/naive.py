from typing import List


class BuiltinSorter:
    """Use built-in sort to return a sorted copy."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def quicksort(self) -> List[int]:
        return sorted(self.nums)
