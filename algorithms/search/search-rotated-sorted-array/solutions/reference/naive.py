class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array using linear search.

        Args:
            nums: The rotated sorted array.
            target: The value to search for.

        Returns:
            The index of the target value if found, otherwise -1.
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
