"""MedianMaintainingHeap - Efficiently compute median of dynamic dataset.

Uses two heaps: a max-heap for the smaller half and a min-heap for the larger half.

Time complexity:
    - insert: O(log n)
    - get_median: O(1)
"""


def solve():
    """Naive median structure with explicit heap classes."""

    class MinHeap:
        def __init__(self):
            self.H = [None]

        def size(self):
            return len(self.H) - 1

        def min_element(self):
            return self.H[1]

        def insert(self, elt):
            self.H.append(elt)
            idx = len(self.H) - 1
            while idx > 1:
                p = idx // 2
                if self.H[p] <= self.H[idx]:
                    break
                self.H[p], self.H[idx] = self.H[idx], self.H[p]
                idx = p

        def delete_min(self):
            if self.size() == 0:
                return
            if self.size() == 1:
                self.H.pop()
                return
            self.H[1] = self.H.pop()
            idx = 1
            while True:
                l = 2 * idx
                r = 2 * idx + 1
                lval = self.H[l] if l < len(self.H) else float('inf')
                rval = self.H[r] if r < len(self.H) else float('inf')
                if self.H[idx] <= min(lval, rval):
                    break
                child = l if lval <= rval else r
                self.H[idx], self.H[child] = self.H[child], self.H[idx]
                idx = child

    class MaxHeap:
        def __init__(self):
            self.H = [None]

        def size(self):
            return len(self.H) - 1

        def max_element(self):
            return self.H[1]

        def insert(self, elt):
            self.H.append(elt)
            idx = len(self.H) - 1
            while idx > 1:
                p = idx // 2
                if self.H[p] >= self.H[idx]:
                    break
                self.H[p], self.H[idx] = self.H[idx], self.H[p]
                idx = p

        def delete_max(self):
            if self.size() == 0:
                return
            if self.size() == 1:
                self.H.pop()
                return
            self.H[1] = self.H.pop()
            idx = 1
            while True:
                l = 2 * idx
                r = 2 * idx + 1
                lval = self.H[l] if l < len(self.H) else float('-inf')
                rval = self.H[r] if r < len(self.H) else float('-inf')
                if self.H[idx] >= max(lval, rval):
                    break
                child = l if lval >= rval else r
                self.H[idx], self.H[child] = self.H[child], self.H[idx]
                idx = child

    class MedianMaintainingHeap:
        def __init__(self):
            self.L = MaxHeap()
            self.R = MinHeap()

        def size(self):
            return self.L.size() + self.R.size()

        def insert(self, elt):
            if self.L.size() == 0 or elt <= self.L.max_element():
                self.L.insert(elt)
            else:
                self.R.insert(elt)

            if self.L.size() > self.R.size() + 1:
                mv = self.L.max_element()
                self.L.delete_max()
                self.R.insert(mv)
            elif self.R.size() > self.L.size():
                mv = self.R.min_element()
                self.R.delete_min()
                self.L.insert(mv)

        def get_median(self):
            if self.L.size() > self.R.size():
                return self.L.max_element()
            return (self.L.max_element() + self.R.min_element()) / 2

    return MedianMaintainingHeap
