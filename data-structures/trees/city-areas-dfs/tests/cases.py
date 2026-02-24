from dataclasses import dataclass


class CityNode:
    """A city area node. Uses 'name' and 'areas' as attribute names."""

    def __init__(self, name: str):
        self.name = name
        self.areas: list["CityNode"] = []

    def add_area(self, area_name: str) -> None:
        self.areas.append(CityNode(area_name))

    def dfs(self, visited: set | None = None, result: list | None = None) -> list[str]:
        """DFS traversal — pre-order, collects names into result."""
        if visited is None:
            visited = set()
        if result is None:
            result = []
        visited.add(self.name)
        result.append(self.name)
        for area in self.areas:
            if area.name not in visited:
                area.dfs(visited, result)
        return result


def _build_city_tree() -> CityNode:
    """Build the city hierarchy from the lesson.

    City Center
    ├── North District
    │   ├── Elm Suburb
    │   └── Oak Suburb
    ├── East District
    │   ├── Pine Suburb
    │   └── Maple Suburb
    └── South District
        └── Cedar Suburb
    """
    city = CityNode("City Center")
    city.add_area("North District")
    city.add_area("East District")
    city.add_area("South District")

    north = city.areas[0]
    north.add_area("Elm Suburb")
    north.add_area("Oak Suburb")

    east = city.areas[1]
    east.add_area("Pine Suburb")
    east.add_area("Maple Suburb")

    south = city.areas[2]
    south.add_area("Cedar Suburb")

    return city


@dataclass
class TestCase:
    id: str
    expected: list[str]


TEST_CASES = [
    TestCase(
        id="city_hierarchy_dfs",
        expected=[
            "City Center",
            "North District",
            "Elm Suburb",
            "Oak Suburb",
            "East District",
            "Pine Suburb",
            "Maple Suburb",
            "South District",
            "Cedar Suburb",
        ],
    ),
]
