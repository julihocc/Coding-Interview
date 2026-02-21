"""Linked List – Length Parity: Starter / Template.

Your task
---------
Implement ``length_parity`` so that it returns ``"Even"`` if the linked list
has an even number of nodes, and ``"Odd"`` otherwise.

Space Voyager scenario
----------------------
    ll = LinkedList()
    ll.add_node(1); ll.add_node(2); ll.add_node(3)
    ll.length_parity()  # "Odd"

    ll2 = LinkedList()
    ll2.add_node(10); ll2.add_node(20); ll2.add_node(30); ll2.add_node(40)
    ll2.length_parity() # "Even"

    ll3 = LinkedList()
    ll3.length_parity() # "Even"  (empty list)

Hint
----
Use a counter that toggles between 0 and 1:
    count = (count + 1) % 2
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data) -> None:
        """Append a node at the tail."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def length_parity(self) -> str:
        """Return 'Even' or 'Odd' based on the number of nodes."""
        raise NotImplementedError("Implement length_parity")


# ── Demo (matches the problem statement) ────────────────────────────────────
if __name__ == "__main__":
    ll = Solution()
    ll.add_node(1); ll.add_node(2); ll.add_node(3)
    print(ll.length_parity())   # Expected: Odd
