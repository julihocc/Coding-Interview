class LinearCubeRootFinder:
    """Linear search for the largest k with k^3 <= n."""

    def __init__(self, n):
        self.n = n

    def integerCubeRoot(self):
        if self.n == 0:
            return 0
        if self.n < 0:
            return -LinearCubeRootFinder(-self.n).integerCubeRoot()

        k = 1
        while (k + 1) ** 3 <= self.n:
            k += 1
        return k
