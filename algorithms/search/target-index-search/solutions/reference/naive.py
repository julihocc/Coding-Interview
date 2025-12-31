from typing import List


class LinearTargetIndexFinder:
    """Linear scan to locate the target index."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def target_index_search(self, target: int) -> int:
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                return i
        return -1
