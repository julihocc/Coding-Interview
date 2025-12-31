from typing import List


class LinearTargetIndexFinder:
    """Linear scan to locate the target index."""

    def target_index_search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
