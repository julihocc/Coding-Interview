class LinearScanCrossoverFinder:
    """Linear scan from the right to locate the crossover index."""

    def findCrossoverIndex(self, x, y):
        assert len(x) == len(y)
        n = len(x)

        for i in range(n - 1, -1, -1):
            if x[i] >= y[i]:
                return i

        return -1
