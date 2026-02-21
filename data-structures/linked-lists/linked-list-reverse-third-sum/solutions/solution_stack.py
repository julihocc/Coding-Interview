"""Linked List – Reverse Third Sum: Stack-Based Solution.

Algorithm
---------
1. Forward pass (head → tail): push every node's data onto a stack.
2. Reverse pass (stack pop = tail → head): maintain a 1-based position counter.
   Add the value to sum_ whenever position % 3 == 0.

Time Complexity : O(n)
Space Complexity: O(n) — stack stores all n values
"""

from typing import List, Optional


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution:
    # ── helper (used by the judge) ─────────────────────────────────────────
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

    # ── main method ────────────────────────────────────────────────────────
    def find_sum(self, head: Optional[Node]) -> int:
        """Return the sum of every third element in reversed traversal.

        Positions are 1-based from the tail.  Elements at positions 3, 6, 9, …
        are included in the sum.
        """
        stack = []
        while head:
            stack.append(head.data)
            head = head.next

        sum_, index = 0, 1
        while stack:
            value = stack.pop()
            if index % 3 == 0:
                sum_ += value
            index += 1
        return sum_


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    # 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9
    # reversed: 9 8 7 6 5 4 3 2 1
    # pos 3→7, pos 6→4, pos 9→1  ⟹  sum = 12
    head = sol.build([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(sol.find_sum(head))   # 12
