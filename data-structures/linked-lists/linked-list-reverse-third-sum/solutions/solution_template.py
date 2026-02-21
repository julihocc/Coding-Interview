"""Linked List – Reverse Third Sum: Starter / Template.

Your task
---------
Complete ``find_sum`` so that it returns the sum of every third element
when the list is traversed tail → head.

Cosmo scenario
--------------
    # List: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9
    # Reversed: 9  8  7  6  5  4  3  2  1
    # Positions: 1  2  3  4  5  6  7  8  9
    # Every 3rd (pos 3,6,9): 7, 4, 1  →  sum = 12

Hint
----
1. Traverse head → tail, pushing each node's data onto a stack.
2. Pop values (giving reversed order) while maintaining a 1-based counter.
3. When counter % 3 == 0, add the value to the running sum.
"""

from typing import List, Optional


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution:
    # ── helper (used by the judge, do not modify) ──────────────────────────
    def build(self, values: List) -> Optional[Node]:
        """Build a linked list from a Python list; returns the head node."""
        if not values:
            return None
        head = Node(values[0])
        current = head
        for v in values[1:]:
            current.next = Node(v)
            current = current.next
        return head

    # ── implement this ─────────────────────────────────────────────────────
    def find_sum(self, head: Optional[Node]) -> int:
        """Return the sum of every third element in reversed traversal."""
        stack = []
        while head:
            # TODO: push head.data onto stack, advance head
            pass

        sum_, index = 0, 1
        while stack:
            # TODO: pop a value; if it's at every 3rd position, add it to sum_
            pass

        return sum_


# ── Demo (matches the problem statement) ────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    head = sol.build([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(sol.find_sum(head))   # Expected: 12
