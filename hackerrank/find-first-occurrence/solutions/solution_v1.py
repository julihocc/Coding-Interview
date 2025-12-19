def binary_seach(nums, target):
    left_pos = 0
    right_pos = len(nums)-1
    while left_pos<=right_pos:
        left = nums[left_pos]
        right = nums[right_pos]
        mid_pos = (left_pos+right_pos)//2
        mid = nums[mid_pos]
        if mid==target:
            return mid_pos 
        if mid > target: 
            right_pos = mid_pos-1
        if mid < target:
            left_pos = mid_pos+1
    return -1
        
def findFirstOccurrence(nums, target):
    # Write your code here
    some_occurece_pos = binary_seach(nums, target)
    while True:
        if some_occurece_pos==-1:
            return -1
        if nums[some_occurece_pos-1]!=target or some_occurece_pos==0:
            return some_occurece_pos
        some_occurece_pos-=1
    return some_occurece_pos

find_first_occurrence = findFirstOccurrence