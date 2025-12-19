import sys
import os
import time
import glob
import importlib.util

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
                # Use filename as solution name (e.g., 'naive', 'optimized')
                solutions.append((module_name, func))
            else:
                 print(f"Warning: {function_name} not found in {base_name}")
                 
    return sorted(solutions, key=lambda x: x[0])

def run_test_case(solution_func, case_name, input_path, output_path):
    # Read input
    with open(input_path, 'r') as f:
        lines = f.readlines()
        if not lines: return False, 0
        n, d = map(int, lines[0].split())
        a = list(map(int, lines[1].split()))

    # Read expected output
    with open(output_path, 'r') as f:
        expected = list(map(int, f.read().split()))

    # Measure time
    start_time = time.perf_counter()
    # Pass copy of a to ensure isolation
    result = solution_func(list(a), d) 
    end_time = time.perf_counter()
    duration = end_time - start_time

    # Verify
    passed = (result == expected)
    return passed, duration

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(base_dir, 'tests')
    input_dir = os.path.join(test_dir, 'input')
    output_dir = os.path.join(test_dir, 'output')
    solutions_dir = os.path.join(base_dir, 'solutions')
    
    input_files = sorted(glob.glob(os.path.join(input_dir, 'input*.txt')))
    
    # Dynamic discovery of solutions
    solutions = load_solutions(solutions_dir, 'rotLeft')
    
    if not solutions:
        print("No solutions found in", solutions_dir)
        return

    print(f"{'Solution':<15} | {'Case':<10} | {'Status':<10} | {'Time (s)':<10}")
    print("-" * 55)
    
    for sol_name, sol_func in solutions:
        for input_path in input_files:
            filename = os.path.basename(input_path)
            case_name = filename.replace('input', '').replace('.txt', '')
            output_filename = filename.replace('input', 'output')
            output_path = os.path.join(output_dir, output_filename)
            
            if not os.path.exists(output_path):
                print(f"{sol_name:<15} | {case_name:<10} | {'No Output':<10} | {'-':<10}")
                continue
                
            passed, duration = run_test_case(sol_func, case_name, input_path, output_path)
            status = "PASS" if passed else "FAIL"
            print(f"{sol_name:<15} | {case_name:<10} | {status:<10} | {duration:<10.6f}")
        print("-" * 55)

if __name__ == "__main__":
    main()
