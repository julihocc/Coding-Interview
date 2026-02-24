# Department Tree DFS Traversal — Implement the Missing Logic

## Problem Description

A `DepartmentTree` class represents a company's organizational hierarchy. Each node is itself a `DepartmentTree` instance with a `name` attribute and a `subdepartments` list.

The `traverse` method is **partially implemented**: it visits the current node and marks it as visited, but the recursive logic to visit each subdepartment is **missing**.

Your task: **complete the `traverse` method** so that DFS visits every department in pre-order.

## The Starter Code (incomplete)

```python
def traverse(self, visited=None):
    if visited is None:
        visited = set()
    print(self.name)
    visited.add(self.name)

    # TODO: Add logic here to complete the traversal of the department tree
```

## The Company Hierarchy

```
CEO
├── CTO
│   ├── Infrastructure
│   ├── App Development
│   └── Security
├── CFO
│   ├── Accounting
│   └── Investor Relations
└── COO
```

**Expected DFS Output:**

```
['CEO', 'CTO', 'Infrastructure', 'App Development', 'Security',
 'CFO', 'Accounting', 'Investor Relations', 'COO']
```

## Constraints

- Use `self.subdepartments` to iterate over children.
- Use `self.name` as the node identifier.
- Pass the `visited` set recursively to avoid revisiting nodes.
- Do **not** change `__init__` or `add_subdepartment`.

## Class Definition

```python
class DepartmentTree:
    def __init__(self, name):
        self.name = name
        self.subdepartments = []

    def add_subdepartment(self, subdept_name):
        self.subdepartments.append(DepartmentTree(subdept_name))

    def traverse(self, visited=None) -> list[str]:
        # Complete this method
        pass
```

## Function Signature

```python
class Solution:
    def dfs(self, root) -> list[str]:
        """Return department names in DFS order."""
        pass
```
