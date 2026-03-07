import sys
import os

# Add parent directory to path to allow importing solutions and tests
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from solutions.solution_optimized import is_balanced, kthSmallest, TreeNode
    from tests.cases import BALANCE_TEST_CASES, KTH_TEST_CASES, build_tree
except ImportError as e:
    print(f"Error importing required files: {e}")
    sys.exit(1)


def run_tests():
    print("--- Testing Problem 1: is_balanced ---")
    balance_passed = 0
    balance_total = len(BALANCE_TEST_CASES)

    for idx, test_case in enumerate(BALANCE_TEST_CASES):
        tree_list = test_case["tree"]
        expected = test_case["expected"]
        name = test_case.get("name", f"Test {idx + 1}")

        # Build the tree using the helper function
        # Since build_tree expects values, we handle None correctly.
        try:
            root = None
            if len(tree_list) > 0:
                # Basic build_tree adaptation for complete level-order without Nones
                # Actually, our helper handles None.
                root = build_tree(tree_list)

            result = is_balanced(root)

            if result == expected:
                print(f"✅ {name}: Passed")
                balance_passed += 1
            else:
                print(f"❌ {name}: Failed")
                print(f"   Expected: {expected}")
                print(f"   Got:      {result}")
        except Exception as e:
            print(f"❌ {name}: Failed with error - {e}")

    print(f"\nProblem 1 Results: {balance_passed}/{balance_total} tests passed.\n")

    print("--- Testing Problem 2: kthSmallest ---")
    kth_passed = 0
    kth_total = len(KTH_TEST_CASES)

    for idx, test_case in enumerate(KTH_TEST_CASES):
        tree_list = test_case["tree"]
        k = test_case["k"]
        expected = test_case["expected"]
        name = test_case.get("name", f"Test {idx + 1}")

        try:
            root = None
            if len(tree_list) > 0:
                root = build_tree(tree_list)

            result = kthSmallest(root, k)

            if result == expected:
                print(f"✅ {name}: Passed")
                kth_passed += 1
            else:
                print(f"❌ {name}: Failed")
                print(f"   Expected: {expected}")
                print(f"   Got:      {result}")
        except Exception as e:
            print(f"❌ {name}: Failed with error - {e}")

    print(f"\nProblem 2 Results: {kth_passed}/{kth_total} tests passed.\n")

    if balance_passed == balance_total and kth_passed == kth_total:
        print("🎉 All tests passed successfully!")
        return 0
    else:
        print("⚠️ Some tests failed. Please review your implementation.")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
