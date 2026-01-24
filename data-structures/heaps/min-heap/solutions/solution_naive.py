class Solution:
    """
    Naive implementation of MinHeap using a simple list.
    Operations are O(n) or O(n log n).
    """
    def __init__(self):
        self.h = []

    def size(self):
        return len(self.h)

    def min_element(self):
        if not self.h:
            raise Exception("Heap is empty")
        return min(self.h)

    def insert(self, elt):
        self.h.append(elt)

    def delete_min(self):
        if not self.h:
            return
        m = min(self.h)
        self.h.remove(m)
