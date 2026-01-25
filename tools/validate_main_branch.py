import os
import sys

# Allowed files in solutions/ folder
SOLUTIONS_DIRECT_ALLOWED = {
    "solution_naive.py", 
    "solution_optimized.py", 
    "solution_template.py",
    "__init__.py"
}

# Allowed files in reference/ folder (Legacy pattern)
REFERENCE_ALLOWED = {"naive.py", "optimized.py", "__init__.py"}

# Allowed files at solutions/ root (Legacy pattern)
SOLUTIONS_ROOT_LEGACY_ALLOWED = {"__init__.py", "template.py"}


def find_disallowed(root: str):
    """Check for disallowed files in solutions folder structure."""
    bad = []
    for dirpath, dirnames, filenames in os.walk(root):
        if os.path.basename(dirpath) == "solutions":
            # Check files at solutions root
            # We support two patterns:
            # 1. New: solution_naive.py, etc.
            # 2. Legacy: template.py, then reference/ subfolder
            
            for fname in filenames:
                if fname.endswith(".py"):
                    is_new_valid = fname in SOLUTIONS_DIRECT_ALLOWED
                    is_legacy_valid = fname in SOLUTIONS_ROOT_LEGACY_ALLOWED
                    
                    if not (is_new_valid or is_legacy_valid):
                        bad.append(os.path.join(dirpath, fname).replace("\\", "/"))
            
            # Subdirectories: allow reference (legacy) and __pycache__
            # disallowed_dirs = [d for d in dirnames if d not in ("reference", "__pycache__", "contributed")]
            # strict check:
            for dirname in dirnames:
                if dirname not in ("reference", "__pycache__", "contributed"):
                     bad.append(os.path.join(dirpath, dirname).replace("\\", "/"))

        elif os.path.basename(dirpath) == "reference":
            # Check files in reference/ subfolder
            for fname in filenames:
                if fname.endswith(".py") and fname not in REFERENCE_ALLOWED:
                    bad.append(os.path.join(dirpath, fname).replace("\\", "/"))
    
    return bad


def main():
    root = os.getcwd()
    bad = find_disallowed(root)
    if bad:
        print("Disallowed solution files detected for PR to main:")
        for path in bad:
            print(f" - {path}")
        print("\nAllowed structure:")
        print("  solutions/")
        print("    __init__.py")
        print("    solution_template.py (New Pattern)")
        print("    solution_naive.py")
        print("    solution_optimized.py")
        print("    OR (Legacy Pattern)")
        print("    template.py")
        print("    reference/")
        print("      naive.py")
        print("      optimized.py")
        sys.exit(1)
    else:
        print("Branch policy check passed for main.")


if __name__ == "__main__":
    main()
