class BinarySearchCubeRootFinder:
    """Binary search to find the largest k with k^3 <= n."""

    def integerCubeRoot(self, n):
        assert n > 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self._helper(n, 0, n - 1)

    def _helper(self, n, left, right):
        cube = lambda x: x * x * x
        assert left < right
        mid = (left + right) // 2

        if cube(mid) <= n and cube(mid + 1) > n:
            return mid
        if cube(mid) > n:
            return self._helper(n, left, mid)
        return self._helper(n, mid, right)
