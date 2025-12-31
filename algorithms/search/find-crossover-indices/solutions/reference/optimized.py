class BinarySearchCrossoverFinder:
    """Binary search refinement to locate the crossover index."""

    def findCrossoverIndex(self, x, y):
        assert len(x) == len(y)
        n = len(x)
        if n == 0:
            return -1

        return self._helper(x, y, 0, n - 1)

    def _helper(self, x, y, left, right):
        assert left <= right
        if left + 1 == right:
            return left

        mid = (left + right) // 2

        if x[mid] > y[mid]:
            return self._helper(x, y, mid, right)
        if x[mid] >= y[mid]:
            return self._helper(x, y, mid, right)
        return self._helper(x, y, left, mid)
