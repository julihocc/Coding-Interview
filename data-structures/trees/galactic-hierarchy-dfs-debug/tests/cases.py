from dataclasses import dataclass


class TreeNode:
    """A tree node with DFS as a method — contains the bug intentionally for study."""

    def __init__(self, value: str):
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child_value: str) -> None:
        self.children.append(TreeNode(child_value))

    def depth_first_search(self, result: list | None = None) -> list[str]:
        """Fixed DFS method: delegates to child, not self."""
        if result is None:
            result = []
        result.append(self.value)
        for child in self.children:
            child.depth_first_search(result)  # fixed: child, not self
        return result


def _build_lesson_tree() -> TreeNode:
    """Build the galactic hierarchy from the lesson.

    Structure:
        Root
        ├── Left Child
        │   ├── Left Grandchild
        │   └── Right Grandchild
        └── Right Child

    DFS order: Root → Left Child → Left Grandchild → Right Grandchild → Right Child
    """
    root = TreeNode("Root")
    root.add_child("Left Child")
    root.add_child("Right Child")

    left_child = root.children[0]
    left_child.add_child("Left Grandchild")
    left_child.add_child("Right Grandchild")
    return root


def _build_single_node() -> TreeNode:
    return TreeNode("Milky Way")


def _build_chain() -> TreeNode:
    """Linear chain: Galaxy → Star System → Planet."""
    root = TreeNode("Galaxy")
    root.add_child("Star System")
    root.children[0].add_child("Planet")
    return root


def _build_wide_tree() -> TreeNode:
    """Root with four leaf children, no grandchildren."""
    root = TreeNode("Universe")
    for name in ["Galaxy A", "Galaxy B", "Galaxy C", "Galaxy D"]:
        root.add_child(name)
    return root


@dataclass
class TestCase:
    id: str
    root: TreeNode
    expected: list[str]


TEST_CASES = [
    TestCase(
        id="lesson_galactic_hierarchy",
        root=_build_lesson_tree(),
        expected=[
            "Root",
            "Left Child",
            "Left Grandchild",
            "Right Grandchild",
            "Right Child",
        ],
    ),
    TestCase(
        id="single_node",
        root=_build_single_node(),
        expected=["Milky Way"],
    ),
    TestCase(
        id="linear_chain",
        root=_build_chain(),
        expected=["Galaxy", "Star System", "Planet"],
    ),
    TestCase(
        id="wide_flat_tree",
        root=_build_wide_tree(),
        expected=["Universe", "Galaxy A", "Galaxy B", "Galaxy C", "Galaxy D"],
    ),
]
