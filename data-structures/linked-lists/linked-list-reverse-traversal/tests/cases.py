from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    input_values: List   # values pushed (prepended) in order
    expected_output: List  # expected to_reverse_list() result


TEST_CASES = [
    # ── empty list ────────────────────────────────────────────────────────────
    TestCase(
        id="empty_list",
        input_values=[],
        expected_output=[],
    ),

    # ── single element ────────────────────────────────────────────────────────
    TestCase(
        id="single_element",
        input_values=["google.com"],
        expected_output=["google.com"],
    ),

    # ── two elements ─────────────────────────────────────────────────────────
    # push("B") then push("A") → list: A→B
    # reverse: B, A
    TestCase(
        id="two_elements",
        input_values=["B", "A"],
        expected_output=["B", "A"],
    ),

    # ── browser history scenario ──────────────────────────────────────────────
    # push in order builds list: google.com→github.com→youtube.com
    # reverse should be: youtube.com, github.com, google.com
    TestCase(
        id="browser_history",
        input_values=["youtube.com", "github.com", "google.com"],
        expected_output=["youtube.com", "github.com", "google.com"],
    ),

    # ── integer values ────────────────────────────────────────────────────────
    # push 5,4,3,2,1 → list: 1→2→3→4→5  reverse: 5,4,3,2,1
    TestCase(
        id="integers",
        input_values=[5, 4, 3, 2, 1],
        expected_output=[5, 4, 3, 2, 1],
    ),

    # ── longer string sequence ────────────────────────────────────────────────
    TestCase(
        id="five_strings_reverse",
        input_values=["E", "D", "C", "B", "A"],
        expected_output=["E", "D", "C", "B", "A"],
    ),
]
