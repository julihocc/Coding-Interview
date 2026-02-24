from dataclasses import dataclass
from typing import Optional


# The lesson tree (adjacency dict, bidirectional)
LESSON_TREE = {
    "A": ["B", "C", "D"],
    "B": ["A", "E", "F"],
    "C": ["A"],
    "D": ["A", "G", "H"],
    "E": ["B"],
    "F": ["B", "I", "J"],
    "G": ["D"],
    "H": ["D"],
    "I": ["F"],
    "J": ["F"],
}

# A simple chain: A -> B -> C
CHAIN_TREE = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
}

# Single node
SINGLE_TREE = {
    "X": [],
}

# Star tree: root with four leaves
STAR_TREE = {
    "R": ["L1", "L2", "L3", "L4"],
    "L1": ["R"],
    "L2": ["R"],
    "L3": ["R"],
    "L4": ["R"],
}


@dataclass
class TestCase:
    id: str
    mode: str  # 'traversal' or 'path'
    tree: dict
    start: str
    end: Optional[str]
    expected: object


TEST_CASES = [
    # --- Traversal cases ---
    TestCase(
        id="lesson_tree_dfs_from_A",
        mode="traversal",
        tree=LESSON_TREE,
        start="A",
        end=None,
        expected=["A", "B", "E", "F", "I", "J", "C", "D", "G", "H"],
    ),
    TestCase(
        id="single_node",
        mode="traversal",
        tree=SINGLE_TREE,
        start="X",
        end=None,
        expected=["X"],
    ),
    TestCase(
        id="chain_from_A",
        mode="traversal",
        tree=CHAIN_TREE,
        start="A",
        end=None,
        expected=["A", "B", "C"],
    ),
    TestCase(
        id="star_from_root",
        mode="traversal",
        tree=STAR_TREE,
        start="R",
        end=None,
        expected=["R", "L1", "L2", "L3", "L4"],
    ),
    # --- Path finding cases ---
    TestCase(
        id="path_A_to_J",
        mode="path",
        tree=LESSON_TREE,
        start="A",
        end="J",
        expected=["A", "B", "F", "J"],
    ),
    TestCase(
        id="path_A_to_A_same_node",
        mode="path",
        tree=LESSON_TREE,
        start="A",
        end="A",
        expected=["A"],
    ),
    TestCase(
        id="path_chain_A_to_C",
        mode="path",
        tree=CHAIN_TREE,
        start="A",
        end="C",
        expected=["A", "B", "C"],
    ),
    TestCase(
        id="path_star_root_to_L3",
        mode="path",
        tree=STAR_TREE,
        start="R",
        end="L3",
        expected=["R", "L3"],
    ),
]
