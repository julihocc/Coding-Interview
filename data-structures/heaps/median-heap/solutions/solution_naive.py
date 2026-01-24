import statistics

class Solution:
    """
    Naive implementation of MedianHeap using a list and sorting/statistics.
    """
    def __init__(self):
        self.data = []

    def insert(self, elt):
        self.data.append(elt)

    def get_median(self):
        if not self.data:
            return 0
        return statistics.median(self.data)
    
    def size(self):
        return len(self.data)
