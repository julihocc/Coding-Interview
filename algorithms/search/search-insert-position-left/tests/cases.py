from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    nums: List[int]
    target: int
    expected: int


TEST_CASES = [
    TestCase(id="example_1_found_dup", nums=[1, 2, 3, 3, 5], target=3, expected=2),
    TestCase(id="example_2_not_found", nums=[1, 2, 3, 3, 5], target=4, expected=4),
    TestCase(id="example_3_end_insert", nums=[1, 3, 5, 7, 9], target=10, expected=5),
    TestCase(id="single_element_found", nums=[1], target=1, expected=0),
    TestCase(id="single_element_smaller", nums=[1], target=0, expected=0),
    TestCase(id="single_element_larger", nums=[1], target=2, expected=1),
    TestCase(id="all_duplicates", nums=[2, 2, 2, 2], target=2, expected=0),
    TestCase(id="start_insert", nums=[2, 3, 4], target=1, expected=0),
]
