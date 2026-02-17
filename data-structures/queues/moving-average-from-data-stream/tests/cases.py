class TestCase:
    def __init__(self, size, operations, expected):
        self.size = size
        self.operations = operations  # List of values to add
        self.expected = expected      # List of expected averages

TEST_CASES = [
    # Case 1: Standard example
    TestCase(
        size=3,
        operations=[1, 10, 3, 5],
        expected=[1.0, 5.5, 4.67, 6.0] 
        # 1 -> [1], avg 1.0
        # 10 -> [1, 10], avg 5.5
        # 3 -> [1, 10, 3], avg 4.666... -> 4.67 (rounded)
        # 5 -> [10, 3, 5], avg 6.0
    ),
    # Case 2: Size 1 window
    TestCase(
        size=1,
        operations=[1, 2, 3],
        expected=[1.0, 2.0, 3.0]
    ),
    # Case 3: Larger window than stream
    TestCase(
        size=5,
        operations=[1, 2, 3],
        expected=[1.0, 1.5, 2.0]
    )
]
