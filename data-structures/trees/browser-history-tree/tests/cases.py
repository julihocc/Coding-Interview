from dataclasses import dataclass
from typing import Optional


class TreeNode:
    """A node in the browser history tree (non-binary, multi-way)."""
    def __init__(self, value: str):
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child_node: "TreeNode") -> None:
        self.children.append(child_node)

    def remove_child(self, child_node: "TreeNode") -> None:
        self.children = [c for c in self.children if c is not child_node]


def _build_lesson_tree() -> TreeNode:
    """Build the full browser history tree from the lesson material.

    Structure:
        Start
        └── Google.com
            ├── CodeSignal.com
            │   ├── CodeSignal.com/Tour
            │   └── CodeSignal.com/Blog
            └── Gmail.com

    Pre-order: [Start, Google.com, CodeSignal.com,
                CodeSignal.com/Tour, CodeSignal.com/Blog, Gmail.com]
    """
    browser_history_root = TreeNode("Start")
    google = TreeNode("Google.com")
    browser_history_root.add_child(google)

    codesignal = TreeNode("CodeSignal.com")
    google.add_child(codesignal)

    gmail = TreeNode("Gmail.com")
    google.add_child(gmail)

    codesignal_tour = TreeNode("CodeSignal.com/Tour")
    codesignal_blog = TreeNode("CodeSignal.com/Blog")
    codesignal.add_child(codesignal_tour)
    codesignal.add_child(codesignal_blog)

    return browser_history_root


def _build_chain() -> TreeNode:
    """A → B → C (each page leads to exactly one next page).
    Pre-order: [A, B, C]
    """
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    a.add_child(b)
    b.add_child(c)
    return a


def _build_flat_tree() -> TreeNode:
    """Root directly links to four pages (no grandchildren).
    Pre-order: [Home, Page1, Page2, Page3, Page4]
    """
    root = TreeNode("Home")
    for i in range(1, 5):
        root.add_child(TreeNode(f"Page{i}"))
    return root


@dataclass
class TestCase:
    id: str
    root: Optional[TreeNode]
    expected: list


TEST_CASES = [
    TestCase(
        id="lesson_full_browser_history",
        root=_build_lesson_tree(),
        expected=[
            "Start",
            "Google.com",
            "CodeSignal.com",
            "CodeSignal.com/Tour",
            "CodeSignal.com/Blog",
            "Gmail.com",
        ],
    ),
    TestCase(
        id="empty_tree",
        root=None,
        expected=[],
    ),
    TestCase(
        id="single_page",
        root=TreeNode("Google.com"),
        expected=["Google.com"],
    ),
    TestCase(
        id="linear_chain",
        root=_build_chain(),
        expected=["A", "B", "C"],
    ),
    TestCase(
        id="flat_tree_no_grandchildren",
        root=_build_flat_tree(),
        expected=["Home", "Page1", "Page2", "Page3", "Page4"],
    ),
]
