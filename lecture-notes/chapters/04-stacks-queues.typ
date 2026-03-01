== Stacks and Queues

Stacks and Queues are abstract, linear data structures that enforce strict rules for adding and removing elements. They can be implemented using either arrays or linked lists.

=== Stacks (LIFO)
A Stack follows the *Last-In-First-Out (LIFO)* principle. The last element added to the stack is the first one removed (think of a stack of plates).

- *Push:* Add an element to the top ($O(1)$).
- *Pop:* Remove the element from the top ($O(1)$).
- *Peek/Top:* View the top element without removing it ($O(1)$).

==== Common Uses
- Function call stacks in programming languages.
- Parsing algorithms (e.g., ensuring balanced brackets).
- Depth-First Search (DFS) traversals.

==== The Monotonic Stack Pattern
A stack in which the elements are strictly increasing or strictly decreasing from bottom to top. It is incredibly useful for finding the "Next Greater Element" or "Previous Smaller Element" in an array in $O(n)$ time.
- As you iterate through the array, pop elements from the stack that violate the monotonic property before pushing the new element.

=== Queues (FIFO)
A Queue follows the *First-In-First-Out (FIFO)* principle. The first element added is the first one removed (think of a line of people waiting).

- *Enqueue:* Add an element to the back ($O(1)$).
- *Dequeue:* Remove an element from the front ($O(1)$).

_Note:_ In Python, always use `collections.deque` for queues to ensure $O(1)$ operations at both ends. Using a regular `list` and popping from index $0$ is an $O(n)$ operation.

==== Common Uses
- Scheduling tasks or managing shared resources (like a printer queue).
- Breadth-First Search (BFS) traversals.
