#!/usr/bin/env python3
"""
Update all judge.py files to load from reference/ and contributed/ subfolders.
"""

import os
import re
from pathlib import Path

def update_judge_file(judge_path, is_class_based):
    """Update a judge.py file to use new structure."""
    with open(judge_path, 'r') as f:
        content = f.read()
    
    # Determine the load function and class/function name
    if is_class_based:
        # Extract class name from load_classes call
        match = re.search(r"load_classes\(solutions_dir, '(\w+)'\)", content)
        if not match:
            print(f"  ⚠️  Could not find load_classes call in {judge_path}")
            return False
        
        entity_name = match.group(1)
        load_func = 'load_classes'
    else:
        # Extract function name from load_solutions call
        match = re.search(r"load_solutions\(solutions_dir, '(\w+)'\)", content)
        if not match:
            print(f"  ⚠️  Could not find load_solutions call in {judge_path}")
            return False
        
        entity_name = match.group(1)
        load_func = 'load_solutions'
    
    # Build new main function that loads from reference then contributed
    new_main = f"""def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')

    # Load and test reference solutions
    reference_solutions = {load_func}(solutions_dir, '{entity_name}', 'reference')
    run_tests(reference_solutions, TEST_CASES, run_case_logic, 'REFERENCE SOLUTIONS')
    
    # Load and test contributed solutions
    contributed_solutions = {load_func}(solutions_dir, '{entity_name}', 'contributed')
    run_tests(contributed_solutions, TEST_CASES, run_case_logic, 'CONTRIBUTED SOLUTIONS')
"""
    
    # Replace the old main function
    old_main_pattern = r"def main\(\):[\s\S]*?(?=\nif __name__|$)"
    new_content = re.sub(old_main_pattern, new_main.rstrip(), content)
    
    with open(judge_path, 'w') as f:
        f.write(new_content)
    
    return True

def main():
    """Find and update all judge.py files."""
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    judge_files = []
    for root, dirs, files in os.walk(repo_root):
        if 'judge.py' in files:
            judge_files.append(os.path.join(root, 'judge.py'))
    
    if not judge_files:
        print("No judge files found!")
        return
    
    print(f"Found {len(judge_files)} judge files to update:\n")
    
    for judge_path in sorted(judge_files):
        relative_path = os.path.relpath(judge_path, repo_root)
        print(f"{relative_path}")
        
        # Determine if class-based or function-based
        with open(judge_path, 'r') as f:
            content = f.read()
        
        is_class_based = 'load_classes' in content
        
        if update_judge_file(judge_path, is_class_based):
            print(f"  ✓ Updated")
        else:
            print(f"  ⚠️  Failed to update")
    
    print(f"\n✅ Judge files updated!")

if __name__ == '__main__':
    main()
