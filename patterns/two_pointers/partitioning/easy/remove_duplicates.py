"Leetcode 26: Remove duplicates"

def remove_duplicates(nums):
    slow = 1
    for i in range(1,len(nums)):
        if nums[slow - 1] != nums[i] and nums[slow] != nums[i]:
            nums[slow] = nums[i]
            slow += 1
    return slow

