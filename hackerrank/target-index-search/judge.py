import sys
import os
import time
import glob
# Need to adjust path to import solutions package
# Assuming this script is run as "python hackerrank/target-index-search/judge.py" 
# or using uv run which might handle paths differently.
# Let's handle generic import structure.

from solutions import naive, optimized, original

def run_test_case(solution_func, case_name, input_path, output_path):
    # Read input
    # Format according to README:
    # Line 1: target
    # Line 2: n (or array elements?) NO, sample says:
    # Sample Input 1:
    # 1 (target)
    # 10 (size?) -> actually the sample format in README is confusing or incomplete.
    # Let's check test_original.py or input files to be sure.
    # The PROBLEM description says: two parameters, nums and target.
    # The SAMPLE INPUT says:
    # 1
    # 10
    # 10
    # Output: 0
    # Wait, README Sample 1:
    # 1 (Input?) No.
    # checking README again...
    
    """
    Sample Input 1
    1
    10
    10
    Sample Output 1
    0
    """ 
    # This implies:
    # Line 1: target?
    # Line 2: size?
    # Line 3: array elements? 
    # Let's assume standard hackerrank format:
    # Line 1: target (or n?)
    # Line 2: ...
    # I need to verify checking an actual input file or the test loader code. 
    # But I can't check 'tests/input/file' content easily without listed files.
    # Wait, previous `list_dir` showed `tests/input` exists.
    # Let's ASSUME standard format based on typical problems or sample.
    # Actually, let's write the judge to adapt or read robustly.
    
    with open(input_path, 'r') as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        
    # Heuristic parsing based on sample:
    # If 3 lines: target, n, array_str
    # If 2 lines: target, array_str? 
    
    if len(lines) >= 3:
        target = int(lines[0])
        n = int(lines[1])
        nums = list(map(int, lines[2].split()))
    elif len(lines) == 2:
        # Maybe target, nums?
        try:
            target = int(lines[0])
            nums = list(map(int, lines[1].split()))
        except:
             # Maybe n, nums, and target is separate?
             pass
    else:
        # Fallback or error
        return False, 0

    # Read expected
    with open(output_path, 'r') as f:
        expected = int(f.read().strip())

    start_time = time.perf_counter()
    result = solution_func(nums, target)
    end_time = time.perf_counter()
    duration = end_time - start_time

    return (result == expected), duration

def main():
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    input_dir = os.path.join(test_dir, 'input')
    output_dir = os.path.join(test_dir, 'output')
    
    input_files = sorted(glob.glob(os.path.join(input_dir, 'input*.txt')))
    
    solutions = [
        ("Naive", naive.target_index_search),
        ("Optimized", optimized.target_index_search),
        ("Original", original.target_index_search)
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
                continue
                
            try:
                passed, duration = run_test_case(sol_func, case_name, input_path, output_path)
                status = "PASS" if passed else "FAIL"
                print(f"{sol_name:<12} | {case_name:<10} | {status:<10} | {duration:<10.6f}")
            except Exception as e:
                print(f"{sol_name:<12} | {case_name:<10} | ERROR      | 0.000000")
        print("-" * 50)

if __name__ == "__main__":
    main()
