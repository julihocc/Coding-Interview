class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Brute force solution.
        Time Complexity: O(N^2)
        Space Complexity: O(1) (excluding output)
        """
        n = len(temperatures)
        ans = [-1] * n
        
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] < temperatures[i]:
                    ans[i] = j - i
                    break
        
        return ans
