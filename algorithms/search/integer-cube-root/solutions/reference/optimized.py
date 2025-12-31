class BinarySearchCubeRootFinder:
    """Binary search to find the largest k with k^3 <= n."""

    def __init__(self, n):
        assert n > 0
        self.n = n

    def integerCubeRoot(self):
        if self.n == 1:
            return 1
        if self.n == 2:
            return 1
        return self._helper(0, self.n - 1)

    def _helper(self, left, right):
        cube = lambda x: x * x * x
        assert left < right
        mid = (left + right) // 2

        if cube(mid) <= self.n and cube(mid + 1) > self.n:
            return mid
        if cube(mid) > self.n:
            return self._helper(left, mid)
        return self._helper(mid, right)
