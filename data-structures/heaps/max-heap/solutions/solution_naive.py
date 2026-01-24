class Solution:
    """
    Naive implementation of MaxHeap using a simple list.
    Operations are O(n) or O(n log n) instead of O(log n).
    """
    def __init__(self):
        self.h = []

    def size(self):
        return len(self.h)

    def max_element(self):
        if not self.h:
            raise Exception("Heap is empty")
        return max(self.h)

    def insert(self, elt):
        self.h.append(elt)

    def delete_max(self):
        if not self.h:
            return
        m = max(self.h)
        self.h.remove(m)
