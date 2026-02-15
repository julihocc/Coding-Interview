from collections import deque


class Solution:
    """Printer queue simulation template.
    
    Implement a printer queue system that processes print jobs in FIFO order.
    Use collections.deque for efficient O(1) operations.
    """
    
    def __init__(self):
        """Initialize an empty printer queue.
        
        Hint: Use collections.deque() to store job names.
        """
        raise NotImplementedError("Initialize your printer queue here")
    
    def add_job(self, job_name: str):
        """Add a print job to the queue.
        
        Args:
            job_name: Name of the document/file to print
            
        Time Complexity: O(1)
        
        Hint: Use append() to add jobs to the end of the queue.
        """
        raise NotImplementedError("Implement add_job operation")
    
    def process_job(self) -> str:
        """Process the next print job in the queue.
        
        Returns:
            str: Name of the job being processed
            
        Time Complexity: O(1)
        
        Hint: Use popleft() to remove and return the first job.
        """
        raise NotImplementedError("Implement process_job operation")
    
    def peek_next_job(self) -> str:
        """View the next job without processing it.
        
        Returns:
            str: Name of the next job to be processed
            
        Time Complexity: O(1)
        
        Hint: Access the first element without removing it.
        """
        raise NotImplementedError("Implement peek_next_job operation")
    
    def is_queue_empty(self) -> bool:
        """Check if the printer queue is empty.
        
        Returns:
            bool: True if no jobs pending, False otherwise
            
        Time Complexity: O(1)
        
        Hint: Check if the queue has any elements.
        """
        raise NotImplementedError("Implement is_queue_empty check")
    
    def queue_size(self) -> int:
        """Return the number of pending print jobs.
        
        Returns:
            int: Number of jobs waiting to be printed
            
        Time Complexity: O(1)
        
        Hint: Use len() to get the queue size.
        """
        raise NotImplementedError("Implement queue_size operation")
    
    def get_all_jobs(self) -> list:
        """Return a list of all pending job names.
        
        Returns:
            list: List of job names in queue order
            
        Time Complexity: O(n)
        
        Hint: Convert the deque to a list.
        """
        raise NotImplementedError("Implement get_all_jobs operation")
