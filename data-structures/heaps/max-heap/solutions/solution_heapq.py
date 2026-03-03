"""MaxHeap using Python's built-in heapq module.

Scenario: Managing the takeoff queue for spaceships at a space station.
Spaceships are identified by the last 2 digits of their license numbers.
The spaceship with the largest license number initiates takeoff first.

Since Python's heapq only provides a min-heap implementation, we can simulate
a max-heap by negating the values before inserting them, and then negating
them back when popping.

Time complexity:
    - insert: O(log n) per element
    - delete: O(log n)
Space complexity: O(n)
"""

import heapq


class Solution:
    """Implement MaxHeap using Python's heapq."""

    def __init__(self):
        """Initialize empty heap."""
        self.maxHeap = []

    def insert(self, elt):
        """Insert element into heap, maintaining max-heap property.

        We negate the value before pushing to simulate a max-heap.
        """
        heapq.heappush(self.maxHeap, -elt)

    def delete_max(self):
        """Remove and return the maximum element.

        We pop the minimum (most negative) value and negate it back to get the maximum.
        """
        if not self.maxHeap:
            return None
        return -heapq.heappop(self.maxHeap)

    def max_element(self):
        """Return the maximum element without removing it."""
        if not self.maxHeap:
            return None
        return -self.maxHeap[0]

    def size(self):
        """Return the number of elements in the heap."""
        return len(self.maxHeap)


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Spaceships identified by the last 2 digits of their license numbers
    spaceships = [28, 14, 35, 55, 68, 72, 47, 19, 11, 32]

    heap = Solution()
    # Add all spacecrafts to the queue
    for spaceship in spaceships:
        heap.insert(spaceship)

    print(f"Heap size: {heap.size()}")
    print(f"Max element: {heap.max_element()}")

    # Delete the spacecraft with the largest license number
    largest_removed = heap.delete_max()
    print(f"Removed spaceship with license number: {largest_removed}")
    print(f"Heap size after deletion: {heap.size()}")
    print(f"New max element: {heap.max_element()}")

    # Demonstrate further deletions
    print(f"Removed: {heap.delete_max()}")
    print(f"Removed: {heap.delete_max()}")
    print(f"Current max element: {heap.max_element()}")
    print(f"Current heap size: {heap.size()}")
