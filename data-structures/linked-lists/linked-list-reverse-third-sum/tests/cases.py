from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    input_values: List   # list values head→tail; [] means empty list
    expected_sum: int    # expected find_sum() result


TEST_CASES = [
    # ── empty list ────────────────────────────────────────────────────────────
    TestCase(
        id="empty_list",
        input_values=[],
        expected_sum=0,
    ),

    # ── fewer than 3 elements ─────────────────────────────────────────────────
    TestCase(
        id="one_element",
        input_values=[42],
        expected_sum=0,
    ),
    TestCase(
        id="two_elements",
        input_values=[10, 20],
        expected_sum=0,
    ),

    # ── exactly 3 elements ───────────────────────────────────────────────────
    # reversed: 3, 2, 1  → position 3 = 1
    TestCase(
        id="three_elements",
        input_values=[1, 2, 3],
        expected_sum=1,
    ),

    # ── cosmo example: 9 elements ────────────────────────────────────────────
    # list:     1→2→3→4→5→6→7→8→9
    # reversed: 9 8 7 6 5 4 3 2 1
    # pos 3→7, pos 6→4, pos 9→1  sum=12
    TestCase(
        id="nine_elements",
        input_values=[1, 2, 3, 4, 5, 6, 7, 8, 9],
        expected_sum=12,
    ),

    # ── 6 elements ───────────────────────────────────────────────────────────
    # list:     1→2→3→4→5→6
    # reversed: 6 5 4 3 2 1
    # pos 3→4, pos 6→1  sum=5
    TestCase(
        id="six_elements",
        input_values=[1, 2, 3, 4, 5, 6],
        expected_sum=5,
    ),

    # ── 5 elements (last 3rd pos is 3, next would be 6 but only 5 elements) ──
    # list:     10→20→30→40→50
    # reversed: 50 40 30 20 10
    # pos 3→30  sum=30
    TestCase(
        id="five_elements",
        input_values=[10, 20, 30, 40, 50],
        expected_sum=30,
    ),

    # ── negative numbers ─────────────────────────────────────────────────────
    # list:     -1→-2→-3→-4→-5→-6
    # reversed: -6 -5 -4 -3 -2 -1
    # pos 3→-4, pos 6→-1  sum=-5
    TestCase(
        id="negative_numbers",
        input_values=[-1, -2, -3, -4, -5, -6],
        expected_sum=-5,
    ),
]
