#!/usr/bin/env python3
"""
Reorganize solutions folders to have reference/ and contributed/ subfolders.
Moves naive.py and optimized.py to reference/, creates contributed/ folder.
"""

import os
import shutil

def reorganize_problem(problem_dir):
    """Reorganize a single problem's solutions folder."""
    solutions_dir = os.path.join(problem_dir, 'solutions')
    
    if not os.path.exists(solutions_dir):
        print(f"  ⚠️  No solutions folder in {problem_dir}")
        return False
    
    reference_dir = os.path.join(solutions_dir, 'reference')
    contributed_dir = os.path.join(solutions_dir, 'contributed')
    
    # Create reference directory if it doesn't exist
    if not os.path.exists(reference_dir):
        os.makedirs(reference_dir)
        print("  ✓ Created reference/")
    
    # Create contributed directory if it doesn't exist
    if not os.path.exists(contributed_dir):
        os.makedirs(contributed_dir)
        print("  ✓ Created contributed/")
    
    # Move naive.py and optimized.py to reference/
    for filename in ['naive.py', 'optimized.py']:
        src = os.path.join(solutions_dir, filename)
        dst = os.path.join(reference_dir, filename)
        
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.move(src, dst)
            print(f"  ✓ Moved {filename} -> reference/")
        elif os.path.exists(dst):
            print(f"  ✓ {filename} already in reference/")
    
    # Keep template.py, __init__.py at solutions root (don't move)
    print("  ✓ template.py and __init__.py stay at root")
    
    return True

def main():
    """Find all problem directories and reorganize them."""
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Find all problem directories (look for judge.py)
    problem_dirs = []
    for root, dirs, files in os.walk(repo_root):
        if 'judge.py' in files and 'solutions' in dirs:
            problem_dirs.append(root)
    
    if not problem_dirs:
        print("No problem directories found!")
        return
    
    print(f"Found {len(problem_dirs)} problems to reorganize:\n")
    
    for problem_dir in sorted(problem_dirs):
        relative_path = os.path.relpath(problem_dir, repo_root)
        print(f"{relative_path}")
        reorganize_problem(problem_dir)
    
    print("\n✅ Reorganization complete!")

if __name__ == '__main__':
    main()
