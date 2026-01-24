from typing import List

class Solution:
    def rotLeft(self, a: List[int], d: int) -> List[int]:
        """
        Optimized implementation of left rotation using slicing.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(a)
        if n == 0:
            return a
        d = d % n
        return a[d:] + a[:d]
