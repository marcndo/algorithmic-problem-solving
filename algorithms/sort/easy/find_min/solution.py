"https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/"

def find_min(nums):
    left = 0 
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid 
    return nums[left]

print(find_min([3, 4, 5, 1, 2, 0, -1, -10]))