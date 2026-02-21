"""Linked List – Length Parity: Toggle-Bit Solution.

Algorithm
---------
Toggle a single counter bit while traversing. The counter alternates between
0 (even number of nodes seen) and 1 (odd number of nodes seen), so no full
count accumulates.

Time Complexity : O(n)
Space Complexity: O(1)
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
        """Append a node at the tail – O(1) thanks to the tail pointer."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def length_parity(self) -> str:
        """Return 'Even' if the list has an even number of nodes, else 'Odd'."""
        current = self.head
        count = 0
        while current:
            count = (count + 1) % 2   # flip between 0 and 1
            current = current.next
        return "Even" if count == 0 else "Odd"


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ll = Solution()
    ll.add_node(1); ll.add_node(2); ll.add_node(3)
    print(ll.length_parity())   # Odd

    ll2 = Solution()
    ll2.add_node(10); ll2.add_node(20); ll2.add_node(30); ll2.add_node(40)
    print(ll2.length_parity())  # Even

    ll3 = Solution()
    print(ll3.length_parity())  # Even  (empty list)
