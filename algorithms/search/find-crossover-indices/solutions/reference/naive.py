class LinearScanCrossoverFinder:
    """Linear scan from the right to locate the crossover index."""

    def __init__(self, x, y):
        assert len(x) == len(y)
        self.x = x
        self.y = y

    def findCrossoverIndex(self):
        n = len(self.x)

        for i in range(n - 1, -1, -1):
            if self.x[i] >= self.y[i]:
                return i

        return -1
