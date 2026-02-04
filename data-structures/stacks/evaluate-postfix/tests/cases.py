from dataclasses import dataclass

@dataclass
class TestCase:
    id: str
    tokens: list[str]
    expected: int

TEST_CASES = [
    TestCase(
        id="example_1_simple_mult",
        tokens=["2", "1", "+", "3", "*"],
        expected=9
    ),
    TestCase(
        id="example_2_division_add",
        tokens=["4", "13", "5", "/", "+"],
        expected=6
    ),
    TestCase(
        id="example_3_complex",
        tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        expected=22
    ),
    TestCase(
        id="simple_add",
        tokens=["3", "4", "+"],
        expected=7
    ),
    TestCase(
        id="simple_sub",
        tokens=["3", "4", "-"],
        expected=-1
    ),
    TestCase(
        id="negative_result",
        tokens=["3", "-4", "+"],
        expected=-1
    ),
    TestCase(
        id="division_truncate_positive",
        tokens=["13", "5", "/"],
        expected=2
    ),
    TestCase(
        id="division_truncate_negative",
        tokens=["13", "-5", "/"],
        expected=-2
    ),
    TestCase(
        id="multi_digit",
        tokens=["100", "200", "+"],
        expected=300
    ),
]
