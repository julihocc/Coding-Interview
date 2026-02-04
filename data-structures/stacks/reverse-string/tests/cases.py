from dataclasses import dataclass

@dataclass
class TestCase:
    id: str
    input_str: str
    expected: str

TEST_CASES = [
    TestCase(
        id="example_1_hello",
        input_str="Hello",
        expected="olleH"
    ),
    TestCase(
        id="example_2_multi_word",
        input_str="Data Structures",
        expected="serutcurtS ataD"
    ),
    TestCase(
        id="example_3_palindrome",
        input_str="racecar",
        expected="racecar"
    ),
    TestCase(
        id="empty_string",
        input_str="",
        expected=""
    ),
    TestCase(
        id="single_char",
        input_str="A",
        expected="A"
    ),
    TestCase(
        id="special_chars",
        input_str="!@#$%",
        expected="%$#@!"
    ),
    TestCase(
        id="numbers",
        input_str="12345",
        expected="54321"
    ),
]
