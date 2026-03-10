import sys
import os
import time

# Add the repository root to the path so we can import utils
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
)

from utils.judge_utils import load_classes_with_method, run_tests


def run_test_case(solution_class, case) -> bool:
    """
    Runs a single test case for a given solution class.

    Returns:
        bool: True if test passed, False otherwise.
    """
    # Create an instance with the users and edges
    instance = solution_class(case.users, list(case.edges))

    # Execute the method
    result = instance.find_recommendations()

    if result == case.expected:
        return True
    else:
        raise AssertionError(f"Expected {case.expected}, got {result}")


def main():
    # Load test cases
    try:
        from tests.cases import TEST_CASES
    except ImportError:
        print("Error: Could not import TEST_CASES from tests.cases")
        sys.exit(1)

    problem_dir = os.path.dirname(os.path.abspath(__file__))

    # Load reference solutions
    reference_solutions = load_classes_with_method(
        os.path.join(problem_dir, "solutions"),
        "find_recommendations",
        subfolder="",  # No subfolder used
    )

    # Load contributed solutions (if any)
    contributed_solutions = load_classes_with_method(
        os.path.join(problem_dir, "solutions", "contributed"),
        "find_recommendations",
        subfolder="",
    )

    # Run tests and print results
    run_tests(
        reference_solutions,
        TEST_CASES,
        run_test_case,
        section_name="REFERENCE SOLUTIONS",
    )

    if contributed_solutions:
        run_tests(
            contributed_solutions,
            TEST_CASES,
            run_test_case,
            section_name="CONTRIBUTED SOLUTIONS",
        )
    else:
        print("\n=== CONTRIBUTED SOLUTIONS ===")
        print("No solutions found.")


if __name__ == "__main__":
    main()
