"""Linked List Size Tracker – Fixed Solution.

The Bug
-------
In the original ``delete`` method, the size update read::

    self.size += 1   # wrong – adds instead of subtracting

Fix
---
Change to::

    self.size -= 1   # correct – decrement on successful deletion

Why it matters
--------------
- Deleting a node *removes* one element → size should go DOWN.
- The bug only triggers on delete; insert was already correct.
- Deleting a non-existent node must NOT change size – the early
  ``return`` (before the size line) already handles this correctly
  once the sign is fixed.

Time Complexity:
    - insert: O(n) – traverses to tail
    - delete: O(n) – linear search
    - to_list: O(n)

Space Complexity: O(n)
"""

from typing import List


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution:
    """Singly linked list with a correctly-maintained size counter."""

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data) -> None:
        """Append at tail – O(n)."""
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        self.size += 1      # ← correct: size grows on insert

    def delete(self, data) -> None:
        """Remove first occurrence – O(n).

        Size is decremented ONLY when the node is actually found and
        removed.  If the value is not in the list the method returns
        early, leaving size unchanged.
        """
        temp = self.head
        prev = None
        while temp:
            if temp.data == data:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                self.size -= 1  # ← FIX: was += 1 (the bug), now -= 1
                return
            prev = temp
            temp = temp.next

    def to_list(self) -> List:
        """Return all node values as a Python list (used by the judge)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


# ── Demonstrate correct behaviour ────────────────────────────────────────────
if __name__ == "__main__":
    ll = Solution()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    print("Size after 3 inserts :", ll.size)   # 3

    ll.delete(2)
    print("Size after delete(2) :", ll.size)   # 2

    ll.delete(5)                               # 5 not in list
    print("Size after delete(5) :", ll.size)   # 2
