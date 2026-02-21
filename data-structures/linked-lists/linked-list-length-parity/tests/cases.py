from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    input_values: List          # values added head→tail; [] means empty list
    expected_parity: str        # "Even" or "Odd"


TEST_CASES = [
    # ── space-voyager demo cases ──────────────────────────────────────────────
    TestCase(
        id="three_elements_odd",
        input_values=[1, 2, 3],
        expected_parity="Odd",
    ),
    TestCase(
        id="four_elements_even",
        input_values=[10, 20, 30, 40],
        expected_parity="Even",
    ),

    # ── edge: empty list ─────────────────────────────────────────────────────
    TestCase(
        id="empty_list_even",
        input_values=[],
        expected_parity="Even",
    ),

    # ── single element ────────────────────────────────────────────────────────
    TestCase(
        id="one_element_odd",
        input_values=[42],
        expected_parity="Odd",
    ),

    # ── two elements ─────────────────────────────────────────────────────────
    TestCase(
        id="two_elements_even",
        input_values=["A", "B"],
        expected_parity="Even",
    ),

    # ── five elements ─────────────────────────────────────────────────────────
    TestCase(
        id="five_elements_odd",
        input_values=[1, 2, 3, 4, 5],
        expected_parity="Odd",
    ),

    # ── ten elements ──────────────────────────────────────────────────────────
    TestCase(
        id="ten_elements_even",
        input_values=list(range(10)),
        expected_parity="Even",
    ),

    # ── seven elements ────────────────────────────────────────────────────────
    TestCase(
        id="seven_elements_odd",
        input_values=list(range(7)),
        expected_parity="Odd",
    ),
]
