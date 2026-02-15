from dataclasses import dataclass
from typing import List, Any, Optional

@dataclass
class TestCase:
    id: str
    operations: List[str]  # List of operation names
    arguments: List[List[Any]]  # Arguments for each operation
    expected: List[Optional[Any]]  # Expected results for each operation

TEST_CASES = [
    TestCase(
        id="Basic Operations",
        operations=["enqueue", "enqueue", "enqueue", "peek", "dequeue", 
                    "dequeue", "size", "is_empty"],
        arguments=[["Alice"], ["Bob"], ["Charlie"], [], [], [], [], []],
        expected=[None, None, None, "Alice", "Alice", "Bob", 1, False]
    ),
    TestCase(
        id="Empty Queue",
        operations=["is_empty", "size"],
        arguments=[[], []],
        expected=[True, 0]
    ),
    TestCase(
        id="Single Element",
        operations=["enqueue", "peek", "dequeue", "is_empty"],
        arguments=[[42], [], [], []],
        expected=[None, 42, 42, True]
    ),
    TestCase(
        id="Multiple Enqueue-Dequeue",
        operations=["enqueue", "enqueue", "dequeue", "enqueue", 
                    "dequeue", "dequeue", "is_empty"],
        arguments=[[1], [2], [], [3], [], [], []],
        expected=[None, None, 1, None, 2, 3, True]
    ),
    TestCase(
        id="String Queue",
        operations=["enqueue", "enqueue", "enqueue", "dequeue", 
                    "peek", "size"],
        arguments=[["first"], ["second"], ["third"], [], [], []],
        expected=[None, None, None, "first", "second", 2]
    ),
    TestCase(
        id="Large Queue",
        operations=(["enqueue"] * 100 + ["size"] + ["dequeue"] * 50 + 
                    ["size", "is_empty"]),
        arguments=([[i] for i in range(100)] + [[]] + 
                   [[]] * 50 + [[]] + [[]]),
        expected=([None] * 100 + [100] + list(range(50)) + [50, False])
    ),
    TestCase(
        id="Peek Without Dequeue",
        operations=["enqueue", "peek", "peek", "peek", "size", "dequeue"],
        arguments=[["stable"], [], [], [], [], []],
        expected=[None, "stable", "stable", "stable", 1, "stable"]
    ),
    TestCase(
        id="Alternating Operations",
        operations=["enqueue", "dequeue", "enqueue", "dequeue", 
                    "enqueue", "enqueue", "size"],
        arguments=[["A"], [], ["B"], [], ["C"], ["D"], []],
        expected=[None, "A", None, "B", None, None, 2]
    ),
]
