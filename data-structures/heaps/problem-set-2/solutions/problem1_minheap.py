"""Problem1 - MinHeap implementation

Exports:
    MinHeap: A min-heap data structure implementation
    solve(): Test runner for validation
"""

class MinHeap:
    """Min-heap data structure with O(log n) insert and delete operations.
    
    Time complexity:
        - insert: O(log n)
        - delete_min: O(log n)
        - min_element: O(1)
    """
    
    def __init__(self):
        self.H = [None]  # 1-indexed array
    
    def size(self):
        return len(self.H) - 1
    
    def __repr__(self):
        return str(self.H[1:])
    
    def min_element(self):
        assert self.size() > 0, "Heap is empty"
        return self.H[1]
    
    def bubble_up(self, index):
        if index == 1:
            return
        p = index // 2
        if self.H[p] <= self.H[index]:
            return
        self.H[p], self.H[index] = self.H[index], self.H[p]
        self.bubble_up(p)
    
    def bubble_down(self, index):
        l = 2 * index
        r = 2 * index + 1
        lval = self.H[l] if l < len(self.H) else float('inf')
        rval = self.H[r] if r < len(self.H) else float('inf')
        if self.H[index] <= min(lval, rval):
            return
        child = l if lval <= rval else r
        self.H[index], self.H[child] = self.H[child], self.H[index]
        self.bubble_down(child)
    
    def insert(self, elt):
        """Insert element into heap."""
        self.H.append(elt)
        self.bubble_up(len(self.H) - 1)
    
    def delete_min(self):
        """Remove and return the minimum element."""
        if self.size() == 0:
            return
        if self.size() == 1:
            self.H.pop()
            return
        self.H[1] = self.H.pop()
        self.bubble_down(1)


def solve():
    """Test runner for MinHeap validation."""

    h = MinHeap()
    h.insert(5); assert h.min_element()==5
    h.insert(2); assert h.min_element()==2
    h.insert(4); assert h.min_element()==2
    h.insert(-1); assert h.min_element()==-1
    h.insert(7); assert h.min_element()==-1
    h.delete_min(); assert h.min_element()==2
    h.delete_min(); assert h.min_element()==4
    h.delete_min(); assert h.min_element()==5
    h.delete_min(); assert h.min_element()==7
    h.delete_min(); assert h.size()==0
    return True
