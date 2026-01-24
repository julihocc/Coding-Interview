"""MinHeap - A min-heap data structure with O(log n) insert and delete operations.

Time complexity:
    - insert: O(log n)
    - delete_min: O(log n)
    - min_element: O(1)
"""


class Solution:
            def __init__(self):
                self.H = [None]  # 1-indexed array
    
            def size(self):
                return len(self.H) - 1
    
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
