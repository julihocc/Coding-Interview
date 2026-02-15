import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    """Test a single case for basic queue operations."""
    queue = SolutionClass()
    
    for i, operation in enumerate(case.operations):
        args = case.arguments[i]
        expected = case.expected[i]
        
        if operation == "enqueue":
            result = queue.enqueue(*args)
        elif operation == "dequeue":
            result = queue.dequeue()
        elif operation == "peek":
            result = queue.peek()
        elif operation == "is_empty":
            result = queue.is_empty()
        elif operation == "size":
            result = queue.size()
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        if result != expected:
            return False
    
    return True

if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
