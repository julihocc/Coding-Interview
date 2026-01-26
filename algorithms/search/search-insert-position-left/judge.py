import os
import sys

from tests.cases import TEST_CASES

# Add the root directory to sys.path to allow importing utils
script_dir = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(script_dir, "../../../"))
sys.path.append(ROOT_DIR)

from utils.judge_utils import run_judge_from_file  # noqa: E402

def run_test_case(sol_class, case):
    """Test a single case for search insert position."""
    
    # Check if sol_class is a class or a function
    if isinstance(sol_class, type):
        sol = sol_class()
        if hasattr(sol, 'run'):
             result = sol.run(list(case.nums), case.target)
        # Attempt to find a suitable method if 'run' doesn't exist or specific name is expected
        else:
            # Fallback or specific method call if needed, but for now we expect a class 
            # wrapper with search_insert or similar as per other modules. 
            # However, prompt specifically asked for a function.
            # Let's support both: calling instance.insert_position if it exists, or just the function if passed.
            if hasattr(sol, 'insert_position'):
                result = sol.insert_position(list(case.nums), case.target)
            else:
                 # Try to find any method that looks like a solution
                 methods = [func for func in dir(sol) if callable(getattr(sol, func)) and not func.startswith("__")]
                 if methods:
                     result = getattr(sol, methods[0])(list(case.nums), case.target)
                 else:
                     raise ValueError("No suitable method found in solution class")

    else:
        # It's a function
        result = sol_class(list(case.nums), case.target)

    return result == case.expected

if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_test_case, section_name="Solutions")
