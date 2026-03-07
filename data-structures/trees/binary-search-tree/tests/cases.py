from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    inserts: List[int]
    searches: List[int]
    deletes: List[int]
    expected_searches: List[bool]
    expected_inorder_after: List[int]
    name: str = "Test Case"


# Define standard cases based on common BST shapes and operations
cases = [
    TestCase(
        name="Basic Complete Tree Insert and Delete",
        inserts=[5, 3, 9, 1, 4, 6],
        searches=[4, 7],  # Should find 4, shouldn't find 7
        deletes=[3],  # Delete node with two children
        expected_searches=[True, False],
        expected_inorder_after=[1, 4, 5, 6, 9],
    ),
    TestCase(
        name="Skewed Left Tree",
        inserts=[5, 4, 3, 2, 1],
        searches=[1, 6],
        deletes=[5],  # Delete the root
        expected_searches=[True, False],
        expected_inorder_after=[1, 2, 3, 4],
    ),
    TestCase(
        name="Single Node Operations",
        inserts=[10],
        searches=[10, 5],
        deletes=[10],  # Delete the only node
        expected_searches=[True, False],
        expected_inorder_after=[],
    ),
    TestCase(
        name="Delete Leaf Nodes",
        inserts=[10, 5, 15],
        searches=[15, 20],
        deletes=[5, 15],  # Delete both leaf nodes
        expected_searches=[True, False],
        expected_inorder_after=[10],
    ),
    TestCase(
        name="Large Unbalanced Insertions",
        inserts=[50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85],
        searches=[25, 100, 50],
        deletes=[50, 20, 85],  # Delete root, internal with children, and leaf
        expected_searches=[True, False, True],
        expected_inorder_after=[10, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80],
    ),
]
