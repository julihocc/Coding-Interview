import sys
import os

# Add the root directory to sys.path to allow imports from utils
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_classes, run_tests
from tests.cases import TEST_CASES

def run_case_logic(cls, case):
    """
    Test logic for Queue Interleaving.
    """
    # Create a copy of the input queue
    input_copy = case.input_queue.copy()
    
    # Instantiate Solution
    solver = cls()
    
    # Call the method
    result = solver.interleave_queue(input_copy)
    
    # Compare with expected queue
    return result == case.expected_queue

if __name__ == "__main__":
    solutions_dir = os.path.join(current_dir, 'solutions')
    
    # Load Solution classes
    solutions = load_classes(solutions_dir, "Solution", subfolder=".")
    
    # Run the tests
    run_tests(solutions, TEST_CASES, run_case_logic, section_name="Queue Interleaving", report_dir=current_dir)
