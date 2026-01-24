"""
Unit tests for judge_utils.py

Tests the core functionality of the judge utility functions including:
- Loading solution classes and functions
- Running tests with proper formatting
- Error handling for broken solutions
- Dynamic column width calculation
"""

import os
import sys
import tempfile
import shutil
from dataclasses import dataclass
import pytest

# Add parent directory to path to import judge_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import judge_utils


@dataclass
class MockTestCase:
    """Mock test case for testing"""
    id: str
    value: int
    expected: int


class TestLoadClasses:
    """Tests for load_classes function"""
    
    def setup_method(self):
        """Create temporary directory with test solution files"""
        self.temp_dir = tempfile.mkdtemp()
        self.solutions_dir = os.path.join(self.temp_dir, "solutions")
        os.makedirs(self.solutions_dir)
    
    def teardown_method(self):
        """Clean up temporary directory"""
        shutil.rmtree(self.temp_dir)
    
    def test_load_valid_solution(self):
        """Test loading a valid solution class"""
        # Create a valid solution file
        solution_file = os.path.join(self.solutions_dir, "solution_test.py")
        with open(solution_file, "w") as f:
            f.write("""
class Solution:
    def solve(self):
        return 42
""")
        
        solutions = judge_utils.load_classes(
            self.solutions_dir, "Solution", subfolder=None
        )
        
        assert len(solutions) == 1
        assert solutions[0][0] == "solution_test"
        assert solutions[0][1].__name__ == "Solution"
    
    def test_load_multiple_solutions(self):
        """Test loading multiple solution files"""
        # Create multiple solution files
        for i in range(3):
            solution_file = os.path.join(self.solutions_dir, f"solution_{i}.py")
            with open(solution_file, "w") as f:
                f.write(f"""
class Solution:
    def solve(self):
        return {i}
""")
        
        solutions = judge_utils.load_classes(
            self.solutions_dir, "Solution", subfolder=None
        )
        
        assert len(solutions) == 3
        assert [s[0] for s in solutions] == ["solution_0", "solution_1", "solution_2"]
    
    def test_skip_template_files(self):
        """Test that template.py and hints.py are skipped"""
        # Create template and hints files
        for filename in ["template.py", "hints.py"]:
            filepath = os.path.join(self.solutions_dir, filename)
            with open(filepath, "w") as f:
                f.write("class Solution: pass")
        
        # Create a valid solution
        solution_file = os.path.join(self.solutions_dir, "solution_test.py")
        with open(solution_file, "w") as f:
            f.write("class Solution: pass")
        
        solutions = judge_utils.load_classes(
            self.solutions_dir, "Solution", subfolder=None
        )
        
        assert len(solutions) == 1
        assert solutions[0][0] == "solution_test"
    
    def test_handle_syntax_error(self):
        """Test graceful handling of syntax errors in solution files"""
        # Create a file with syntax error
        solution_file = os.path.join(self.solutions_dir, "solution_broken.py")
        with open(solution_file, "w") as f:
            f.write("class Solution:\n    def solve(self\n")  # Missing closing paren
        
        # Should not raise exception, just return empty list
        solutions = judge_utils.load_classes(
            self.solutions_dir, "Solution", subfolder=None
        )
        
        assert len(solutions) == 0
    
    def test_handle_missing_class(self):
        """Test handling of files without the expected class"""
        # Create a file without Solution class
        solution_file = os.path.join(self.solutions_dir, "solution_test.py")
        with open(solution_file, "w") as f:
            f.write("class WrongName: pass")
        
        solutions = judge_utils.load_classes(
            self.solutions_dir, "Solution", subfolder=None
        )
        
        assert len(solutions) == 0
    
    def test_nonexistent_directory(self):
        """Test handling of nonexistent directory"""
        solutions = judge_utils.load_classes(
            "/nonexistent/path", "Solution", subfolder=None
        )
        
        assert len(solutions) == 0


class TestLoadSolutions:
    """Tests for load_solutions function"""
    
    def setup_method(self):
        """Create temporary directory with test solution files"""
        self.temp_dir = tempfile.mkdtemp()
        self.solutions_dir = os.path.join(self.temp_dir, "solutions")
        self.reference_dir = os.path.join(self.solutions_dir, "reference")
        os.makedirs(self.reference_dir)
    
    def teardown_method(self):
        """Clean up temporary directory"""
        shutil.rmtree(self.temp_dir)
    
    def test_load_valid_function(self):
        """Test loading a valid function"""
        solution_file = os.path.join(self.reference_dir, "solution_test.py")
        with open(solution_file, "w") as f:
            f.write("""
def solve(x):
    return x * 2
""")
        
        solutions = judge_utils.load_solutions(
            self.solutions_dir, "solve", subfolder="reference"
        )
        
        assert len(solutions) == 1
        assert solutions[0][0] == "solution_test"
        assert callable(solutions[0][1])
        assert solutions[0][1](5) == 10


class TestRunTests:
    """Tests for run_tests function"""
    
    def setup_method(self):
        """Create temporary directory for reports"""
        self.temp_dir = tempfile.mkdtemp()
    
    def teardown_method(self):
        """Clean up temporary directory"""
        shutil.rmtree(self.temp_dir)
    
    def test_run_tests_with_passing_solution(self):
        """Test running tests with a passing solution"""
        # Create a simple solution
        class SimpleSolution:
            def solve(self, x):
                return x * 2
        
        solutions = [("test_solution", SimpleSolution)]
        test_cases = [
            MockTestCase(id="case1", value=5, expected=10),
            MockTestCase(id="case2", value=3, expected=6),
        ]
        
        def runner(SolutionClass, case):
            instance = SolutionClass()
            result = instance.solve(case.value)
            return result == case.expected
        
        # Run tests
        judge_utils.run_tests(
            solutions, test_cases, runner, 
            section_name="TEST", report_dir=self.temp_dir
        )
        
        # Check that report was created
        report_path = os.path.join(self.temp_dir, "report.txt")
        assert os.path.exists(report_path)
        
        # Check report contents
        with open(report_path, "r") as f:
            content = f.read()
            assert "TEST" in content
            assert "test_solution" in content
            assert "case1" in content
            assert "case2" in content
            assert "PASS" in content
    
    def test_run_tests_with_failing_solution(self):
        """Test running tests with a failing solution"""
        class FailingSolution:
            def solve(self, x):
                return x * 3  # Wrong implementation
        
        solutions = [("failing_solution", FailingSolution)]
        test_cases = [MockTestCase(id="case1", value=5, expected=10)]
        
        def runner(SolutionClass, case):
            instance = SolutionClass()
            result = instance.solve(case.value)
            return result == case.expected
        
        judge_utils.run_tests(
            solutions, test_cases, runner, report_dir=self.temp_dir
        )
        
        report_path = os.path.join(self.temp_dir, "report.txt")
        with open(report_path, "r") as f:
            content = f.read()
            assert "FAIL" in content
    
    def test_run_tests_with_error(self):
        """Test running tests with a solution that raises an error"""
        class ErrorSolution:
            def solve(self, x):
                raise ValueError("Test error")
        
        solutions = [("error_solution", ErrorSolution)]
        test_cases = [MockTestCase(id="case1", value=5, expected=10)]
        
        def runner(SolutionClass, case):
            instance = SolutionClass()
            result = instance.solve(case.value)
            return result == case.expected
        
        judge_utils.run_tests(
            solutions, test_cases, runner, report_dir=self.temp_dir
        )
        
        report_path = os.path.join(self.temp_dir, "report.txt")
        with open(report_path, "r") as f:
            content = f.read()
            assert "ERROR" in content
            assert "Error details:" in content
            assert "ValueError" in content
    
    def test_dynamic_column_widths(self):
        """Test that column widths adjust to content"""
        class Solution:
            def solve(self, x):
                return x
        
        solutions = [("very_long_solution_name_here", Solution)]
        test_cases = [
            MockTestCase(id="very_long_test_case_id_here", value=1, expected=1)
        ]
        
        def runner(SolutionClass, case):
            return True
        
        judge_utils.run_tests(
            solutions, test_cases, runner, report_dir=self.temp_dir
        )
        
        report_path = os.path.join(self.temp_dir, "report.txt")
        with open(report_path, "r") as f:
            content = f.read()
            # Check that long names are fully displayed
            assert "very_long_solution_name_here" in content
            assert "very_long_test_case_id_here" in content


class TestRunJudgeFromFile:
    """Tests for run_judge_from_file function"""
    
    def setup_method(self):
        """Create temporary directory structure"""
        self.temp_dir = tempfile.mkdtemp()
        self.problem_dir = os.path.join(self.temp_dir, "problem")
        self.solutions_dir = os.path.join(self.problem_dir, "solutions")
        os.makedirs(self.solutions_dir)
        
        # Create a judge file
        self.judge_file = os.path.join(self.problem_dir, "judge.py")
        with open(self.judge_file, "w") as f:
            f.write("# Judge file")
    
    def teardown_method(self):
        """Clean up temporary directory"""
        shutil.rmtree(self.temp_dir)
    
    def test_run_judge_from_file(self):
        """Test the run_judge_from_file helper function"""
        # Create a solution file
        solution_file = os.path.join(self.solutions_dir, "solution_test.py")
        with open(solution_file, "w") as f:
            f.write("""
class Solution:
    def solve(self, x):
        return x * 2
""")
        
        test_cases = [MockTestCase(id="case1", value=5, expected=10)]
        
        def run_case_logic(SolutionClass, case):
            instance = SolutionClass()
            result = instance.solve(case.value)
            return result == case.expected
        
        # Run the judge
        judge_utils.run_judge_from_file(
            self.judge_file, test_cases, run_case_logic
        )
        
        # Check that report was created
        report_path = os.path.join(self.problem_dir, "report.txt")
        assert os.path.exists(report_path)
        
        with open(report_path, "r") as f:
            content = f.read()
            assert "solution_test" in content
            assert "PASS" in content


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
