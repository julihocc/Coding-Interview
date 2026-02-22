from dataclasses import dataclass


@dataclass
class TestCase:
    id: str
    expected: list


# The solution must build exactly this balanced BST:
#
#         4
#        / \
#       2   6
#      / \ / \
#     1  3 5  7
#
# In-order traversal of a BST yields sorted order.

TEST_CASES = [
    TestCase(
        id="balanced_bst_in_order",
        expected=[1, 2, 3, 4, 5, 6, 7],
    ),
]
