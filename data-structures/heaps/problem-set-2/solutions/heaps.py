"""Reusable heap implementations for problem-set-2.

Exports:
    MinHeap: A min-heap data structure
    MaxHeap: A max-heap data structure
    TopKHeap: Data structure maintaining k smallest elements
    MedianMaintainingHeap: Data structure for efficiently computing median
"""
import bisect


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


class TopKHeap:
    """Data structure to efficiently maintain the k smallest elements.
    
    Uses a sorted array A for the k smallest elements and a min-heap H for the rest.
    
    Time complexity:
        - insert: O(k) worst case
        - delete_top_k: O(k + log n)
    """
    
    def __init__(self, k):
        self.k = k
        self.A = []
        self.H = MinHeap()
    
    def size(self):
        return len(self.A) + self.H.size()
    
    def insert_into_A(self, elt):
        """Insert element into sorted array A."""
        self.A.append(elt)
        j = len(self.A) - 1
        while j >= 1 and self.A[j] < self.A[j - 1]:
            self.A[j], self.A[j - 1] = self.A[j - 1], self.A[j]
            j -= 1
    
    def insert(self, elt):
        """Insert element into the data structure."""
        if self.size() < self.k:
            self.insert_into_A(elt)
            return
        if len(self.A) > 0 and elt < self.A[-1]:
            pos = bisect.bisect_left(self.A, elt)
            self.A.insert(pos, elt)
            displaced = self.A.pop()
            self.H.insert(displaced)
        else:
            self.H.insert(elt)
    
    def delete_top_k(self, j):
        """Delete the j-th smallest element (0-indexed)."""
        assert self.size() > self.k
        del self.A[j]
        mv = self.H.min_element()
        self.H.delete_min()
        self.A.append(mv)
        idx = len(self.A) - 1
        while idx >= 1 and self.A[idx] < self.A[idx - 1]:
            self.A[idx], self.A[idx - 1] = self.A[idx - 1], self.A[idx]
            idx -= 1


class MedianMaintainingHeap:
    """Data structure to efficiently compute the median of a dynamic dataset.
    
    Uses two heaps: a max-heap for the smaller half and a min-heap for the larger half.
    
    Time complexity:
        - insert: O(log n)
        - get_median: O(1)
    """
    
    def __init__(self):
        self.L = MaxHeap()  # max-heap for smaller half
        self.R = MinHeap()  # min-heap for larger half
    
    def size(self):
        return self.L.size() + self.R.size()
    
    def insert(self, elt):
        """Insert element and maintain heap balance."""
        if self.L.size() == 0 or elt <= self.L.max_element():
            self.L.insert(elt)
        else:
            self.R.insert(elt)
        
        # Rebalance heaps if necessary
        if self.L.size() > self.R.size() + 1:
            mv = self.L.max_element()
            self.L.delete_max()
            self.R.insert(mv)
        elif self.R.size() > self.L.size():
            mv = self.R.min_element()
            self.R.delete_min()
            self.L.insert(mv)
    
    def get_median(self):
        """Get the median of the dataset."""
        if self.L.size() > self.R.size():
            return self.L.max_element()
        return (self.L.max_element() + self.R.min_element()) / 2
