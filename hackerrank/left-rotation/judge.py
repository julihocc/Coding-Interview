import sys
import os
import time
import glob
from solutions import naive, optimized, original

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
    # Need to pass a copy because naive/optimized might modify in place (though we wrote them to be safe)
    # But especially naive modifiying list in loop would break if we reused same list object? 
    # Our naive implementation modifies in-place! So we MUST pass a copy.
    result = solution_func(list(a), d) 
    end_time = time.perf_counter()
    duration = end_time - start_time

    # Verify
    passed = (result == expected)
    return passed, duration

def main():
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    input_dir = os.path.join(test_dir, 'input')
    output_dir = os.path.join(test_dir, 'output')
    
    input_files = sorted(glob.glob(os.path.join(input_dir, 'input*.txt')))
    
    solutions = [
        ("Naive", naive.rotLeft),
        ("Optimized", optimized.rotLeft),
        ("Original", original.rotLeft)
    ]
    
    print(f"{'Solution':<12} | {'Case':<10} | {'Status':<10} | {'Time (s)':<10}")
    print("-" * 50)
    
    for sol_name, sol_func in solutions:
        for input_path in input_files:
            filename = os.path.basename(input_path)
            case_name = filename.replace('input', '').replace('.txt', '')
            output_filename = filename.replace('input', 'output')
            output_path = os.path.join(output_dir, output_filename)
            
            if not os.path.exists(output_path):
                print(f"{sol_name:<12} | {case_name:<10} | {'No Output':<10} | {'-':<10}")
                continue
                
            passed, duration = run_test_case(sol_func, case_name, input_path, output_path)
            status = "PASS" if passed else "FAIL"
            print(f"{sol_name:<12} | {case_name:<10} | {status:<10} | {duration:<10.6f}")
        print("-" * 50)

if __name__ == "__main__":
    main()
