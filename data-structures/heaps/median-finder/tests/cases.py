TEST_CASES = [
    {"name": "Single Element", "inputs": [1], "expected": [1.0]},
    {"name": "Two Elements", "inputs": [1, 2], "expected": [1.0, 1.5]},
    {
        "name": "Ascending Order",
        "inputs": [1, 2, 3, 4, 5],
        "expected": [1.0, 1.5, 2.0, 2.5, 3.0],
    },
    {
        "name": "Descending Order",
        "inputs": [5, 4, 3, 2, 1],
        "expected": [5.0, 4.5, 4.0, 3.5, 3.0],
    },
    {
        "name": "Mixed Order",
        "inputs": [1, 5, 2, 4, 3],
        "expected": [1.0, 3.0, 2.0, 3.0, 3.0],
    },
]
