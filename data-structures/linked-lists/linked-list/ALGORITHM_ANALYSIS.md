# Linked List - Algorithm Analysis

## Time Complexity

| Operation | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Insert    | O(1)      | O(1)         | O(1)       |
| Delete    | O(1)      | O(n)         | O(n)       |
| Search    | O(1)      | O(n)         | O(n)       |
| Traverse  | O(n)      | O(n)         | O(n)       |

### Detailed Analysis

**Insert at end: O(1)**
- If we maintain a `tail` pointer, appending is constant time
- Without tail pointer: O(n) to find the end

**Delete: O(n) average**
- Need to traverse to find the target node: O(n)
- Deletion itself is O(1) (just update links)
- Head deletion is O(1) special case

**Search: O(n)**
- Must traverse from head until found or end reached
- No random access like arrays

**Traversal: O(n)**
- Must visit each node sequentially

## Space Complexity

**O(n)** where n is the number of nodes
- Each node stores one data element and one pointer
- No auxiliary data structures needed (except for conversion to list)

## Why Use Linked Lists?

1. **Efficient insertion/deletion** at known positions (O(1) after traversal)
2. **Dynamic memory** allocation - grows as needed
3. **No shifting** required like arrays when inserting/deleting
4. **Cache unfriendly** - nodes scattered in memory

## Common Pitfalls

- **Forgetting to update tail** during insertion
- **Not handling edge cases** (empty list, single node, deletion of head)
- **Memory leaks** - not properly dereferencing deleted nodes
- **Off-by-one errors** when traversing
