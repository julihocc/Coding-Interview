from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    strings: List[str]
    expected: List[str]

TEST_CASES = [
    TestCase(
        id="Basic prefix sorting",
        strings=["apple", "application", "app", "banana", "band"],
        expected=["apple", "application", "app", "banana", "band"],
    ),
    TestCase(
        id="Already sorted by prefix",
        strings=["alpha", "beta", "gamma", "delta"],
        expected=["alpha", "beta", "delta", "gamma"],
    ),
    TestCase(
        id="Reverse order prefixes",
        strings=["zebra", "yellow", "xray", "whiskey"],
        expected=["whiskey", "xray", "yellow", "zebra"],
    ),
    TestCase(
        id="Same prefix different lengths",
        strings=["cat", "catch", "category", "catastrophe"],
        expected=["cat", "catch", "category", "catastrophe"],
    ),
    TestCase(
        id="Mixed prefixes",
        strings=["dog", "dot", "dove", "cat", "car", "cart"],
        expected=["car", "cart", "cat", "dog", "dot", "dove"],
    ),
    TestCase(
        id="Short strings (< 3 chars)",
        strings=["ab", "a", "abc", "ac"],
        expected=["a", "ab", "abc", "ac"],
    ),
    TestCase(
        id="Numbers as strings",
        strings=["123", "124", "125", "120", "121"],
        expected=["120", "121", "123", "124", "125"],
    ),
    TestCase(
        id="Case sensitivity",
        strings=["Apple", "apple", "APPLE", "aPpLe"],
        expected=["APPLE", "Apple", "aPpLe", "apple"],
    ),
    TestCase(
        id="Special characters",
        strings=["@@@", "###", "$$$", "!!!"],
        expected=["!!!", "###", "$$$", "@@@"],
    ),
    TestCase(
        id="Single element",
        strings=["solo"],
        expected=["solo"],
    ),
    TestCase(
        id="Empty list",
        strings=[],
        expected=[],
    ),
    TestCase(
        id="Two elements same prefix",
        strings=["abc123", "abc456"],
        expected=["abc123", "abc456"],
    ),
    TestCase(
        id="Two elements different prefix",
        strings=["xyz", "abc"],
        expected=["abc", "xyz"],
    ),
    TestCase(
        id="Long strings same prefix",
        strings=[
            "internationalization",
            "international",
            "internet",
            "internally"
        ],
        expected=[
            "internationalization",
            "international",
            "internet",
            "internally"
        ],
    ),
]
