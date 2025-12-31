from typing import List


class SortThenPickSelector:
    """Sort then pick the k-th element."""

    def quickselect(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[k]
