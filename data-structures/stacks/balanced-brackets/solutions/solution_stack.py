class Solution:
    def is_balanced(self, s: str) -> bool:
        """
        Determines if the string of brackets is balanced using a stack.
        
        Time Complexity: O(n) - We traverse the string once.
        Space Complexity: O(n) - In the worst case (all open brackets), the stack holds n characters.
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # It's a closing bracket
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = "#" # Use a dummy value if stack is empty
                
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket
                stack.append(char)
        
        return not stack
