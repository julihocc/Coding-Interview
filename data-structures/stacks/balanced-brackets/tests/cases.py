from dataclasses import dataclass

@dataclass
class TestCase:
    id: str
    input_str: str
    expected: bool

TEST_CASES = [
    TestCase(
        id="example_1_simple_pair",
        input_str="()",
        expected=True
    ),
    TestCase(
        id="example_2_nested_different",
        input_str="()[]{}",
        expected=True
    ),
    TestCase(
        id="example_3_incorrect_match",
        input_str="(]",
        expected=False
    ),
    TestCase(
        id="example_4_nested_mismatch",
        input_str="([)]",
        expected=False
    ),
    TestCase(
        id="example_5_nested_correct",
        input_str="{[]}",
        expected=True
    ),
    TestCase(
        id="empty_string",
        input_str="",
        expected=True
    ),
    TestCase(
        id="single_open",
        input_str="(",
        expected=False
    ),
    TestCase(
        id="single_close",
        input_str="]",
        expected=False
    ),
    TestCase(
        id="only_opens",
        input_str="(((",
        expected=False
    ),
    TestCase(
        id="only_closes",
        input_str=")))",
        expected=False
    ),
    TestCase(
        id="complex_nested",
        input_str="([]{()})",
        expected=True
    ),
    TestCase(
        id="unbalanced_long",
        input_str="([]{()}[)",
        expected=False
    ),
]
