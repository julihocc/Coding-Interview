from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    operations: List[tuple]       # List of ("insert"/"delete", value) tuples
    expected_backward: List       # Expected tail-to-head traversal after all ops


TEST_CASES = [
    # ── core scenario from the problem statement ─────────────────────────────
    TestCase(
        id="jupiter_removal_backward",
        operations=[
            ("insert", "Mars"),
            ("insert", "Jupiter"),
            ("insert", "Saturn"),
            ("delete", "Jupiter"),
        ],
        expected_backward=["Saturn", "Mars"],
    ),

    # ── basic insert, no deletions ────────────────────────────────────────────
    TestCase(
        id="three_planets_backward",
        operations=[
            ("insert", "Mercury"),
            ("insert", "Venus"),
            ("insert", "Earth"),
        ],
        expected_backward=["Earth", "Venus", "Mercury"],
    ),

    # ── empty list ────────────────────────────────────────────────────────────
    TestCase(
        id="empty_list",
        operations=[],
        expected_backward=[],
    ),

    # ── single element ────────────────────────────────────────────────────────
    TestCase(
        id="single_element",
        operations=[
            ("insert", "Pluto"),
        ],
        expected_backward=["Pluto"],
    ),

    # ── delete head node ─────────────────────────────────────────────────────
    TestCase(
        id="delete_head",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("delete", 1),
        ],
        expected_backward=[3, 2],
    ),

    # ── delete tail node ─────────────────────────────────────────────────────
    TestCase(
        id="delete_tail",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("delete", 3),
        ],
        expected_backward=[2, 1],
    ),

    # ── delete middle node ───────────────────────────────────────────────────
    TestCase(
        id="delete_middle",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("delete", 2),
        ],
        expected_backward=[3, 1],
    ),

    # ── delete non-existent value (list unchanged) ────────────────────────────
    TestCase(
        id="delete_nonexistent",
        operations=[
            ("insert", "A"),
            ("insert", "B"),
            ("delete", "Z"),
        ],
        expected_backward=["B", "A"],
    ),

    # ── delete sole element → empty ───────────────────────────────────────────
    TestCase(
        id="delete_only_element",
        operations=[
            ("insert", 42),
            ("delete", 42),
        ],
        expected_backward=[],
    ),
]
