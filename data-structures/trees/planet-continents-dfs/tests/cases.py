from dataclasses import dataclass


class Node:
    """A node in the planet hierarchy tree.

    DFS is implemented as a method on the node, following the lesson pattern.
    """

    def __init__(self, value: str):
        self.value = value
        self.children: list["Node"] = []

    def add_child(self, child_value: str) -> None:
        self.children.append(Node(child_value))

    def depth_first_search(
        self, visited: set | None = None, result: list | None = None
    ):
        """Perform DFS from this node, collecting visited values into result."""
        if visited is None:
            visited = set()
        if result is None:
            result = []
        visited.add(self.value)
        result.append(self.value)
        for child in self.children:
            if child.value not in visited:
                child.depth_first_search(visited, result)
        return result


def _build_starter_tree() -> Node:
    """Build the starter tree from the lesson (Africa + Asia, 2 countries each)."""
    root = Node("Earth")
    root.add_child("Africa")
    root.add_child("Asia")

    africa = root.children[0]
    africa.add_child("Nigeria")
    africa.add_child("South Africa")

    asia = root.children[1]
    asia.add_child("China")
    asia.add_child("India")
    return root


def _build_single_continent() -> Node:
    """Earth with only Europe and two countries."""
    root = Node("Earth")
    root.add_child("Europe")
    europe = root.children[0]
    europe.add_child("France")
    europe.add_child("Germany")
    return root


@dataclass
class TestCase:
    id: str
    root: Node
    expected: list[str]


TEST_CASES = [
    TestCase(
        id="lesson_tree_extended",
        root=_build_starter_tree(),
        expected=[
            "Earth",
            "Africa",
            "Nigeria",
            "South Africa",
            "Egypt",
            "Kenya",
            "Asia",
            "China",
            "India",
            "Japan",
            "South Korea",
        ],
    ),
    TestCase(
        id="single_continent_no_additions",
        root=_build_single_continent(),
        expected=[
            "Earth",
            "Europe",
            "France",
            "Germany",
        ],
    ),
]
