== Linked Lists

A Linked List is a linear access data structure where each element (a *Node*) contains a value and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory.

=== Types of Linked Lists

- *Singly Linked Lists:* Each node points only to the next node. Iteration only goes forward.
- *Doubly Linked Lists:* Each node contains pointers to both the next node and the previous node. This allows for backward traversal but consumes extra memory for the back-pointers.
- *Circular Linked Lists:* The "next" pointer of the last node points back to the first node, creating a loop.

=== Time Complexity Comparison

Because memory is not contiguous, calculating memory addresses via indices is impossible.
- *Access/Search:* $O(n)$ time. You must traverse the list node by node from the head.
- *Insertion/Deletion:* $O(1)$ time if you already have a pointer to the specific node. This is the key advantage over arrays — you only reassign a couple of pointers without shifting any other elements.

=== Common Patterns

==== The Dummy Node
When modifying a linked list (especially inserting/deleting the head node), keeping track of the actual head can be tricky due to edge cases.
- *Pattern:* Create a temporary `Dummy` node whose `next` pointer points to the original head. Perform operations using the dummy node to guarantee the list always has a valid prior node, then return `Dummy.next` at the end.

==== Fast and Slow Pointers
Use two pointers that traverse the list at different speeds (one moves 1 step, the other moves 2 steps).
- *Finding the Middle:* When the fast pointer reaches the end, the slow pointer will be at the exact middle of the list.
- *Detecting Cycles:* If the list has a cycle, the fast pointer will eventually "lap" the slow pointer and they will meet.
