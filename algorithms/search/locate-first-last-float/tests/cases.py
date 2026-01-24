from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    nums: List[float]
    target: float
    expected: List[int]


TEST_CASES = [
    TestCase(id="example_1", nums=[3.14, 3.14, 6.28, 9.42], target=3.14, expected=[0, 1]),
    TestCase(id="example_2", nums=[1.5, 2.5, 2.5, 2.5, 3.5], target=2.5, expected=[1, 3]),
    TestCase(id="not_found", nums=[1.1, 2.2], target=3.3, expected=[-1, -1]),
    TestCase(id="single_element_found", nums=[1.23], target=1.23, expected=[0, 0]),
    TestCase(id="single_element_not_found", nums=[1.23], target=4.56, expected=[-1, -1]),
    TestCase(id="all_same", nums=[7.7, 7.7, 7.7], target=7.7, expected=[0, 2]),
    TestCase(id="empty_array", nums=[], target=0.0, expected=[-1, -1]),
]
