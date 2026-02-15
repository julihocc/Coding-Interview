# Contributing Guide

Welcome! This guide will help you contribute new problems to the repository while maintaining consistency with existing patterns. We encourage using **AI-assisted coding** (vibe coding with GitHub Copilot, Claude, ChatGPT, etc.) to ensure your contributions integrate seamlessly.

---

## 🤖 AI-Assisted Contribution Workflow (Recommended)

This repository is designed for AI-assisted development. The structured patterns and comprehensive documentation make it ideal for vibe coding.

### Why Use AI Assistance?

- ✅ **Consistency**: AI ensures your contribution matches repository patterns
- ✅ **Speed**: Generate boilerplate structure and test cases quickly
- ✅ **Quality**: AI can suggest edge cases and optimization approaches
- ✅ **Learning**: See multiple solution approaches generated and explained

### Prerequisites for AI Coding

Before starting, ensure your AI assistant has context:

1. **Read the architecture**: Point AI to [.github/copilot-instructions.md](.github/copilot-instructions.md)
2. **Study examples**: Reference existing problems as templates
3. **Understand patterns**: Review [REPOSITORY_STRUCTURE_GUIDE.md](REPOSITORY_STRUCTURE_GUIDE.md)

---

## 📋 Contribution Process

### Step 1: Choose Your Problem Category

Identify where your problem belongs:

- **`algorithms/search/`** - Binary search variants, search in special arrays
- **`algorithms/sorting/`** - Sorting algorithms, order statistics
- **`data-structures/arrays/`** - Array manipulation, rotations, subarrays
- **`data-structures/heaps/`** - Priority queue problems, k-th element problems
- **`data-structures/stacks/`** - LIFO applications, monotonic stack problems
- **`data-structures/queues/`** - FIFO applications, scheduling simulations

### Step 2: Create Directory Structure

Use AI to generate the complete structure:

#### Prompt Template for AI:
```
Create a new problem in [category]/[problem-name]/ following this repository's structure:
- README.md with problem statement
- ALGORITHM_ANALYSIS.md with complexity analysis
- judge.py for automated testing
- tests/cases.py with TestCase dataclass
- solutions/ with template, naive, and optimized implementations

Follow the patterns in [reference-problem] for consistency.
```

#### Example AI Conversation:
```
You: "I want to add a 'rotate-array' problem to data-structures/arrays/. 
Look at left-rotation for the structure and create all necessary files."

AI: "I'll create the complete structure following the left-rotation pattern..."
[AI generates all files with proper structure]
```

### Step 3: Generate Problem Files with AI

#### 3.1 README.md

**AI Prompt:**
```
Create README.md for [problem-name] including:
1. Clear problem statement
2. Real-world analogy (if applicable)
3. 2-3 examples with input/output
4. Constraints
5. Function signature showing class-based pattern
6. Notes about time/space requirements

Follow the style in data-structures/queues/basic-queue/README.md
```

**Key Requirements:**
- Problem statement should be clear and unambiguous
- Examples should cover normal, edge, and boundary cases
- Function signature must use `class Solution:` pattern

#### 3.2 ALGORITHM_ANALYSIS.md

**AI Prompt:**
```
Create ALGORITHM_ANALYSIS.md for [problem-name] with:
1. Overview of the problem
2. Naive approach with O(?) complexity
3. Optimized approach with O(?) complexity
4. Why optimization works (algorithm insight)
5. Comparison table of approaches
6. Practical applications (if applicable)
7. Best practices

Use data-structures/heaps/min-heap/ALGORITHM_ANALYSIS.md as reference.
```

**Key Requirements:**
- Include Big-O notation for all approaches
- Explain the "why" behind optimizations
- Compare space vs. time trade-offs

#### 3.3 Test Cases (tests/cases.py)

**AI Prompt:**
```
Create test cases for [problem-name] in tests/cases.py:
1. Define TestCase dataclass with appropriate fields
2. Create TEST_CASES list with 8-12 comprehensive test cases including:
   - Example cases from README
   - Edge cases (empty, single element)
   - Boundary cases (min/max values)
   - Large inputs for performance testing
   - Special cases specific to the problem

Follow the pattern in algorithms/search/find-first-occurrence/tests/cases.py
```

**Key Requirements:**
- Use `@dataclass` decorator
- Include descriptive `id` for each test case
- Cover all edge cases
- At least one large test case (100+ elements) for performance

#### 3.4 Judge (judge.py)

**AI Prompt:**
```
Create judge.py for [problem-name] that:
1. Imports run_judge_from_file from utils.judge_utils
2. Imports TEST_CASES from tests.cases
3. Defines run_case_logic(SolutionClass, case) that:
   - Instantiates Solution with test data
   - Calls appropriate methods
   - Returns boolean for pass/fail
4. Calls run_judge_from_file in __main__

Use algorithms/search/find-first-occurrence/judge.py as template.
```

**Key Requirements:**
- Proper sys.path manipulation for imports
- `run_case_logic` returns `True`/`False`
- Handle both expected result and method calls

#### 3.5 Solution Template

**AI Prompt:**
```
Create solution_template.py for [problem-name] with:
1. Class named Solution
2. __init__ method (if stateful) or empty (if stateless)
3. Main method(s) with:
   - Descriptive docstring
   - Args/Returns documentation
   - Time complexity note
   - Implementation hints (but NOT actual code)
4. Helper method stubs with docstrings
5. All methods raise NotImplementedError

Model after data-structures/queues/basic-queue/solutions/solution_template.py
```

**Key Requirements:**
- Hints guide implementation without revealing solution
- Show expected helper method structure
- Include complexity goals in docstrings

#### 3.6 Naive Solution

**AI Prompt:**
```
Create solution_naive.py for [problem-name] with:
1. Brute-force approach that's easy to understand
2. Full docstring explaining the approach
3. Time/space complexity in module docstring
4. Complete implementation
5. __main__ block for standalone testing

Use straightforward, readable code even if inefficient.
Reference: algorithms/search/find-first-occurrence/solutions/solution_naive.py
```

**Key Requirements:**
- Working solution that passes all tests
- Clear, simple logic over optimization
- Educational value for understanding problem

#### 3.7 Optimized Solution

**AI Prompt:**
```
Create solution_optimized.py for [problem-name] with:
1. Efficient algorithm approach
2. Module docstring with time/space complexity
3. Complete implementation with helper methods
4. Inline comments for complex logic
5. __main__ block for standalone testing

Optimize for the best known time/space complexity.
Reference: algorithms/search/find-first-occurrence/solutions/solution_optimized.py
```

**Key Requirements:**
- Optimal or near-optimal complexity
- Clean, maintainable code
- Passes all test cases

---

## 🎯 AI Prompting Best Practices

### Effective Prompts Structure

```
Context: I'm adding [problem-name] to [category] in a coding interview repository
Task: Create [specific-file]
Requirements: 
  - Follow class-based pattern with Solution class
  - Use patterns from [reference-file]
  - Include [specific-requirements]
Format: [any specific formatting needs]
```

### Incremental Refinement

Don't try to generate everything perfectly at once:

1. **Generate structure** → Review → Refine
2. **Generate test cases** → Run → Add edge cases
3. **Generate solutions** → Test → Optimize
4. **Generate documentation** → Review → Enhance

### Context Management

Keep AI focused on repository patterns:

```
"Before generating code, review the structure of 
data-structures/queues/basic-queue/ and follow the same patterns
for file organization, class naming, and test structure."
```

---

## ✅ Validation Checklist

Before submitting, ensure your contribution passes all checks:

### Structure Validation
```bash
python tools/validate_main_branch.py
```

- [ ] All required files present (README, ALGORITHM_ANALYSIS, judge.py, tests/, solutions/)
- [ ] Solution files follow naming convention (solution_*.py)
- [ ] `__init__.py` present in tests/ and solutions/
- [ ] No disallowed files in solutions/ directory

### Functionality Validation
```bash
# Run your judge
python [category]/[problem-name]/judge.py

# Run individual solutions
python [category]/[problem-name]/solutions/solution_naive.py
python [category]/[problem-name]/solutions/solution_optimized.py
```

- [ ] Judge runs without errors
- [ ] All test cases pass for all solutions
- [ ] Template raises NotImplementedError (doesn't accidentally pass tests)

### Quality Validation

- [ ] README clearly explains the problem
- [ ] Examples in README are correct
- [ ] ALGORITHM_ANALYSIS includes complexity comparison
- [ ] Test cases cover edge cases and large inputs
- [ ] Solutions include proper docstrings
- [ ] Code follows Google Python Style Guide (80 char lines, snake_case)

---

## 📝 Example: Complete AI-Assisted Workflow

Let's walk through adding a "circular-queue" problem:

### Conversation 1: Planning
```
You: "I want to add a circular queue problem to data-structures/queues/. 
It should implement a fixed-size queue using circular buffer. What files 
do I need?"

AI: "You'll need:
1. data-structures/queues/circular-queue/README.md
2. data-structures/queues/circular-queue/ALGORITHM_ANALYSIS.md
3. data-structures/queues/circular-queue/judge.py
4. data-structures/queues/circular-queue/tests/cases.py
5. data-structures/queues/circular-queue/solutions/solution_template.py
6. data-structures/queues/circular-queue/solutions/solution_optimized.py

Let's start with the directory structure..."
```

### Conversation 2: README
```
You: "Create README.md for circular-queue. Follow the pattern in 
basic-queue/README.md but focus on fixed-size circular buffer with 
wraparound. Include operations: enqueue, dequeue, is_full, is_empty, size."

AI: [Generates README with proper structure]

You: "Add an example showing what happens when queue reaches capacity."

AI: [Adds example]
```

### Conversation 3: Test Cases
```
You: "Create test cases in tests/cases.py. Include:
- Basic operations
- Filling queue to capacity
- Wraparound scenario
- Multiple enqueue/dequeue cycles
- Edge case: size 1 queue

Follow the TestCase dataclass pattern from basic-queue."

AI: [Generates comprehensive test cases]
```

### Conversation 4: Solutions
```
You: "Create solution_optimized.py using a list with head/tail pointers
for O(1) operations. The __init__ should take capacity as parameter.
Follow the Solution class pattern."

AI: [Generates implementation]

You: "Add better handling for empty queue dequeue - should return None."

AI: [Refines implementation]
```

### Conversation 5: Validation
```
You: "Now create judge.py that instantiates Solution with test capacity
and runs all operations from test cases."

AI: [Generates judge]

You: [Run judge and verify all tests pass]
```

---

## 🚀 Advanced: Contributing Algorithm Variations

### When Adding Search Algorithm Variants

**AI Prompt Template:**
```
I want to add [search-variant] to algorithms/search/:
- Problem: [description]
- Key difference from standard binary search: [what makes it unique]
- Expected complexity: [time/space]

Generate all files following algorithms/search/find-first-occurrence/ structure.
Ensure the Solution class stores the array in __init__() and the search
method takes only the target/query parameters.
```

### When Adding Sorting Algorithm Variants

**AI Prompt Template:**
```
I want to add [sorting-variant] to algorithms/sorting/:
- Algorithm: [name and approach]
- Key characteristics: [stable/in-place/etc]
- Expected complexity: [time/space]

Follow algorithms/sorting/merge-sort/ structure. Solution class should
store the array in __init__() and sorting method should modify it in-place
or return sorted result.
```

---

## 🤝 Collaboration with AI

### Effective Review Prompts

After AI generates code:
```
"Review this solution for:
1. Adherence to repository patterns (class-based, Solution naming)
2. Edge case handling
3. Code clarity and documentation
4. Performance optimization opportunities
5. Test coverage completeness"
```

### Debugging with AI

If tests fail:
```
"The test case [id] is failing with [error]. Here's my implementation:
[paste code]. Review against the expected behavior in README and 
suggest fixes."
```

---

## 📊 Git Workflow

### Commit Message Convention

Follow the pattern from existing commits:

```
feat(category): add problem-name problem infrastructure

- Add README with problem description
- Add ALGORITHM_ANALYSIS with complexity analysis
- Add judge.py for automated testing
- Add comprehensive test cases
- [Brief description of problem's value]
```

```
feat(category): add problem-name solution implementations

- Add solution_template.py with guided hints
- Add solution_naive.py with O(?) approach
- Add solution_optimized.py with O(?) approach
- All solutions pass X test cases
- [Brief description of optimization]
```

### Suggested Commit Structure

Commit in logical chunks:
1. Infrastructure (README, ALGORITHM_ANALYSIS, judge, tests)
2. Solutions (template and implementations)
3. Documentation updates (if updating README or learning guide)

---

## 🔍 Code Review Checklist

Before submitting a pull request:

### Functionality
- [ ] All solutions pass all test cases
- [ ] Judge runs without errors
- [ ] Individual solution files run standalone
- [ ] Template properly raises NotImplementedError

### Structure
- [ ] Follows repository directory structure
- [ ] Class named `Solution` (not problem-specific names)
- [ ] Uses stateful pattern (data in `__init__()` when appropriate)
- [ ] Proper `__init__.py` files present

### Documentation
- [ ] README has clear problem statement and examples
- [ ] ALGORITHM_ANALYSIS compares approaches with Big-O
- [ ] Solutions have module-level docstrings
- [ ] Methods have docstrings with Args/Returns

### Code Quality
- [ ] Follows Google Python Style Guide
- [ ] Max 80 characters per line
- [ ] Type hints on public methods
- [ ] No unused imports or variables
- [ ] Meaningful variable names

### Testing
- [ ] At least 8 test cases
- [ ] Covers edge cases (empty, single element)
- [ ] Includes large test case (100+ elements)
- [ ] Test IDs are descriptive

---

## 🆘 Getting Help

### Resources

1. **Repository Documentation**
   - [REPOSITORY_STRUCTURE_GUIDE.md](REPOSITORY_STRUCTURE_GUIDE.md) - File structure requirements
   - [.github/copilot-instructions.md](.github/copilot-instructions.md) - Architecture patterns
   - [LEARNING_GUIDE.md](LEARNING_GUIDE.md) - Problem organization and dependencies

2. **Example Problems**
   - **Simple Algorithm**: `algorithms/search/find-first-occurrence/`
   - **Data Structure**: `data-structures/queues/basic-queue/`
   - **Complex Algorithm**: `algorithms/sorting/quickselect/`

3. **AI Context Files**
   - Share `.github/copilot-instructions.md` with your AI assistant
   - Reference existing problems in your AI prompts
   - Use validation tools to check your work

### Common Issues and Solutions

**Issue**: Judge can't find solution classes
- **Solution**: Ensure class is named exactly `Solution`
- **AI Prompt**: "Fix the class name to match repository pattern"

**Issue**: Import errors in judge.py
- **Solution**: Check sys.path manipulation matches template
- **AI Prompt**: "Fix imports following algorithms/search/find-first-occurrence/judge.py"

**Issue**: Tests failing unexpectedly
- **Solution**: Verify test case structure matches TestCase dataclass
- **AI Prompt**: "Review test cases against data-structures/queues/basic-queue/tests/cases.py"

**Issue**: Validation script reports errors
- **Solution**: Run `python tools/validate_main_branch.py` and fix reported issues
- **AI Prompt**: "Restructure files to pass validation following allowed patterns"

---

## 🎓 Learning by Contributing

Contributing is a great way to learn:

1. **Start with variations** of existing problems (e.g., if min-heap exists, add max-heap)
2. **Use AI to understand** patterns before implementing
3. **Compare your solutions** with existing ones in the repo
4. **Iterate based on feedback** from validation tools

---

## 🌟 Best Practices Summary

### DO:
✅ Use AI to maintain consistency with existing patterns  
✅ Generate comprehensive test cases with edge cases  
✅ Create both naive and optimized solutions  
✅ Follow the class-based solution pattern  
✅ Include detailed complexity analysis  
✅ Validate with provided tools before submitting  
✅ Write clear, educational documentation  
✅ Commit in logical chunks  

### DON'T:
❌ Skip the solution_template.py file  
❌ Use problem-specific class names (use `Solution`)  
❌ Forget `__init__.py` in packages  
❌ Submit without running validation tools  
❌ Create solutions that don't follow repository patterns  
❌ Skip edge case testing  
❌ Ignore line length limits (80 chars)  
❌ Commit all changes in one massive commit  

---

## 🎉 Your First Contribution

Ready to contribute? Here's your starter prompt for AI:

```
I'm contributing to a coding interview repository. Help me add [problem-name] 
to [category]. 

First, review the structure and patterns in .github/copilot-instructions.md 
and [reference-problem].

Then, generate all required files following the repository's patterns:
1. README.md with problem statement
2. ALGORITHM_ANALYSIS.md with complexity analysis  
3. judge.py for testing
4. tests/cases.py with comprehensive test cases
5. solutions/solution_template.py with hints
6. solutions/solution_naive.py with brute-force approach
7. solutions/solution_optimized.py with efficient approach

Let's start with the README...
```

Welcome to the community! We're excited to see your contributions. Remember: AI is here to help you maintain consistency and quality, making your contributions integrate seamlessly with existing patterns.

**Happy Contributing!** 🚀
