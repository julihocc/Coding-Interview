from dataclasses import dataclass
from typing import Optional


class TreeNode:
    """A node in the fruit tree (non-binary, multi-way)."""
    def __init__(self, value: str):
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child_node: "TreeNode") -> None:
        self.children.append(child_node)

    def remove_child(self, child_node: "TreeNode") -> None:
        self.children = [c for c in self.children if c is not child_node]


def _build_initial_tree() -> TreeNode:
    """Build the initial fruit tree from the lesson starter code.

    Structure (before Plum insertion):
        Apple
        ├── Banana
        │   ├── Date
        │   └── Elderberry
        └── Cherry
            ├── Pear
            └── Grape
    """
    tree_root = TreeNode("Apple")

    root_left = TreeNode("Banana")
    root_right = TreeNode("Cherry")
    tree_root.add_child(root_left)
    tree_root.add_child(root_right)

    root_left.add_child(TreeNode("Date"))
    root_left.add_child(TreeNode("Elderberry"))

    root_right.add_child(TreeNode("Pear"))
    root_right.add_child(TreeNode("Grape"))

    return tree_root


def _build_pear_already_has_child() -> TreeNode:
    """Pear already has 'Mango' as a child — Plum should be appended after it.

    Pre-order after inserting Plum under Pear:
    [Apple, Pear, Mango, Plum]
    """
    root = TreeNode("Apple")
    pear = TreeNode("Pear")
    pear.add_child(TreeNode("Mango"))
    root.add_child(pear)
    return root


@dataclass
class TestCase:
    id: str
    root: Optional[TreeNode]
    expected: list


TEST_CASES = [
    TestCase(
        id="lesson_full_fruit_tree",
        root=_build_initial_tree(),
        expected=[
            "Apple",
            "Banana",
            "Date",
            "Elderberry",
            "Cherry",
            "Pear",
            "Plum",
            "Grape",
        ],
    ),
    TestCase(
        id="empty_tree",
        root=None,
        expected=[],
    ),
    TestCase(
        id="single_node_no_pear",
        root=TreeNode("Apple"),
        expected=["Apple"],
    ),
    TestCase(
        id="pear_already_has_child",
        root=_build_pear_already_has_child(),
        expected=["Apple", "Pear", "Mango", "Plum"],
    ),
]
