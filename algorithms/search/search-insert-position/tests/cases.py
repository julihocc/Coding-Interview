from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    nums: List[int]
    target: int
    expected: int


TEST_CASES = [
    TestCase(id="example_1_found", nums=[1, 3, 5, 6], target=5, expected=2),
    TestCase(id="example_2_missing_start", nums=[1, 3, 5, 6], target=2, expected=1),
    TestCase(id="example_3_missing_end", nums=[1, 3, 5, 6], target=7, expected=4),
    TestCase(id="missing_absolute_start", nums=[1, 3, 5, 6], target=0, expected=0),
    TestCase(id="single_element_found", nums=[1], target=1, expected=0),
    TestCase(id="single_element_smaller", nums=[1], target=0, expected=0),
    TestCase(id="single_element_larger", nums=[1], target=2, expected=1),
    TestCase(id="empty_array", nums=[], target=5, expected=0),
    # User provided cases
    TestCase(id="user_case_1", nums=[1, 2, 3, 3, 5], target=3, expected=2),
    TestCase(id="user_case_2", nums=[1, 2, 3, 3, 5], target=4, expected=4),
    TestCase(id="user_case_3", nums=[1, 3, 5, 7, 9], target=10, expected=5),
]
