import os
import sys

# Allowed files in reference/ folder
REFERENCE_ALLOWED = {"naive.py", "optimized.py", "__init__.py"}

# Allowed files at solutions/ root
SOLUTIONS_ROOT_ALLOWED = {"__init__.py", "template.py"}


def find_disallowed(root: str):
    """Check for disallowed files in solutions folder structure."""
    bad = []
    for dirpath, dirnames, filenames in os.walk(root):
        if os.path.basename(dirpath) == "solutions":
            # Check files at solutions root
            for fname in filenames:
                if fname.endswith(".py") and fname not in SOLUTIONS_ROOT_ALLOWED:
                    bad.append(os.path.join(dirpath, fname).replace("\\", "/"))
        
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
        print("    template.py")
        print("    reference/")
        print("      naive.py")
        print("      optimized.py")
        print("      __init__.py")
        print("    contributed/")
        print("      (user submissions)")
        sys.exit(1)
    else:
        print("Branch policy check passed for main.")


if __name__ == "__main__":
    main()
