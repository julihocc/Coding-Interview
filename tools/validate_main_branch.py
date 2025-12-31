import os
import sys

ALLOWED = {"naive.py", "optimized.py", "__init__.py", "hints.py", "template.py"}


def find_disallowed(root: str):
    bad = []
    for dirpath, dirnames, filenames in os.walk(root):
        if os.path.basename(dirpath) == "solutions":
            for fname in filenames:
                if fname.endswith(".py") and fname not in ALLOWED:
                    bad.append(os.path.join(dirpath, fname).replace("\\", "/"))
    return bad


def main():
    root = os.getcwd()
    bad = find_disallowed(root)
    if bad:
        print("Disallowed solution files detected for PR to main:")
        for path in bad:
            print(f" - {path}")
        print("\nOnly allowed in main: naive.py, optimized.py, __init__.py, hints.py, template.py")
        sys.exit(1)
    else:
        print("Branch policy check passed for main.")


if __name__ == "__main__":
    main()
