class Solution:
    def reverse_string(self, s: str) -> str:
        """
        Reverses a string using a stack.
        
        Time Complexity: O(n) - We traverse the string twice (push and pop).
        Space Complexity: O(n) - The stack stores all characters of the string.
        """
        stack = []
        
        # 1. Push all characters onto the stack
        for char in s:
            stack.append(char)
            
        # 2. Pop all characters from the stack to build the reversed string
        reversed_chars = []
        while stack:
            reversed_chars.append(stack.pop())
            
        return "".join(reversed_chars)
