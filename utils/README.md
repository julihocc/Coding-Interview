# Utils Directory

This directory contains utility functions used across the Google Interview preparation repository.

## Files

### `judge_utils.py`
Core utilities for running judge scripts that test solution implementations.

**Key Functions:**
- `load_classes()`: Dynamically loads solution classes from Python files
- `load_solutions()`: Dynamically loads solution functions from Python files
- `run_tests()`: Executes test cases and generates formatted reports
- `run_judge_from_file()`: Simplified helper that eliminates boilerplate in judge scripts

**Features:**
- Dynamic column width calculation for perfect alignment
- Microsecond-precision timing (μs)
- Robust error handling for broken solutions
- Detailed error reporting with exception types and messages

### `test_judge_utils.py`
Comprehensive test suite for `judge_utils.py` with 12 tests covering:
- Solution loading (valid, invalid, syntax errors)
- Test execution (passing, failing, errors)
- Report generation and formatting
- Error handling edge cases

## Running Tests

To run the test suite:

```bash
# Run all tests with verbose output
python -m pytest utils/test_judge_utils.py -v

# Run specific test class
python -m pytest utils/test_judge_utils.py::TestLoadClasses -v

# Run with coverage report
python -m pytest utils/test_judge_utils.py --cov=utils.judge_utils --cov-report=term-missing
```

## Example Usage

### Using `run_judge_from_file()` in a judge script:

```python
from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    """Test a single case."""
    instance = SolutionClass(case.input)
    result = instance.solve()
    return result == case.expected

if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
```

This automatically:
1. Determines the problem directory from `__file__`
2. Loads all solution classes from `solutions/`
3. Runs tests and generates `report.txt`
4. Displays results with proper formatting

## Report Format

Example output:

```
=== SOLUTIONS ===
Solution             | Case                       | Status     | Time (μs) 
---------------------------------------------------------------------------
solution_naive       | example_1                  | PASS       | 35.5      
solution_optimized   | large_rotation_not_found   | PASS       | 2.7       
---------------------------------------------------------------------------
solution_template    | example_1                  | ERROR      | 0.0
Error details: NotImplementedError
---------------------------------------------------------------------------
```

## Development

When modifying `judge_utils.py`:
1. Run the test suite to ensure no regressions
2. Add new tests for new functionality
3. Update this README if adding new functions
