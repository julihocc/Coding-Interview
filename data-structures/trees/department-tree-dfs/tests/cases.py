from dataclasses import dataclass


class DepartmentTree:
    """A node in a company department hierarchy.

    Uses 'name' and 'subdepartments' attributes (matching the lesson).
    """

    def __init__(self, name: str):
        self.name = name
        self.subdepartments: list["DepartmentTree"] = []

    def add_subdepartment(self, subdept_name: str) -> None:
        self.subdepartments.append(DepartmentTree(subdept_name))

    def traverse(
        self, visited: set | None = None, result: list | None = None
    ) -> list[str]:
        """DFS traversal — completed version with recursive subdepartment loop."""
        if visited is None:
            visited = set()
        if result is None:
            result = []
        visited.add(self.name)
        result.append(self.name)
        for subdept in self.subdepartments:
            if subdept.name not in visited:
                subdept.traverse(visited, result)
        return result


def _build_lesson_tree() -> DepartmentTree:
    """Build the company hierarchy from the lesson.

    Structure:
        CEO
        ├── CTO
        │   ├── Infrastructure
        │   ├── App Development
        │   └── Security
        ├── CFO
        │   ├── Accounting
        │   └── Investor Relations
        └── COO

    DFS order: CEO → CTO → Infrastructure → App Development → Security
               → CFO → Accounting → Investor Relations → COO
    """
    root = DepartmentTree("CEO")
    root.add_subdepartment("CTO")
    root.add_subdepartment("CFO")
    root.add_subdepartment("COO")

    cto = root.subdepartments[0]
    cto.add_subdepartment("Infrastructure")
    cto.add_subdepartment("App Development")
    cto.add_subdepartment("Security")

    cfo = root.subdepartments[1]
    cfo.add_subdepartment("Accounting")
    cfo.add_subdepartment("Investor Relations")

    return root


def _build_single_node() -> DepartmentTree:
    return DepartmentTree("CEO")


def _build_chain() -> DepartmentTree:
    """CEO → CTO → Infrastructure (linear chain)."""
    root = DepartmentTree("CEO")
    root.add_subdepartment("CTO")
    root.subdepartments[0].add_subdepartment("Infrastructure")
    return root


def _build_wide_tree() -> DepartmentTree:
    """CEO with four direct subdepartments, no sub-subdepartments."""
    root = DepartmentTree("CEO")
    for name in ["HR", "Legal", "Finance", "Operations"]:
        root.add_subdepartment(name)
    return root


@dataclass
class TestCase:
    id: str
    root: DepartmentTree
    expected: list[str]


TEST_CASES = [
    TestCase(
        id="lesson_company_hierarchy",
        root=_build_lesson_tree(),
        expected=[
            "CEO",
            "CTO",
            "Infrastructure",
            "App Development",
            "Security",
            "CFO",
            "Accounting",
            "Investor Relations",
            "COO",
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
        expected=["CEO", "CTO", "Infrastructure"],
    ),
    TestCase(
        id="wide_flat_tree",
        root=_build_wide_tree(),
        expected=["CEO", "HR", "Legal", "Finance", "Operations"],
    ),
]
