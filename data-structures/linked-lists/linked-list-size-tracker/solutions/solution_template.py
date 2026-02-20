"""Linked List Size Tracker – Starter / Template (contains the bug).

Your task
---------
The ``LinkedList`` class below tracks its ``size``, but the counter
updates incorrectly. Identify the bug and fix it so that ``size``
always reflects the true number of nodes.

Expected output when you run this script directly
-------------------------------------------------
    Size after 3 inserts : 3
    Size after delete(2) : 2
    Size after delete(5) : 2   ← 5 was not in the list, so no change

Hint
----
One of the arithmetic operators in the counter-update lines is wrong.
"""

from typing import List


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution:
    """Singly linked list with a size counter – contains a deliberate bug."""

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data) -> None:
        """Append at tail and increment size."""
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        self.size += 1          # ← correct

    def delete(self, data) -> None:
        """Remove first occurrence and update size. BUG: size is wrong here!"""
        temp = self.head
        prev = None
        while temp:
            if temp.data == data:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                self.size += 1  # ← BUG: should be -= 1  (TODO: fix this)
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


# ── Demonstrate the bug ──────────────────────────────────────────────────────
if __name__ == "__main__":
    ll = Solution()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    print("Size after 3 inserts :", ll.size)   # Expected: 3

    ll.delete(2)
    print("Size after delete(2) :", ll.size)   # Expected: 2  (buggy: 4)

    ll.delete(5)
    print("Size after delete(5) :", ll.size)   # Expected: 2
