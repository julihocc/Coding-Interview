class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Monotonic Stack solution.
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        n = len(temperatures)
        ans = [-1] * n
        stack = []  # Stores indices
        
        for i, temp in enumerate(temperatures):
            # We are looking for the next COOLER day.
            # So we maintain a Monotonic INCREASING Stack.
            # While current temp is SMALLER than stack top temp,
            # we found the next cooler day for stack top.
            while stack and temp < temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            
            stack.append(i)
            
        return ans
