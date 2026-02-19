from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TestCase:
    id: str
    operations: List[tuple]  # List of (operation, *args) tuples
    expected_forward: List
    expected_backward: Optional[List] = None  # If None, should be reverse of forward
    search_results: Optional[List[tuple]] = None  # List of (value, expected_bool)


TEST_CASES = [
    TestCase(
        id="basic_insert_and_traverse",
        operations=[
            ("insert", "Mercury"),
            ("insert", "Venus"),
            ("insert", "Earth"),
        ],
        expected_forward=["Mercury", "Venus", "Earth"],
        expected_backward=["Earth", "Venus", "Mercury"],
        search_results=[("Mercury", True), ("Earth", True), ("Mars", False)],
    ),
    TestCase(
        id="jupiter_removal",
        operations=[
            ("insert", "Mercury"),
            ("insert", "Venus"),
            ("insert", "Earth"),
            ("insert", "Jupiter"),
            ("insert", "Saturn"),
            ("delete", "Jupiter"),
        ],
        expected_forward=["Mercury", "Venus", "Earth", "Saturn"],
        expected_backward=["Saturn", "Earth", "Venus", "Mercury"],
        search_results=[("Jupiter", False), ("Saturn", True), ("Earth", True)],
    ),
    TestCase(
        id="single_element",
        operations=[
            ("insert", 42),
        ],
        expected_forward=[42],
        expected_backward=[42],
        search_results=[(42, True), (99, False)],
    ),
    TestCase(
        id="empty_list",
        operations=[],
        expected_forward=[],
        expected_backward=[],
        search_results=[(1, False)],
    ),
    TestCase(
        id="delete_head",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("delete", 1),
        ],
        expected_forward=[2, 3],
        expected_backward=[3, 2],
    ),
    TestCase(
        id="delete_tail",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("delete", 3),
        ],
        expected_forward=[1, 2],
        expected_backward=[2, 1],
    ),
    TestCase(
        id="delete_middle",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("delete", 2),
        ],
        expected_forward=[1, 3],
        expected_backward=[3, 1],
    ),
    TestCase(
        id="delete_nonexistent",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("delete", 99),
        ],
        expected_forward=[1, 2],
        expected_backward=[2, 1],
    ),
    TestCase(
        id="delete_single_node",
        operations=[
            ("insert", 100),
            ("delete", 100),
        ],
        expected_forward=[],
        expected_backward=[],
    ),
    TestCase(
        id="multiple_deletions",
        operations=[
            ("insert", "A"),
            ("insert", "B"),
            ("insert", "C"),
            ("insert", "D"),
            ("insert", "E"),
            ("delete", "B"),
            ("delete", "D"),
        ],
        expected_forward=["A", "C", "E"],
        expected_backward=["E", "C", "A"],
    ),
    TestCase(
        id="duplicate_values_delete_first",
        operations=[
            ("insert", 5),
            ("insert", 5),
            ("insert", 5),
            ("delete", 5),
        ],
        expected_forward=[5, 5],
        expected_backward=[5, 5],
    ),
    TestCase(
        id="complex_scenario",
        operations=[
            ("insert", 10),
            ("insert", 20),
            ("insert", 30),
            ("insert", 40),
            ("delete", 20),
            ("insert", 25),
            ("delete", 40),
            ("insert", 45),
        ],
        expected_forward=[10, 30, 25, 45],
        expected_backward=[45, 25, 30, 10],
    ),
]
