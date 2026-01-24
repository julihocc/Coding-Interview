import inspect
import os
import glob
import importlib.util
import time

def load_solutions(solutions_dir, function_name, subfolder='reference'):
    """
    Dynamically loads Python modules from a subfolder of the solutions directory
    and extracts the specified function.
    Excludes hints.py and template.py (learning guides, not solutions).
    
    Args:
        solutions_dir: Path to the solutions directory
        function_name: Name of the function to extract
        subfolder: Subfolder to load from (default: 'reference')
    """
    target_dir = os.path.join(solutions_dir, subfolder)
    if not os.path.exists(target_dir):
        print(f"Warning: {target_dir} does not exist")
        return []
    
    solutions = []
    sol_files = glob.glob(os.path.join(target_dir, "*.py"))
    
    for file_path in sol_files:
        base_name = os.path.basename(file_path)
        # Skip __init__.py and learning guide files
        if base_name in ("__init__.py", "hints.py", "template.py"):
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

def load_classes(solutions_dir, class_name, subfolder='reference', file_pattern="*.py"):
    """
    Dynamically loads Python modules from a directory and extracts the specified class.
    
    Args:
        solutions_dir: Path to the solutions directory
        class_name: Name of the class to extract
        subfolder: Subfolder to load from (default: 'reference'). If None, loads from solutions_dir directly.
        file_pattern: Glob pattern to match files (default: "*.py")
    """
    if subfolder:
        target_dir = os.path.join(solutions_dir, subfolder)
    else:
        target_dir = solutions_dir

    if not os.path.exists(target_dir):
        print(f"Warning: {target_dir} does not exist")
        return []
    
    solutions = []
    sol_files = glob.glob(os.path.join(target_dir, file_pattern))
    
    for file_path in sol_files:
        base_name = os.path.basename(file_path)
        # Skip __init__.py and learning guide files
        if base_name in ("__init__.py", "hints.py", "template.py"):
            continue
            
        module_name = base_name.replace(".py", "")
        
        # Dynamic import
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, class_name):
                cls = getattr(module, class_name)
                solutions.append((module_name, cls))
            else:
                 # Only warn if we expect a solution (e.g. filename starts with solution_)
                 if base_name.startswith("solution_"):
                     print(f"Warning: {class_name} not found in {base_name}")
                 
    return sorted(solutions, key=lambda x: x[0])


def load_classes_with_method(solutions_dir, method_name, subfolder='reference'):
    """
    Dynamically loads Python modules from a subfolder of the solutions directory
    and extracts any class that defines the required method.

    This is useful when solution class names vary by approach (e.g.,
    BinarySearchFinder, LinearScanFinder) but share a common method contract.
    Excludes hints.py and template.py (learning guides, not solutions).
    """
    target_dir = os.path.join(solutions_dir, subfolder)
    if not os.path.exists(target_dir):
        print(f"Warning: {target_dir} does not exist")
        return []

    solutions = []
    sol_files = glob.glob(os.path.join(target_dir, "*.py"))

    for file_path in sol_files:
        base_name = os.path.basename(file_path)
        if base_name in ("__init__.py", "hints.py", "template.py"):
            continue

        module_name = base_name.replace(".py", "")
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if not (spec and spec.loader):
            continue

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        found = False
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__ != module.__name__:
                continue
            if hasattr(obj, method_name):
                solutions.append((module_name, obj))
                found = True

        if not found:
            print(f"Warning: no class with '{method_name}' found in {base_name}")

    return sorted(solutions, key=lambda x: x[0])

def run_tests(solutions, test_cases, runner_func, section_name=None, report_dir=None):
    """
    Runs the provided test runner function for all solutions and cases,
    printing a formatted report and writing it to report.txt.
    
    Args:
        solutions: List of (name, callable) tuples
        test_cases: List of test case objects
        runner_func: Function that runs a single test
        section_name: Optional section header for the output
        report_dir: Optional directory where report.txt should be created (defaults to current directory)
    """
    # Determine report file path
    if report_dir:
        report_path = os.path.join(report_dir, "report.txt")
    else:
        report_path = "report.txt"
    
    # Open report file for writing
    with open(report_path, "w") as report_file:
        def write_both(message):
            """Helper to write to both console and file"""
            print(message)
            report_file.write(message + "\n")
        
        if not solutions:
            if section_name:
                write_both(f"\n=== {section_name} ===")
            write_both("No solutions found.")
            return

        if section_name:
            write_both(f"\n=== {section_name} ===")
        write_both(f"{'Solution':<15} | {'Case':<15} | {'Status':<10} | {'Time (s)':<10}")
        write_both("-" * 60)
        
        for sol_name, sol_func in solutions:
            for case in test_cases:
                try:
                    # Measure time
                    start_time = time.perf_counter()
                    passed = runner_func(sol_func, case)
                    end_time = time.perf_counter()
                    duration = end_time - start_time
                    
                    status = "PASS" if passed else "FAIL"
                    write_both(f"{sol_name:<15} | {case.id:<15} | {status:<10} | {duration:<10.6f}")
                except Exception as e:
                    write_both(f"{sol_name:<15} | {case.id:<15} | ERROR      | 0.000000")
                    error_msg = f"{type(e).__name__}: {str(e)}" if str(e) else type(e).__name__
                    write_both(f"Error details: {error_msg}")
            write_both("-" * 60)

def run_judge_from_file(judge_file_path, test_cases, run_case_logic, section_name='SOLUTIONS'):
    """
    Simplified judge runner that eliminates boilerplate code.
    
    This function handles:
    - Determining the base directory from the judge file path
    - Loading solution classes from the solutions directory
    - Running tests with proper report directory
    
    Args:
        judge_file_path: __file__ from the calling judge script
        test_cases: List of test case objects
        run_case_logic: Function that runs a single test case
        section_name: Optional section header for the output
    
    Example usage in a judge.py file:
        from utils.judge_utils import run_judge_from_file
        from tests.cases import TEST_CASES
        
        def run_case_logic(SolutionClass, case):
            instance = SolutionClass()
            result = instance.some_method(case.input)
            return result == case.expected
        
        if __name__ == '__main__':
            run_judge_from_file(__file__, TEST_CASES, run_case_logic)
    """
    base_dir = os.path.dirname(os.path.abspath(judge_file_path))
    solutions_dir = os.path.join(base_dir, 'solutions')
    
    solutions = load_classes(
        solutions_dir, "Solution", subfolder=None, file_pattern="solution_*.py"
    )
    
    run_tests(solutions, test_cases, run_case_logic, section_name, report_dir=base_dir)

