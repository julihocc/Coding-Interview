"""MedianMaintainingHeap - Optimized implementation using heapq."""


class MedianMaintainingHeap:
        def __init__(self):
            self.lower = []  # max-heap via negatives
            self.upper = []  # min-heap

        def size(self):
            return len(self.lower) + len(self.upper)

        def insert(self, elt):
            if not self.lower or elt <= -self.lower[0]:
                heapq.heappush(self.lower, -elt)
            else:
                heapq.heappush(self.upper, elt)

            # Rebalance to ensure len(lower) >= len(upper) and difference <= 1
            if len(self.lower) > len(self.upper) + 1:
                mv = -heapq.heappop(self.lower)
                heapq.heappush(self.upper, mv)
            elif len(self.upper) > len(self.lower):
                mv = heapq.heappop(self.upper)
                heapq.heappush(self.lower, -mv)

        def get_median(self):
            if not self.lower:
                raise AssertionError("Cannot get median from empty heap")
            if len(self.lower) > len(self.upper):
                return -self.lower[0]
            return (-self.lower[0] + self.upper[0]) / 2

