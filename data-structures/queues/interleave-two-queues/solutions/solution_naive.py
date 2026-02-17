"""
Interleave Two Queues - Naive Solution

Converts queues to lists to perform interleaving using index access.
"""

from collections import deque

class Solution:
    def interleave_queues(self, q1: deque, q2: deque) -> deque:
        """
        Interleaves two queues using list conversion.
        
        Args:
            q1 (deque): First input queue.
            q2 (deque): Second input queue.
            
        Returns:
            deque: A new queue with interleaved elements.
        """
        list1 = list(q1)
        list2 = list(q2)
        result = deque()
        
        n = len(list1)
        for i in range(n):
            result.append(list1[i])
            result.append(list2[i])
            
        return result

if __name__ == "__main__":
    sol = Solution()
    q1 = deque([1, 2, 3])
    q2 = deque([4, 5, 6])
    print(f"Result: {list(sol.interleave_queues(q1, q2))}")
