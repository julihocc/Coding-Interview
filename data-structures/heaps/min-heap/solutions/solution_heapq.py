"""MinHeap using Python's built-in heapq module.

Scenario: Tracking spacecraft license numbers from a faraway galaxy.
You observe a sequence of license numbers and need to efficiently:
  - Track all spacecraft (insertNode)
  - Remove the spacecraft with the smallest license number once it leaves radar (deleteNode)

Using heapq, Python maintains the min-heap property automatically:
  - heapq.heappush(heap, item): Insert in O(log n)
  - heapq.heappop(heap):        Remove and return the minimum in O(log n)
  - heap[0]:                    Peek at the minimum in O(1)

Time complexity:
    - insertNode: O(log n) per element
    - deleteNode: O(log n)
Space complexity: O(n)
"""

import heapq


# Create an empty MinHeap (a plain Python list)
minHeap = []


def insertNode(node_list):
    """Insert a list of license numbers into the MinHeap.

    heapq.heappush maintains the min-heap invariant after every push.

    Args:
        node_list: Iterable of integers (spacecraft license numbers).
    """
    for node in node_list:
        heapq.heappush(minHeap, node)


def deleteNode():
    """Remove and return the smallest license number from the MinHeap.

    heapq.heappop removes the root (minimum), then restores the heap
    property in O(log n) via sift-down.

    Returns:
        The smallest element, or None if the heap is empty.
    """
    try:
        return heapq.heappop(minHeap)
    except IndexError:
        return None


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Insert spacecraft license numbers
    insertNode([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    print("Heap after insertions: ", minHeap)

    # Remove the spacecraft with the smallest license number
    removed = deleteNode()
    print(f"Removed spacecraft with license number: {removed}")
    print("Heap after deleting the minimum node: ", minHeap)
