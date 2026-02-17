"""
Moving Average - Optimized Solution

Calculates the moving average using a sliding window with a deque.
This approach maintains the sum and elements in O(1) time.
"""

from collections import deque

class Solution:
    """
    Calculates the moving average of a data stream within a sliding window.
    """
    def __init__(self, size: int):
        """
        Initialize the Solution object with a window size.
        
        Args:
            size (int): The size of the sliding window.
        """
        self.queue = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        """
        Add a new value to the stream and return the moving average.
        
        Args:
            val (int): The next value in the stream.
        
        Returns:
            float: The moving average of the current window.
        """
        # If the window is full, remove the oldest element
        if len(self.queue) == self.size:
            self.total -= self.queue.popleft()
            
        self.queue.append(val)
        self.total += val
        
        return round(self.total / len(self.queue), 2)

if __name__ == "__main__":
    sol = Solution(3)
    print(sol.next(1))  # 1.0
    print(sol.next(10)) # 5.5
    print(sol.next(3))  # 4.67
    print(sol.next(5))  # 6.0
