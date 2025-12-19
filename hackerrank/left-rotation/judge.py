import sys
import os
import time
import glob
import importlib.util
from tests.cases import TEST_CASES

def load_solutions(solutions_dir, function_name):
    solutions = []
    # List all .py files in solutions directory
    sol_files = glob.glob(os.path.join(solutions_dir, "*.py"))
    
    for file_path in sol_files:
        base_name = os.path.basename(file_path)
        if base_name == "__init__.py":
            continue
            
        module_name = base_name.replace(".py", "")
        
        # Dynamic import
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, function_name):
                func = getattr(module, function_name)
                solutions.append((module_name, func))
            else:
                 print(f"Warning: {function_name} not found in {base_name}")
                 
    return sorted(solutions, key=lambda x: x[0])

def run_test_case(solution_func, case):
    # Measure time
    start_time = time.perf_counter()
    # Pass copy of a to ensure isolation
    result = solution_func(list(case.a), case.d) 
    end_time = time.perf_counter()
    duration = end_time - start_time

    # Verify
    passed = (result == case.expected)
    return passed, duration

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')
    
    # Dynamic discovery of solutions
    solutions = load_solutions(solutions_dir, 'rotLeft')
    
    if not solutions:
        print("No solutions found in", solutions_dir)
        return

    print(f"{'Solution':<15} | {'Case':<15} | {'Status':<10} | {'Time (s)':<10}")
    print("-" * 60)
    
    for sol_name, sol_func in solutions:
        for case in TEST_CASES:
            try:
                passed, duration = run_test_case(sol_func, case)
                status = "PASS" if passed else "FAIL"
                print(f"{sol_name:<15} | {case.id:<15} | {status:<10} | {duration:<10.6f}")
            except Exception as e:
                print(f"{sol_name:<15} | {case.id:<15} | ERROR      | 0.000000")
                print(f"Error details: {e}")
        print("-" * 60)

if __name__ == "__main__":
    main()
