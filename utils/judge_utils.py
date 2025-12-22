import os
import glob
import importlib.util
import time

def load_solutions(solutions_dir, function_name):
    """
    Dynamically loads Python modules from the solutions directory
    and extracts the specified function.
    """
    solutions = []
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

def run_tests(solutions, test_cases, runner_func):
    """
    Runs the provided test runner function for all solutions and cases,
    printing a formatted report.
    """
    if not solutions:
        print("No solutions found.")
        return

    print(f"{'Solution':<15} | {'Case':<15} | {'Status':<10} | {'Time (s)':<10}")
    print("-" * 60)
    
    for sol_name, sol_func in solutions:
        for case in test_cases:
            try:
                # Measure time
                start_time = time.perf_counter()
                passed = runner_func(sol_func, case)
                end_time = time.perf_counter()
                duration = end_time - start_time
                
                status = "PASS" if passed else "FAIL"
                print(f"{sol_name:<15} | {case.id:<15} | {status:<10} | {duration:<10.6f}")
            except Exception as e:
                print(f"{sol_name:<15} | {case.id:<15} | ERROR      | 0.000000")
                print(f"Error details: {e}")
        print("-" * 60)
