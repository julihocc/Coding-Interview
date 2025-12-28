from dataclasses import dataclass

@dataclass
class TestCase:
    id: str

TEST_CASES = [
    TestCase(id='minheap'),
    TestCase(id='topk'),
    TestCase(id='maxheap'),
    TestCase(id='median'),
]
