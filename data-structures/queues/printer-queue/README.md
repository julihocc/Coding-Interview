# Printer Queue Simulation

## Problem Description

Simulate a printer queue system where print jobs are processed in the order they arrive (FIFO). Implement a `Solution` class that manages printer jobs and processes them sequentially.

The printer queue system should:
1. Accept print jobs with job names
2. Process jobs in the order they were received
3. Track which jobs have been processed
4. Report the current queue status

## Real-World Application

In an office environment, multiple users send print jobs to a shared printer. The printer processes these jobs one at a time in the order they were received. This ensures fairness - the person who submitted their job first gets it printed first.

## Examples

### Example 1: Basic Printer Queue
```python
printer = Solution()
printer.add_job('Document1')
printer.add_job('Document2')
printer.add_job('Picture1')

# Process all jobs
results = []
while not printer.is_queue_empty():
    job = printer.process_job()
    results.append(job)

# Output: ['Document1', 'Document2', 'Picture1']
```

### Example 2: Interleaved Operations
```python
printer = Solution()
printer.add_job('Report.pdf')
printer.add_job('Presentation.pptx')
print(printer.process_job())      # Output: 'Report.pdf'
printer.add_job('Spreadsheet.xlsx')
print(printer.process_job())      # Output: 'Presentation.pptx'
print(printer.queue_size())       # Output: 1
```

## Operations

1. **add_job(job_name)**: Add a print job to the queue
2. **process_job()**: Remove and return the next job to be printed
3. **peek_next_job()**: View the next job without processing it
4. **is_queue_empty()**: Check if there are any pending jobs
5. **queue_size()**: Return the number of pending jobs
6. **get_all_jobs()**: Return a list of all pending job names

## Constraints

- Job names are non-empty strings
- Jobs must be processed in FIFO order
- Use `collections.deque` for efficient queue operations
- Handle edge cases (empty queue, multiple identical job names)

## Function Signature

```python
from collections import deque

class Solution:
    def __init__(self):
        # Initialize the printer queue
        pass
    
    def add_job(self, job_name: str):
        # Add a job to the printer queue
        pass
    
    def process_job(self) -> str:
        # Process and return the next job
        pass
    
    def peek_next_job(self) -> str:
        # View the next job without processing
        pass
    
    def is_queue_empty(self) -> bool:
        # Check if queue is empty
        pass
    
    def queue_size(self) -> int:
        # Return number of pending jobs
        pass
    
    def get_all_jobs(self) -> list:
        # Return list of all pending job names
        pass
```

## Notes

- This problem demonstrates a practical application of the Queue data structure
- Real printer spoolers use similar mechanisms with additional features (priority, job cancellation)
- The FIFO property ensures fairness in job processing
