from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    nums: List[int]
    target: int
    expected: List[int]


TEST_CASES = [
    TestCase(id="found_example_1", nums=[5, 7, 7, 8, 8, 10], target=8, expected=[3, 4]),
    TestCase(id="not_found_example_2", nums=[5, 7, 7, 8, 8, 10], target=6, expected=[-1, -1]),
    TestCase(id="empty_array", nums=[], target=0, expected=[-1, -1]),
    TestCase(id="single_element_found", nums=[1], target=1, expected=[0, 0]),
    TestCase(id="single_element_not_found", nums=[1], target=0, expected=[-1, -1]),
    TestCase(id="two_elements_found", nums=[2, 2], target=2, expected=[0, 1]),
    TestCase(id="three_elements_duplicated", nums=[1, 2, 3], target=2, expected=[1, 1]),
    TestCase(id="multiple_duplicates", nums=[1, 2, 3, 4, 5, 5, 5, 5, 6], target=5, expected=[4, 7]),
]
