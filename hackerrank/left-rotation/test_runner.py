import glob
import os
import subprocess
import sys

def run_tests():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, 'tests', 'input')
    output_dir = os.path.join(script_dir, 'tests', 'output')
    solution_script = os.path.join(script_dir, 'solution.py')

    input_files = sorted(glob.glob(os.path.join(input_dir, '*.txt')))
    
    if not input_files:
        print(f"No input files found in {input_dir}")
        return

    print(f"Running tests...")
    
    passed_count = 0
    total_count = len(input_files)

    for input_file in input_files:
        filename = os.path.basename(input_file)
        expected_output_file = os.path.join(output_dir, filename.replace('input', 'output'))

        if not os.path.exists(expected_output_file):
            print(f"Warning: No expected output file for {filename}")
            continue

        with open(expected_output_file, 'r') as f:
            expected_output = f.read().strip()

        with open(input_file, 'r') as f:
            input_data = f.read()

        try:
            # Run the solution script
            process = subprocess.Popen(
                [sys.executable, solution_script],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(input=input_data)
            
            actual_output = stdout.strip()

            if actual_output == expected_output:
                print(f"PASS: {filename}")
                passed_count += 1
            else:
                print(f"FAIL: {filename}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual:   {actual_output}")
                if stderr:
                    print(f"  Stderr:   {stderr}")

        except Exception as e:
            print(f"ERROR: {filename} - {e}")

    print(f"\nSummary: {passed_count}/{total_count} passed")

if __name__ == "__main__":
    run_tests()
