from dataclasses import dataclass


class Node:
    """A node in a company hierarchy tree."""

    def __init__(self, value: str):
        self.value = value
        self.children: list["Node"] = []


def _build_lesson_tree() -> Node:
    """Build the company hierarchy from the lesson.

    Structure:
        Head Office
        ├── Marketing
        │   ├── SEO
        │   └── Content
        ├── Sales
        │   ├── Domestic
        │   └── International
        └── R&D

    DFS order: Head Office → Marketing → SEO → Content → Sales → Domestic → International → R&D
    """
    root = Node("Head Office")

    marketing = Node("Marketing")
    marketing.children = [Node("SEO"), Node("Content")]

    sales = Node("Sales")
    sales.children = [Node("Domestic"), Node("International")]

    rnd = Node("R&D")

    root.children = [marketing, sales, rnd]
    return root


def _build_single_node() -> Node:
    return Node("CEO")


def _build_chain() -> Node:
    """Head Office -> Sales -> Domestic (linear chain)."""
    root = Node("Head Office")
    sales = Node("Sales")
    domestic = Node("Domestic")
    sales.children.append(domestic)
    root.children.append(sales)
    return root


def _build_wide_tree() -> Node:
    """Head Office with four direct children, no grandchildren."""
    root = Node("Head Office")
    root.children = [Node("HR"), Node("Legal"), Node("Finance"), Node("IT")]
    return root


@dataclass
class TestCase:
    id: str
    root: Node
    expected: list[str]


TEST_CASES = [
    TestCase(
        id="lesson_company_hierarchy",
        root=_build_lesson_tree(),
        expected=[
            "Head Office",
            "Marketing",
            "SEO",
            "Content",
            "Sales",
            "Domestic",
            "International",
            "R&D",
        ],
    ),
    TestCase(
        id="single_node",
        root=_build_single_node(),
        expected=["CEO"],
    ),
    TestCase(
        id="linear_chain",
        root=_build_chain(),
        expected=["Head Office", "Sales", "Domestic"],
    ),
    TestCase(
        id="wide_flat_tree",
        root=_build_wide_tree(),
        expected=["Head Office", "HR", "Legal", "Finance", "IT"],
    ),
]
