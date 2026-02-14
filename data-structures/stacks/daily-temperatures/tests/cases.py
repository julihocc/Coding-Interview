from dataclasses import dataclass

@dataclass
class TestCase:
    id: str
    input: list[int]
    expected: list[int]

TEST_CASES = [
    TestCase(
        id="example_1_standard",
        input=[73, 74, 75, 71, 69, 72, 76, 73],
        expected=[3, 2, 1, 1, -1, -1, 1, -1]
    ),
    TestCase(
        id="example_2_ascending",
        input=[30, 40, 50, 60],
        expected=[-1, -1, -1, -1]
    ),
    TestCase(
        id="example_3_descending",
        input=[60, 50, 40, 30],
        expected=[1, 1, 1, -1]
    ),
    TestCase(
        id="empty_list",
        input=[],
        expected=[]
    ),
    TestCase(
        id="single_element",
        input=[30],
        expected=[-1]
    ),
    TestCase(
        id="duplicates",
        input=[73, 73, 73],
        expected=[-1, -1, -1]
    ),
    TestCase(
        id="mixed_duplicates",
        input=[73, 72, 73, 71],
        expected=[1, 2, 1, -1]
    ),
]
