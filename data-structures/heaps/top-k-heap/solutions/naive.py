"""TopKHeap - Data structure maintaining the k smallest elements.

Uses a sorted array A for the k smallest elements and a min-heap H for the rest.

Time complexity:
    - insert: O(k) worst case
    - delete_top_k: O(k + log n)
"""
import bisect


def solve():
    """Naive TopKHeap with manual min-heap for overflow."""

    class MinHeap:
        def __init__(self):
            self.H = [None]

        def size(self):
            return len(self.H) - 1

        def min_element(self):
            return self.H[1]

        def insert(self, elt):
            self.H.append(elt)
            idx = len(self.H) - 1
            while idx > 1:
                p = idx // 2
                if self.H[p] <= self.H[idx]:
                    break
                self.H[p], self.H[idx] = self.H[idx], self.H[p]
                idx = p

        def delete_min(self):
            if self.size() == 0:
                return
            if self.size() == 1:
                self.H.pop()
                return
            self.H[1] = self.H.pop()
            idx = 1
            while True:
                l = 2 * idx
                r = 2 * idx + 1
                lval = self.H[l] if l < len(self.H) else float('inf')
                rval = self.H[r] if r < len(self.H) else float('inf')
                if self.H[idx] <= min(lval, rval):
                    break
                child = l if lval <= rval else r
                self.H[idx], self.H[child] = self.H[child], self.H[idx]
                idx = child

    class TopKHeap:
        def __init__(self, k):
            self.k = k
            self.A = []
            self.H = MinHeap()

        def size(self):
            return len(self.A) + self.H.size()

        def insert_into_A(self, elt):
            self.A.append(elt)
            j = len(self.A) - 1
            while j >= 1 and self.A[j] < self.A[j - 1]:
                self.A[j], self.A[j - 1] = self.A[j - 1], self.A[j]
                j -= 1

        def insert(self, elt):
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
            assert self.size() > self.k
            del self.A[j]
            mv = self.H.min_element()
            self.H.delete_min()
            self.A.append(mv)
            idx = len(self.A) - 1
            while idx >= 1 and self.A[idx] < self.A[idx - 1]:
                self.A[idx], self.A[idx - 1] = self.A[idx - 1], self.A[idx]
                idx -= 1

    return TopKHeap
