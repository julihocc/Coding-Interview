"""
Moving Average - Naive Solution

Maintains a list of elements. Re-sums the list every time to calculate average.
Time complexity is O(M) where M is the window size.
"""

class Solution:
    """
    Calculates the moving average of a data stream.
    """
    def __init__(self, size: int):
        """
        Initialize the Solution object with a window size.
        
        Args:
            size (int): The size of the sliding window.
        """
        self.size = size
        self.window = []

    def next(self, val: int) -> float:
        """
        Add a new value to the stream and return the moving average.
        
        Args:
            val (int): The next value in the stream.
        
        Returns:
            float: The moving average of the current window.
        """
        self.window.append(val)
        
        if len(self.window) > self.size:
            self.window.pop(0) # Remove oldest element (O(M))
            
        current_sum = sum(self.window) # O(M)
        return round(current_sum / len(self.window), 2)

if __name__ == "__main__":
    sol = Solution(3)
    print(sol.next(1))  # 1.0
    print(sol.next(10)) # 5.5
    print(sol.next(3))  # 4.67
    print(sol.next(5))  # 6.0
