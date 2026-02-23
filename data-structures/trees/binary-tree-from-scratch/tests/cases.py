from dataclasses import dataclass


@dataclass
class TestCase:
    id: str
    traversal: str   # name of Solution method to call
    expected: list


# The canonical balanced BST used in every case:
#
#         4
#        / \
#       2   6
#      / \ / \
#     1  3 5  7
#
# ┌─────────────┬──────────────────────────┬──────────────────────┐
# │  Traversal  │  Visit Order             │  Output              │
# ├─────────────┼──────────────────────────┼──────────────────────┤
# │  In-order   │  Left → Root → Right     │  [1,2,3,4,5,6,7]    │
# │  Pre-order  │  Root → Left → Right     │  [4,2,1,3,6,5,7]    │
# │  Post-order │  Left → Right → Root     │  [1,3,2,5,7,6,4]    │
# └─────────────┴──────────────────────────┴──────────────────────┘

TEST_CASES = [
    TestCase(
        id="in_order_balanced_bst",
        traversal="build_and_inorder",
        expected=[1, 2, 3, 4, 5, 6, 7],
    ),
    TestCase(
        id="pre_order_balanced_bst",
        traversal="build_and_preorder",
        expected=[4, 2, 1, 3, 6, 5, 7],
    ),
    TestCase(
        id="post_order_balanced_bst",
        traversal="build_and_postorder",
        expected=[1, 3, 2, 5, 7, 6, 4],
    ),
]
