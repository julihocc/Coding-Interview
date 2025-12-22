from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    n: int
    expected: int

TEST_CASES = [
    TestCase(id="1", n=1, expected=1),
    TestCase(id="2", n=2, expected=1),
    TestCase(id="4", n=4, expected=1),
    TestCase(id="7", n=7, expected=1),
    TestCase(id="8", n=8, expected=2),
    TestCase(id="20", n=20, expected=2),
    TestCase(id="26", n=26, expected=2),
    TestCase(id="27", n=27, expected=3),
    TestCase(id="63", n=63, expected=3),
    TestCase(id="64", n=64, expected=4),
    TestCase(id="124", n=124, expected=4),
    TestCase(id="125", n=125, expected=5),
    TestCase(id="216", n=216, expected=6),
    TestCase(id="343", n=343, expected=7),
    TestCase(id="511", n=511, expected=7),
]
