import sys
import os
from collections import deque

# Add the root directory to sys.path to allow imports from utils
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_classes, run_tests
from tests.cases import TEST_CASES

def run_case_logic(cls, case):
    """
    Test logic for Interleave Two Queues.
    """
    # Create copies of input queues to ensure originals are not modified if checked
    # (Though the problem statement says don't modify, we test the result)
    q1_copy = deque(case.q1)
    q2_copy = deque(case.q2)
    
    # Instantiate Solution
    solver = cls()
    
    # Call the method
    result = solver.interleave_queues(q1_copy, q2_copy)
    
    # Check result
    if list(result) != case.expected:
        return False
        
    # Optional: Check if inputs were modified? 
    # The problem says "Should not modify", but strict enforcement depends on requirements.
    # For now, we focus on correctness of output.
    
    return True

if __name__ == "__main__":
    solutions_dir = os.path.join(current_dir, 'solutions')
    
    # Load Solution classes
    solutions = load_classes(solutions_dir, "Solution", subfolder=".")
    
    # Run the tests
    run_tests(solutions, TEST_CASES, run_case_logic, section_name="Interleave Two Queues", report_dir=current_dir)
