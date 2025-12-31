from typing import List


class BuiltinSorter:
    """Use built-in sort to return a sorted copy."""

    def quicksort(self, nums: List[int]) -> List[int]:
        return sorted(nums)
