from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TestCase:
    id: str
    operations: List[tuple]       # ("insert"/"delete", value) tuples
    expected_list: List           # expected to_list() result after all ops
    expected_size: int            # expected size after all ops


TEST_CASES = [
    # ── core scenario from the problem statement ─────────────────────────────
    TestCase(
        id="problem_scenario",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("delete", 2),
            ("delete", 5),   # non-existent – size must not change
        ],
        expected_list=[1, 3],
        expected_size=2,
    ),

    # ── size after inserts only ───────────────────────────────────────────────
    TestCase(
        id="size_after_inserts",
        operations=[
            ("insert", 10),
            ("insert", 20),
            ("insert", 30),
        ],
        expected_list=[10, 20, 30],
        expected_size=3,
    ),

    # ── empty list ────────────────────────────────────────────────────────────
    TestCase(
        id="empty_list",
        operations=[],
        expected_list=[],
        expected_size=0,
    ),

    # ── delete from empty list ────────────────────────────────────────────────
    TestCase(
        id="delete_from_empty",
        operations=[
            ("delete", 99),
        ],
        expected_list=[],
        expected_size=0,
    ),

    # ── delete head ───────────────────────────────────────────────────────────
    TestCase(
        id="delete_head",
        operations=[
            ("insert", "A"),
            ("insert", "B"),
            ("insert", "C"),
            ("delete", "A"),
        ],
        expected_list=["B", "C"],
        expected_size=2,
    ),

    # ── delete tail ───────────────────────────────────────────────────────────
    TestCase(
        id="delete_tail",
        operations=[
            ("insert", "A"),
            ("insert", "B"),
            ("insert", "C"),
            ("delete", "C"),
        ],
        expected_list=["A", "B"],
        expected_size=2,
    ),

    # ── delete middle ─────────────────────────────────────────────────────────
    TestCase(
        id="delete_middle",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("delete", 2),
        ],
        expected_list=[1, 3],
        expected_size=2,
    ),

    # ── delete non-existent – size must stay the same ─────────────────────────
    TestCase(
        id="delete_nonexistent",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("delete", 99),
        ],
        expected_list=[1, 2],
        expected_size=2,
    ),

    # ── delete the only element → empty list ─────────────────────────────────
    TestCase(
        id="delete_only_element",
        operations=[
            ("insert", 42),
            ("delete", 42),
        ],
        expected_list=[],
        expected_size=0,
    ),

    # ── multiple deletions reduce size correctly ──────────────────────────────
    TestCase(
        id="multiple_deletions",
        operations=[
            ("insert", 1),
            ("insert", 2),
            ("insert", 3),
            ("insert", 4),
            ("insert", 5),
            ("delete", 2),
            ("delete", 4),
        ],
        expected_list=[1, 3, 5],
        expected_size=3,
    ),
]
