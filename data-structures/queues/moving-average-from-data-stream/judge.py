import sys
import os

# Add the root directory to sys.path to allow imports from utils
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_classes, run_tests
from tests.cases import TEST_CASES

def run_case_logic(cls, case):
    """
    Test logic for Moving Average.
    """
    # Instantiate the Solution class with the window size
    solver = cls(case.size)
    
    # Process each operation and compare with expected output
    for val, expected_avg in zip(case.operations, case.expected):
        result = solver.next(val)
        
        # Check against expected average (allowing small floating point differences)
        if abs(result - expected_avg) > 1e-9:
            return False
                
    return True

if __name__ == "__main__":
    solutions_dir = os.path.join(current_dir, 'solutions')
    
    # Load Solution classes
    solutions = load_classes(solutions_dir, "Solution", subfolder=".")
    
    # Run the tests
    run_tests(solutions, TEST_CASES, run_case_logic, section_name="Moving Average", report_dir=current_dir)
