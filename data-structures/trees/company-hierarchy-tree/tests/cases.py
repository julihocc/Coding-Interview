from dataclasses import dataclass
from typing import Optional


class TreeNode:
    """A node in the company hierarchy tree (non-binary, multi-way)."""
    def __init__(self, value: str):
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child_node: "TreeNode") -> None:
        self.children.append(child_node)

    def remove_child(self, child_node: "TreeNode") -> None:
        self.children = [c for c in self.children if c is not child_node]


def _build_initial_tree() -> TreeNode:
    """Build the INITIAL company hierarchy from the lesson starter code.

    Structure (before restructuring):
        CEO
        ├── VP Marketing
        │   └── Director Marketing
        ├── VP Finance
        └── VP Engineering
            └── Engineer
    """
    company_hierarchy_root = TreeNode("CEO")

    vp_marketing = TreeNode("VP Marketing")
    vp_finance = TreeNode("VP Finance")
    vp_engineering = TreeNode("VP Engineering")

    company_hierarchy_root.add_child(vp_marketing)
    company_hierarchy_root.add_child(vp_finance)
    company_hierarchy_root.add_child(vp_engineering)

    director_marketing = TreeNode("Director Marketing")
    vp_marketing.add_child(director_marketing)

    engineer = TreeNode("Engineer")
    vp_engineering.add_child(engineer)

    return company_hierarchy_root


def _build_already_flat_tree() -> TreeNode:
    """A mini org with only a root CEO (no children).
    After restructuring (no-op): ["CEO"]
    """
    return TreeNode("CEO")


def _build_single_vp_tree() -> TreeNode:
    """CEO → VP Engineering → Engineer (no other VPs).
    After restructuring:
        CEO
        └── VP Engineering
            ├── Senior Engineer
            │   └── Engineer
            └── Product Manager
    Pre-order: [CEO, VP Engineering, Senior Engineer, Engineer, Product Manager]
    """
    root = TreeNode("CEO")
    vp_eng = TreeNode("VP Engineering")
    engineer = TreeNode("Engineer")
    root.add_child(vp_eng)
    vp_eng.add_child(engineer)
    return root


@dataclass
class TestCase:
    id: str
    root: Optional[TreeNode]
    expected: list


TEST_CASES = [
    TestCase(
        id="lesson_full_restructure",
        root=_build_initial_tree(),
        expected=[
            "CEO",
            "VP Marketing",
            "Director Marketing",
            "VP Finance",
            "VP Engineering",
            "Senior Engineer",
            "Engineer",
            "Product Manager",
        ],
    ),
    TestCase(
        id="empty_tree",
        root=None,
        expected=[],
    ),
    TestCase(
        id="only_vp_engineering_and_engineer",
        root=_build_single_vp_tree(),
        expected=[
            "CEO",
            "VP Engineering",
            "Senior Engineer",
            "Engineer",
            "Product Manager",
        ],
    ),
]
