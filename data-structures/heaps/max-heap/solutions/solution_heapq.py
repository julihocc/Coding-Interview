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

# Create an empty MaxHeap (a plain Python list)
maxHeap = []


def insert(nodes):
    """Insert a list of license numbers into the MaxHeap.

    We negate the values before pushing to simulate a max-heap.

    Args:
        nodes: Iterable of integers (spaceship license numbers).
    """
    for node in nodes:
        heapq.heappush(maxHeap, -node)

    # Optional: Display the logical max-heap (re-negating to show original values)
    logical_heap = [-x for x in maxHeap]
    print(f"Max Heap after insertion: {logical_heap}")


def delete():
    """Remove and return the largest license number from the MaxHeap.

    We pop the minimum (most negative) value and negate it back to get the maximum.

    Returns:
        The largest element, or None if the heap is empty.
    """
    try:
        largest = -heapq.heappop(maxHeap)

        # Optional: Display the logical max-heap
        logical_heap = [-x for x in maxHeap]
        print(f"Max Heap after deletion of largest node: {logical_heap}")

        return largest
    except IndexError:
        return None


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Spaceships identified by the last 2 digits of their license numbers
    spaceships = [28, 14, 35, 55, 68, 72, 47, 19, 11, 32]

    # Add all spacecrafts to the queue
    insert(spaceships)

    # Delete the spacecraft with the largest license number
    largest_removed = delete()
    print(f"Removed spaceship with license number: {largest_removed}")
