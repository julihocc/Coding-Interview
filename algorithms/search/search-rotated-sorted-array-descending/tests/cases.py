from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    nums: List[int]
    target: int
    expected: int


TEST_CASES = [
    TestCase(id="example_1_found", nums=[9, 8, 7, 1, 15, 12, 11], target=12, expected=5),
    TestCase(id="example_2_small_found", nums=[5, 1], target=1, expected=1),
    TestCase(id="not_rotated_descending", nums=[5, 4, 3, 2, 1], target=3, expected=2),
    TestCase(id="rotated_pivot_start", nums=[1, 5, 4, 3, 2], target=5, expected=1),
    TestCase(id="rotated_pivot_end", nums=[4, 3, 2, 1, 5], target=1, expected=3),
    TestCase(id="not_found_large", nums=[9, 8, 1, 15, 12], target=20, expected=-1),
    TestCase(id="not_found_small", nums=[9, 8, 1, 15, 12], target=0, expected=-1),
    TestCase(id="single_element_found", nums=[10], target=10, expected=0),
    TestCase(id="single_element_not_found", nums=[10], target=5, expected=-1),
    TestCase(id="empty_array", nums=[], target=5, expected=-1),
]
