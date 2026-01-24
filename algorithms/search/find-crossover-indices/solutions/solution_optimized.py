class Solution:
    """Binary search refinement to locate the crossover index."""

    def __init__(self, x, y):
        assert len(x) == len(y)
        self.x = x
        self.y = y

    def findCrossoverIndex(self):
        n = len(self.x)
        if n == 0:
            return -1
        return self._helper(0, n - 1)

    def _helper(self, left, right):
        assert left <= right
        if left + 1 == right:
            return left

        mid = (left + right) // 2

        if self.x[mid] > self.y[mid]:
            return self._helper(mid, right)
        if self.x[mid] >= self.y[mid]:
            return self._helper(mid, right)
        return self._helper(left, mid)
