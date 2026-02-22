# Browser History Tree — Pre-Order Traversal

## Problem Description

You're building a tool to visualize a user's browser history as a **non-binary tree**. Each node holds a URL, and children represent pages navigated to *from* that parent page.

Given the `root` of a browser history tree, return all visited URLs in **pre-order (DFS)** order: visit the current page first, then recursively visit each child in order.

## Background: The Lesson Scenario

```
browser_history_root ("Start")
└── Google.com
    ├── CodeSignal.com
    │   ├── CodeSignal.com/Tour
    │   └── CodeSignal.com/Blog
    └── Gmail.com
```

**Pre-order output:**
```
Start → Google.com → CodeSignal.com → CodeSignal.com/Tour → CodeSignal.com/Blog → Gmail.com
```

## Examples

**Example 1:** Full lesson tree (above)
```
Input:  browser_history_root
Output: ["Start", "Google.com", "CodeSignal.com",
         "CodeSignal.com/Tour", "CodeSignal.com/Blog", "Gmail.com"]
```

**Example 2:** Single page visited
```
Input:  root = TreeNode("Google.com")
Output: ["Google.com"]
```

**Example 3:** Linear chain (each page leads to exactly one next page)
```
A → B → C
Output: ["A", "B", "C"]
```

## Constraints

- The number of nodes is in the range `[0, 200]`.
- All node values are non-empty strings.
- Each node may have any number of children (including zero).

## Node Definition

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [c for c in self.children if c is not child_node]
```

## Function Signature

```python
class Solution:
    def pre_order(self, root) -> list[str]:
        # Your implementation here
        pass
```
