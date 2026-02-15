from collections import deque


class Solution:
    """Queue implementation template.
    
    Implement a queue data structure with FIFO (First-In, First-Out) behavior.
    Use collections.deque for O(1) enqueue and dequeue operations.
    """
    
    def __init__(self):
        """Initialize an empty queue.
        
        Hint: Use collections.deque() to create a double-ended queue.
        """
        raise NotImplementedError("Initialize your queue here")
    
    def enqueue(self, element):
        """Add an element to the end of the queue.
        
        Args:
            element: The element to add to the queue
            
        Time Complexity: O(1)
        
        Hint: Use append() method to add to the end.
        """
        raise NotImplementedError("Implement enqueue operation")
    
    def dequeue(self):
        """Remove and return the element from the front of the queue.
        
        Returns:
            The element at the front of the queue
            
        Time Complexity: O(1)
        
        Hint: Use popleft() method for O(1) removal from front.
        """
        raise NotImplementedError("Implement dequeue operation")
    
    def peek(self):
        """Return the element at the front without removing it.
        
        Returns:
            The element at the front of the queue
            
        Time Complexity: O(1)
        
        Hint: Access the first element using index [0].
        """
        raise NotImplementedError("Implement peek operation")
    
    def is_empty(self):
        """Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        
        Hint: Check the length of the queue.
        """
        raise NotImplementedError("Implement is_empty check")
    
    def size(self):
        """Return the number of elements in the queue.
        
        Returns:
            int: The number of elements in the queue
            
        Time Complexity: O(1)
        
        Hint: Use len() function.
        """
        raise NotImplementedError("Implement size operation")
