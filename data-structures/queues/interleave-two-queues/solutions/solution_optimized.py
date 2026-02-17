"""
Interleave Two Queues - Optimized Solution

Iterates through both queues simultaneously to create the interleaved result.
Avoids creating intermediate lists.
"""

from collections import deque

class Solution:
    def interleave_queues(self, q1: deque, q2: deque) -> deque:
        """
        Interleaves two queues by iterating directly.
        
        Args:
            q1 (deque): First input queue.
            q2 (deque): Second input queue.
            
        Returns:
            deque: A new queue with interleaved elements.
        """
        result = deque()
        
        # Iterate over both queues simultaneously
        for e1, e2 in zip(q1, q2):
            result.append(e1)
            result.append(e2)
            
        return result

if __name__ == "__main__":
    sol = Solution()
    q1 = deque([1, 2, 3])
    q2 = deque([4, 5, 6])
    print(f"Result: {list(sol.interleave_queues(q1, q2))}")
