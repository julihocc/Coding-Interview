import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    """Test a single case for printer queue operations."""
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
            raise ValueError(f"Unknown operation: {operation}")
        
        if result != expected:
            return False
    
    return True

if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
