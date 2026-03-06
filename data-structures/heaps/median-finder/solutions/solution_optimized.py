import heapq


class Solution:
    def __init__(self):
        # We use a max heap (simulated with negative numbers) for the smaller half
        # and a min heap for the larger half.
        # self.heaps[0] corresponds to 'small', self.heaps[1] corresponds to 'large'
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps

        # Add to max heap (small) by pushing negative
        heapq.heappush(small, -heapq.heappushpop(large, num))

        # Balance the heaps
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        # We subtract `small[0]` from `large[0]`, because `small` consists of negative values
        return float((large[0] - small[0]) / 2.0)
