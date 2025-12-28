"""Problem2 - MaxHeap implementation

Exports:
    MaxHeap: A max-heap data structure implementation
    solve(): Test runner for validation
"""

class MaxHeap:
    """Max-heap data structure with O(log n) insert and delete operations.
    
    Time complexity:
        - insert: O(log n)
        - delete_max: O(log n)
        - max_element: O(1)
    """
    
    def __init__(self):
        self.H = [None]  # 1-indexed array
    
    def size(self):
        return len(self.H) - 1
    
    def __repr__(self):
        return str(self.H[1:])
    
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
        """Insert element into heap."""
        self.H.append(elt)
        self.bubble_up(len(self.H) - 1)
    
    def delete_max(self):
        """Remove and return the maximum element."""
        if self.size() == 0:
            return
        if self.size() == 1:
            self.H.pop()
            return
        self.H[1] = self.H.pop()
        self.bubble_down(1)


def solve():
    """Test runner for MaxHeap validation."""

    h=MaxHeap()
    h.insert(5); assert h.max_element()==5
    h.insert(2); assert h.max_element()==5
    h.insert(4); assert h.max_element()==5
    h.insert(-1); assert h.max_element()==5
    h.insert(7); assert h.max_element()==7
    h.delete_max(); assert h.max_element()==5
    h.delete_max(); assert h.max_element()==4
    h.delete_max(); assert h.max_element()==2
    h.delete_max(); assert h.max_element()==-1
    h.delete_max(); assert h.size()==0
    return True
