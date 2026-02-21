from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    input_values: List   # values pushed (prepended) in order
    expected_length: int  # expected LinkedList_length() result


TEST_CASES = [
    # ── empty list ────────────────────────────────────────────────────────────
    TestCase(
        id="empty_list",
        input_values=[],
        expected_length=0,
    ),

    # ── single element ────────────────────────────────────────────────────────
    TestCase(
        id="single_element",
        input_values=["Alice"],
        expected_length=1,
    ),

    # ── two elements ─────────────────────────────────────────────────────────
    TestCase(
        id="two_elements",
        input_values=["Alice", "Bob"],
        expected_length=2,
    ),

    # ── call-center scenario ──────────────────────────────────────────────────
    TestCase(
        id="call_center_three_callers",
        input_values=["Alice", "Bob", "Carol"],
        expected_length=3,
    ),

    # ── five integer elements ─────────────────────────────────────────────────
    TestCase(
        id="five_integers",
        input_values=[1, 2, 3, 4, 5],
        expected_length=5,
    ),

    # ── ten elements ──────────────────────────────────────────────────────────
    TestCase(
        id="ten_elements",
        input_values=list(range(10)),
        expected_length=10,
    ),
]
