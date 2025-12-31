class LinearCubeRootFinder:
    """Linear search for the largest k with k^3 <= n."""

    def integerCubeRoot(self, n):
        if n == 0:
            return 0
        if n < 0:
            return -self.integerCubeRoot(-n)

        k = 1
        while (k + 1) ** 3 <= n:
            k += 1
        return k
