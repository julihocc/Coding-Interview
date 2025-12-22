from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    lists: List[List[int]]
    expected: List[int]

TEST_CASES = [
    TestCase(
        id="Sample 1",
        lists=[[1,2,3], [4,5,7],[-2,0,6],[5]],
        expected=[-2, 0, 1, 2, 3, 4, 5, 5, 6, 7]
    ),
    TestCase(
        id="Sample 2",
        lists=[[-2, 4, 5 , 8], [0, 1, 2], [-1, 3,6,7]],
        expected=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    ),
    TestCase(
        id="Sample 3",
        lists=[[-1, 1, 2, 3, 4, 5]],
        expected=[-1, 1, 2, 3, 4, 5]
    ),
     TestCase(
        id="Empty",
        lists=[],
        expected=[] # Assuming empty input returns empty list or handles it gracefully. 
        # Check logic: kWayMerge checks len(list_of_lists). If empty, returns undefined in current impl.
        # Current impl: k = len(lists). If k==1 return lists[0]. If k > 1 recurses.
        # If k=0? oneStepKWayMerge(empty) -> empty. recursive calls would loop or fail?
        # Let's stick to valid inputs for now or fix implementation if needed.
        # The provided solution assumes valid inputs mostly. Removing empty case for safety unless we fix logic.
    ),
]
