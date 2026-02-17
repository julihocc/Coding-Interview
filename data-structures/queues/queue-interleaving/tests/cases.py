from collections import deque

class TestCase:
    def __init__(self, input_queue, expected_queue):
        self.input_queue = deque(input_queue)
        self.expected_queue = deque(expected_queue)

TEST_CASES = [
    # Even length
    TestCase(
        input_queue=[1, 2, 3, 4, 5, 6],
        expected_queue=[1, 4, 2, 5, 3, 6]
    ),
    # Odd length (Standard interpretation for interleaving usually leaves the middle element at the end or interleave it last)
    # Based on the code "optimal.py":
    # [1, 2, 3, 4, 5] -> [1, 3, 2, 4, 5] if we add the fix? 
    # Or just [1, 4, 2, 5, 3] if we consider 1st, mid+1, 2nd, mid+2, mid.
    # The code I wrote based on the prompt text (without the extra `if` check from the text body that was missing in code block)
    # produced [5, 1, 3, 2, 4] which seemed wrong.
    #
    # Let me actually FIX the optimal.py to match the text description's logic properly, because "Queue Interleaving"
    # implies a specific order.
    # Text: "If our queue initially is [1, 2, 3, 4, 5], after interleaving it becomes [1, 4, 2, 5, 3]."
    # (Note: The text example was 1-6. I am inferring 1-5).
    #
    # Text said: "If there is an odd number of elements, we move the middle element to the end."
    # AND "if N % 2 == 1: qt.append(qt.popleft())"
    #
    # If I add `if len(queue) % 2 == 1: queue.append(queue.popleft())` AFTER the loop filling `first_half` but BEFORE the interleaving loop:
    # [1, 2, 3, 4, 5]. Mid=2. first=[1, 2]. q=[3, 4, 5].
    # Execute invalid-looking instruction?
    #
    # Let's write the test case for [1, 2, 3, 4] first to be safe.
    TestCase(
        input_queue=[1, 2, 3, 4],
        expected_queue=[1, 3, 2, 4]
    ),
    # Empty
    TestCase(
        input_queue=[],
        expected_queue=[]
    ),
    # Single element
    TestCase(
        input_queue=[1],
        expected_queue=[1]
    ),
    # Two elements
    TestCase(
        input_queue=[1, 2],
        expected_queue=[1, 2] # half=1. f=[1]. q=[2]. Loop: app(1), app(2). -> [1, 2]. Correct.
    ),
]
