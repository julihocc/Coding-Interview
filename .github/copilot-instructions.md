# Copilot Instructions: Google Interview Practice

## Project Overview

This is a **coding interview practice repository** implementing a **Virtual Judge System** for algorithm problems. Each problem has multiple solution approaches (naive vs. optimized) that are automatically tested and benchmarked.

## Architecture Pattern: Virtual Judge System

### Directory Structure (Problem Template)
```
problem-name/
├── judge.py              # Test runner (imports utils.judge_utils)
├── README.md             # Problem description
├── solutions/            # Multiple solution approaches
│   ├── naive.py         # O(n) or less efficient
│   ├── optimized.py     # O(log n) or more efficient
│   └── solution.py      # Alternative implementations
└── tests/
    └── cases.py         # Dataclass-based test cases
```

### Key Components

**1. Test Cases (`tests/cases.py`)**: Define test cases using `@dataclass` with fields:
- `id`: Test case name
- Input parameters (problem-specific)
- `expected`: Expected output (can be single value or `List` for multiple valid answers)

Example:
```python
@dataclass
class TestCase:
    id: str
    x: List[float]
    y: List[float]
    expected: Union[int, List[int]]  # Multiple valid answers supported
```

**2. Solutions (`solutions/*.py`)**: Each file exports one function (problem-specific name like `rotLeft`, `findCrossoverIndex`). Function names are specified in `judge.py`.

**3. Judge Runner (`judge.py`)**: 
- Uses `utils.judge_utils.load_solutions()` to dynamically discover all solution files
- Imports `TEST_CASES` from `tests.cases`
- Implements `run_case_logic()` to validate solution against expected output
- Key pattern: Pass copies of mutable inputs (`list(case.a)`) to ensure test isolation

**4. Shared Utilities (`utils/judge_utils.py`)**:
- `load_solutions(dir, func_name)`: Auto-discovers and imports solution functions
- `run_tests(solutions, cases, runner)`: Executes all combinations and prints formatted results with timing

### Path Resolution Pattern
All `judge.py` files use this exact pattern to import from project root:
```python
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))
from utils.judge_utils import load_solutions, run_tests
```

## Workflows

### Running Tests
```bash
# Run judge for specific problem (from repo root)
uv run python algorithms/search/find-crossover-indices/judge.py
uv run python data-structures/arrays/left-rotation/judge.py

# Output format:
# Solution        | Case            | Status     | Time (s)  
# ------------------------------------------------------------
# naive           | Sample          | PASS       | 0.000006  
# optimized       | Sample          | PASS       | 0.000003  
```

### Adding New Problems
1. Copy an existing problem directory structure
2. Update `tests/cases.py` with new TestCase dataclass fields
3. Implement solutions in `solutions/` (ensure function name matches what `judge.py` loads)
4. Modify `judge.py`: Update function name in `load_solutions()` call and `run_case_logic()` validation
5. Run judge to verify

## Code Conventions

- **Type hints required**: All solution functions use typing (e.g., `List[int]`, `Union`)
- **Docstrings include complexity**: Document time/space complexity in solution docstrings
- **Naive vs Optimized naming**: Use these specific filenames to distinguish O(n) from O(log n) approaches
- **No external dependencies**: Pure Python 3.14+ only (see `pyproject.toml`)
- **Assertions in solutions**: Complex algorithms include invariant assertions for correctness proof

## Problem Categories

- `algorithms/search/`: Binary search variations (find-crossover-indices, integer-cube-root)
- `algorithms/sorting/`: Sorting algorithms (multiway-merge)
- `data-structures/arrays/`: Array manipulation (left-rotation)

Reference: [docs/ProblemSet1_Solutions.md](docs/ProblemSet1_Solutions.md) contains mathematical problem descriptions.

## Testing Philosophy

- Solutions are isolated: Input mutations don't affect other tests (use `list()` copies)
- Multiple valid answers: `expected` can be a list; `run_case_logic()` checks `result in case.expected`
- Benchmark-driven: Every test reports execution time to compare naive vs optimized
- Zero test configuration: Judge auto-discovers all `*.py` in `solutions/` (except `__init__.py`)
