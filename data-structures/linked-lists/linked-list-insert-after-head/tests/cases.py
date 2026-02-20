from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    id: str
    push_values: List        # values pushed (prepended) before insert_after_head calls
    insert_values: List      # values inserted after head, in order
    expected_list: List      # expected to_list() after all operations


TEST_CASES = [
    # ── core alien-network scenario ───────────────────────────────────────────
    TestCase(
        id="zog_then_zak",
        push_values=["Zog"],
        insert_values=["Zak"],
        expected_list=["Zog", "Zak"],
    ),

    # ── insert after head with multiple existing nodes ────────────────────────
    TestCase(
        id="insert_between_head_and_second",
        push_values=["C", "B", "A"],   # list becomes A->B->C
        insert_values=["X"],            # insert X after A → A->X->B->C
        expected_list=["A", "X", "B", "C"],
    ),

    # ── empty list: insert_after_head creates the first node ─────────────────
    TestCase(
        id="insert_into_empty_list",
        push_values=[],
        insert_values=["Solo"],
        expected_list=["Solo"],
    ),

    # ── single node ──────────────────────────────────────────────────────────
    TestCase(
        id="single_node",
        push_values=["Head"],
        insert_values=["After"],
        expected_list=["Head", "After"],
    ),

    # ── multiple consecutive inserts after head ───────────────────────────────
    # Each insert goes right after head, so order reverses relative to insert order
    # Start: A
    # After insert B: A->B
    # After insert C: A->C->B
    TestCase(
        id="multiple_inserts_after_head",
        push_values=["A"],
        insert_values=["B", "C"],
        expected_list=["A", "C", "B"],
    ),

    # ── integers ─────────────────────────────────────────────────────────────
    TestCase(
        id="integer_values",
        push_values=[3, 2, 1],    # list: 1->2->3
        insert_values=[99],        # 1->99->2->3
        expected_list=[1, 99, 2, 3],
    ),
]
