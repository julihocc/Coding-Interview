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
                solutions.append((module_name, func))
            else:
                 print(f"Warning: {function_name} not found in {base_name}")
                 
    return sorted(solutions, key=lambda x: x[0])

def run_test_case(solution_func, case_name, input_path, output_path):
    # Read input
    with open(input_path, 'r') as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    try:
        if len(lines) >= 3:
            # Format: Target, N, Array
            target = int(lines[0])
            n = int(lines[1])
            nums = list(map(int, lines[2].split()))
        elif len(lines) == 2:
            # Fallback Format: Target, Array (or N, Array - but target is critical)
            # Assuming Target, Array based on common formats if N is implicit
            target = int(lines[0])
            nums = list(map(int, lines[1].split()))
        else:
            return False, 0
    except ValueError:
        return False, 0

    # Read expected output
    with open(output_path, 'r') as f:
        expected = int(f.read().strip())

    start_time = time.perf_counter()
    result = solution_func(nums, target)
    end_time = time.perf_counter()
    duration = end_time - start_time

    return (result == expected), duration

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(base_dir, 'tests')
    input_dir = os.path.join(test_dir, 'input')
    output_dir = os.path.join(test_dir, 'output')
    solutions_dir = os.path.join(base_dir, 'solutions')
    
    input_files = sorted(glob.glob(os.path.join(input_dir, 'input*.txt')))
    
    # Dynamic discovery
    solutions = load_solutions(solutions_dir, 'target_index_search')
    
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
                continue
                
            try:
                passed, duration = run_test_case(sol_func, case_name, input_path, output_path)
                status = "PASS" if passed else "FAIL"
                print(f"{sol_name:<15} | {case_name:<10} | {status:<10} | {duration:<10.6f}")
            except Exception as e:
                print(f"{sol_name:<15} | {case_name:<10} | ERROR      | 0.000000")
        print("-" * 55)

if __name__ == "__main__":
    main()
