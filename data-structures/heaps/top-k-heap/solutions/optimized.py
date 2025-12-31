"""TopKHeap - Optimized implementation using heapq for overflow elements."""


class TopKHeap:
        def __init__(self, k):
            self.k = k
            self.A = []  # sorted list of k smallest
            self.H = []  # min-heap for overflow values

        def size(self):
            return len(self.A) + len(self.H)

        def insert(self, elt):
            if len(self.A) < self.k:
                # insert into sorted buffer A
                idx = len(self.A)
                self.A.append(elt)
                while idx > 0 and self.A[idx] < self.A[idx - 1]:
                    self.A[idx], self.A[idx - 1] = self.A[idx - 1], self.A[idx]
                    idx -= 1
                return

            if elt < self.A[-1]:
                # place in A, push displaced into heap
                self.A.append(elt)
                idx = len(self.A) - 1
                while idx > 0 and self.A[idx] < self.A[idx - 1]:
                    self.A[idx], self.A[idx - 1] = self.A[idx - 1], self.A[idx]
                    idx -= 1
                displaced = self.A.pop()
                heapq.heappush(self.H, displaced)
            else:
                heapq.heappush(self.H, elt)

        def delete_top_k(self, j):
            assert 0 <= j < len(self.A)
            del self.A[j]
            if self.H:
                mv = heapq.heappop(self.H)
                # insert popped value back into sorted A tail
                self.A.append(mv)
                idx = len(self.A) - 1
                while idx > 0 and self.A[idx] < self.A[idx - 1]:
                    self.A[idx], self.A[idx - 1] = self.A[idx - 1], self.A[idx]
                    idx -= 1

