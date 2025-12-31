"""MedianMaintainingHeap - Efficiently compute median of dynamic dataset.

Uses two heaps: a max-heap for the smaller half and a min-heap for the larger half.

Time complexity:
    - insert: O(log n)
    - get_median: O(1)
"""


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

