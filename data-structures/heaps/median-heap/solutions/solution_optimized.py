"""MedianMaintainingHeap - Efficiently compute median of dynamic dataset.

Uses two heaps: a max-heap for the smaller half and a min-heap for the larger half.

Time complexity:
    - insert: O(log n)
    - get_median: O(1)
"""


class MinHeap:
    def __init__(self):
        self.H = [None]  # 1-indexed array

    def size(self):
        return len(self.H) - 1

    def min_element(self):
        assert self.size() > 0, "Heap is empty"
        return self.H[1]

    def bubble_up(self, i):
        if i == 1:
            return
        p = i // 2
        if self.H[p] <= self.H[i]:
            return
        self.H[p], self.H[i] = self.H[i], self.H[p]
        self.bubble_up(p)

    def bubble_down(self, i):
        l = 2 * i
        r = 2 * i + 1
        lval = self.H[l] if l < len(self.H) else float('inf')
        rval = self.H[r] if r < len(self.H) else float('inf')
        if self.H[i] <= min(lval, rval):
            return
        child = l if lval <= rval else r
        self.H[i], self.H[child] = self.H[child], self.H[i]
        self.bubble_down(child)

    def insert(self, elt):
        self.H.append(elt)
        self.bubble_up(len(self.H) - 1)

    def delete_min(self):
        if self.size() == 0:
            return
        if self.size() == 1:
            self.H.pop()
            return
        self.H[1] = self.H.pop()
        self.bubble_down(1)


class MaxHeap:
    def __init__(self):
        self.H = [None]  # 1-indexed array

    def size(self):
        return len(self.H) - 1

    def max_element(self):
        assert self.size() > 0, "Heap is empty"
        return self.H[1]

    def bubble_up(self, i):
        if i == 1:
            return
        p = i // 2
        if self.H[p] >= self.H[i]:
            return
        self.H[p], self.H[i] = self.H[i], self.H[p]
        self.bubble_up(p)

    def bubble_down(self, i):
        l = 2 * i
        r = 2 * i + 1
        lval = self.H[l] if l < len(self.H) else float('-inf')
        rval = self.H[r] if r < len(self.H) else float('-inf')
        if self.H[i] >= max(lval, rval):
            return
        child = l if lval >= rval else r
        self.H[i], self.H[child] = self.H[child], self.H[i]
        self.bubble_down(child)

    def insert(self, elt):
        self.H.append(elt)
        self.bubble_up(len(self.H) - 1)

    def delete_max(self):
        if self.size() == 0:
            return
        if self.size() == 1:
            self.H.pop()
            return
        self.H[1] = self.H.pop()
        self.bubble_down(1)


class Solution:
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
