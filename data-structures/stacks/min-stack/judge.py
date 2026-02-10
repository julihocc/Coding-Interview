import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    """Test a single case for MinStack."""
    stack = SolutionClass()
    results = []
    
    for op, val, expected in zip(case.operations, case.values, case.expected):
        if op == "push":
            result = stack.push(val)
        elif op == "pop":
            result = stack.pop()
        elif op == "top":
            result = stack.top()
        elif op == "get_min":
            result = stack.get_min()
        else:
            raise ValueError(f"Unknown operation: {op}")
        
        results.append(result)
    
    return results == case.expected

if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
