class Solution:
    """
    Naive implementation of TopKHeap using a list and sorting.
    """
    def __init__(self, k):
        self.k = k
        self.data = []

    def size(self):
        return len(self.get_top_k())

    def get_top_k(self):
        return sorted(self.data)[:self.k]

    def insert(self, elt):
        self.data.append(elt)

    def delete_top_k(self, j):
        """Delete j-th smallest element from the top k."""
        top_k = self.get_top_k()
        if j < len(top_k):
            val = top_k[j]
            self.data.remove(val)
        
    @property
    def A(self):
        # Compatibility property for the judge
        return self.get_top_k()
