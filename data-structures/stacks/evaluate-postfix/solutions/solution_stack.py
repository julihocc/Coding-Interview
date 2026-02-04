class Solution:
    def eval_rpn(self, tokens: list[str]) -> int:
        """
        Evaluates a Reverse Polish Notation expression using a stack.
        
        Time Complexity: O(n) - We iterate through the tokens once.
        Space Complexity: O(n) - The stack can hold up to n/2 operands.
        """
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                # It's an operand (number), push to stack
                stack.append(int(token))
            else:
                # It's an operator, pop two operands
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Integer division truncating toward zero
                    # In Python, // is floor division, which behaves differently for negative numbers.
                    # We need to use int(a / b) to truncate toward zero.
                    stack.append(int(a / b))
                    
        return stack[0]
