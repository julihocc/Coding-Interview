"""TEMPLATE: Class-based solution for Locate First and Last Position

Reference: See ../README.md for full problem description
"""

class Solution:
    def binary_search(self, nums, left, right, target, find_first):
        mid = (left+right)//2 
        if left <= right: 
            if target < nums[mid]:
                right = mid-1 
            elif target > nums[mid]:
                left = mid+1
            elif target == nums[mid]: 
                if find_first: 
                    right = mid-1
                else: 
                    left = mid+1
            return self.binary_search(nums, left, right, target, find_first)
        else:
            if find_first:
                return left 
            return right

            
    def search_range(self, nums: list[int], target: int) -> list[int]:
        """Find the starting and ending position of a given target value.

        Args:
            nums: A list of integers sorted in non-decreasing order.
            target: The integer value to search for.

        Returns:
            A list of two integers [start, end], or [-1, -1] if not found.
        """
        first = self.binary_search(nums, 0, len(nums)-1, target, True)
        last = self.binary_search(nums, 0, len(nums)-1, target, False)
        if first > last: 
            return [-1,-1]
        return [first, last]

if __name__ == "__main__":
    s = Solution()
    first, last = s.search_range([5,7,7,8,8,8,10], 8)
    print(first, last)
    first, last = s.search_range([5,7,7,8,8,8], 8)
    print(first, last)
    first, last = s.search_range([8,8,8,10], 8)
    print(first, last)
    first, last = s.search_range([5,7,7,8,8,8,10], 6)
    print(first, last)
    first, last = s.search_range([5,7,7,8,8,8,10], 11)
    print(first, last)
    first, last = s.search_range([5,5,5,8,9,9], 8)
    print(first, last)
    first, last = s.search_range([1,2], 1)
    print(first, last)
    first, last = s.search_range([1,2], 2)
    print(first, last)
    first, last = s.search_range([], 0)
    print(first, last)
