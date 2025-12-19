# Google Interview Practice

A repository of coding interview problems and solutions, focusing on HackerRank challenges. This project implements a **Modern Virtual Judge** system to verify multiple solution approaches (Naive vs. Optimized) for each problem.

## Structure

The repository is organized by problem platform and name:

```text
google-interview/
├── hackerrank/
│   ├── judge_utils.py       # Shared utilities for the virtual judge system
│   ├── left-rotation/       # Problem: Arrays - Left Rotation
│   │   ├── solutions/       # Implementation files
│   │   │   ├── naive.py     # Naive O(n*d) solution
│   │   │   └── optimized.py # Optimized O(n) solution
│   │   ├── tests/
│   │   │   └── cases.py     # Python-defined test cases
│   │   ├── judge.py         # Testing script for this problem
│   │   └── README.md        # Problem description
│   └── target-index-search/ # Problem: Target Index Search
│       └── ...              # Same structure as above
```

## Getting Started

### Prerequisites
- **Python 3.14+**
- **uv** (Recommended for dependency management and running scripts)

### Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/google-interview.git
cd google-interview
```

Install dependencies (if any) using uv:
```bash
uv sync
```

## Running Tests (The Virtual Judge)

Each problem directory contains a `judge.py` script. This script automatically:
1.  **Discovers** all Python solution files in the `solutions/` directory.
2.  **Loads** test cases from `tests/cases.py`.
3.  **Executes** every solution against every test case.
4.  **Reports** validity (PASS/FAIL) and execution time.

To run the judge for a specific problem:

```bash
# Example: Left Rotation
uv run python hackerrank/left-rotation/judge.py

# Example: Target Index Search
uv run python hackerrank/target-index-search/judge.py
```

### Sample Output
```text
Solution        | Case            | Status     | Time (s)  
------------------------------------------------------------
naive           | Sample          | PASS       | 0.000006  
optimized       | Sample          | PASS       | 0.000003  
original        | Sample          | PASS       | 0.000001  
```

## Adding New Problems

1.  Create a new directory in `hackerrank/`.
2.  Create `solutions/` folder and add `naive.py` / `optimized.py`.
3.  Create `tests/cases.py` using `dataclasses`.
4.  Create `judge.py` (you can copy from an existing problem) and update the import commands.
5.  Run the judge to verify.

## License
MIT
