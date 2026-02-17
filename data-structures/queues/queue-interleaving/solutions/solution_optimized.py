"""
Queue Interleaving - Optimized Solution

Interleaves the first half of the queue with the second half using a single auxiliary queue.
"""

from collections import deque

class Solution:
    def interleave_queue(self, queue: deque) -> deque:
        """
        Interleaves the first half of the queue with the second half.
        
        Args:
        queue (deque): A deque of integers.
        
        Returns:
        deque: The interleaved queue.
        """
        if not queue:
            return queue
            
        half_size = len(queue) // 2
        first_half = deque()

        # Dequeue the first half elements into a temporary queue
        for _ in range(half_size):
            first_half.append(queue.popleft())

        # Interleave elements
        while first_half:
            queue.append(first_half.popleft())
            if queue: 
                queue.append(queue.popleft())
                
        return queue

if __name__ == "__main__":
    # Simple manual test
    sol = Solution()
    q = deque([1, 2, 3, 4, 5, 6])
    print(f"Input: [1, 2, 3, 4, 5, 6]")
    result = sol.interleave_queue(q)
    print(f"Output: {list(result)}")
