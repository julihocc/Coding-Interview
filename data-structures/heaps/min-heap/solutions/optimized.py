"""MinHeap - Optimized implementation using iterative bubble operations."""


class MinHeap:
        def __init__(self):
            self.H = [None]  # 1-indexed array

        def size(self):
            return len(self.H) - 1

        def min_element(self):
            assert self.size() > 0, "Heap is empty"
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

