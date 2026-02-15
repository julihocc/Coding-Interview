"""Printer queue implementation using collections.deque.

This implementation manages print jobs in FIFO order, simulating a real
printer spooler system.

Time Complexity:
    - add_job: O(1)
    - process_job: O(1)
    - peek_next_job: O(1)
    - is_queue_empty: O(1)
    - queue_size: O(1)
    - get_all_jobs: O(n)
    
Space Complexity: O(n) where n is the number of pending jobs
"""

from collections import deque


class Solution:
    """Printer queue implementation using deque."""
    
    def __init__(self):
        """Initialize an empty printer queue."""
        self.jobs = deque()
    
    def add_job(self, job_name: str):
        """Add a print job to the queue.
        
        Args:
            job_name: Name of the document/file to print
        """
        self.jobs.append(job_name)
    
    def process_job(self) -> str:
        """Process the next print job in the queue.
        
        Returns:
            str: Name of the job being processed
        """
        if not self.is_queue_empty():
            return self.jobs.popleft()
        return None
    
    def peek_next_job(self) -> str:
        """View the next job without processing it.
        
        Returns:
            str: Name of the next job to be processed
        """
        if not self.is_queue_empty():
            return self.jobs[0]
        return None
    
    def is_queue_empty(self) -> bool:
        """Check if the printer queue is empty.
        
        Returns:
            bool: True if no jobs pending, False otherwise
        """
        return len(self.jobs) == 0
    
    def queue_size(self) -> int:
        """Return the number of pending print jobs.
        
        Returns:
            int: Number of jobs waiting to be printed
        """
        return len(self.jobs)
    
    def get_all_jobs(self) -> list:
        """Return a list of all pending job names.
        
        Returns:
            list: List of job names in queue order
        """
        return list(self.jobs)


if __name__ == "__main__":
    import sys
    import os

    # Add the project root to sys.path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    problem_dir = os.path.dirname(current_dir)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(problem_dir)))
    
    sys.path.append(project_root)
    sys.path.append(problem_dir)

    from utils.judge_utils import test_solution
    from tests.cases import TEST_CASES

    def run_case_logic(SolutionClass, case):
        printer = SolutionClass()
        
        for i, operation in enumerate(case.operations):
            args = case.arguments[i]
            expected = case.expected[i]
            
            if operation == "add_job":
                result = printer.add_job(*args)
            elif operation == "process_job":
                result = printer.process_job()
            elif operation == "peek_next_job":
                result = printer.peek_next_job()
            elif operation == "is_queue_empty":
                result = printer.is_queue_empty()
            elif operation == "queue_size":
                result = printer.queue_size()
            elif operation == "get_all_jobs":
                result = printer.get_all_jobs()
            else:
                return False
            
            if result != expected:
                return False
        
        return True
    
    test_solution(Solution, TEST_CASES, run_case_logic)
