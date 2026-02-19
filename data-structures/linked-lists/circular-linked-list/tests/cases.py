from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TestCase:
    id: str
    operations: List[tuple]  # List of (operation, *args) tuples
    expected_list: List[int]
    search_results: Optional[List[tuple]] = None  # List of (value, expected_bool)


TEST_CASES = [
    TestCase(
        id="basic_insert",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
        ],
        expected_list=[1, 2, 3],
        search_results=[(1, True), (2, True), (3, True), (4, False)],
    ),
    TestCase(
        id="single_element",
        operations=[
            ("insert", 42),
        ],
        expected_list=[42],
        search_results=[(42, True), (99, False)],
    ),
    TestCase(
        id="empty_list",
        operations=[],
        expected_list=[],
        search_results=[(1, False), (0, False)],
    ),
    TestCase(
        id="insert_and_delete_from_end",
        operations=[
            ("insert", 10),
            ("insert", 20),
            ("insert", 30),
            ("delete", 30),
        ],
        expected_list=[10, 20],
        search_results=[(10, True), (20, True), (30, False)],
    ),
    TestCase(
        id="delete_from_middle",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("delete", 2),
        ],
        expected_list=[1, 3],
        search_results=[(1, True), (2, False), (3, True)],
    ),
    TestCase(
        id="delete_head",
        operations=[
            ("insert", 5),
            ("insert", 10),
            ("insert", 15),
            ("delete", 5),
        ],
        expected_list=[10, 15],
        search_results=[(5, False), (10, True), (15, True)],
    ),
    TestCase(
        id="delete_nonexistent",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("delete", 99),
        ],
        expected_list=[1, 2],
        search_results=[(1, True), (2, True), (99, False)],
    ),
    TestCase(
        id="delete_single_node",
        operations=[
            ("insert", 99),
            ("delete", 99),
        ],
        expected_list=[],
        search_results=[(99, False)],
    ),
    TestCase(
        id="duplicate_values",
        operations=[
            ("insert", 5),
            ("insert", 5),
            ("insert", 5),
            ("delete", 5),  # Delete first occurrence only
        ],
        expected_list=[5, 5],
        search_results=[(5, True)],
    ),
    TestCase(
        id="multiple_operations",
        operations=[
            ("insert", 100),
            ("insert", 200),
            ("insert", 150),
            ("delete", 200),
            ("insert", 175),
            ("delete", 100),
        ],
        expected_list=[150, 175],
        search_results=[(100, False), (150, True), (175, True), (200, False)],
    ),
]
