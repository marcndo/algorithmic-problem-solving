"Leetcode 80: Remove Duplicates from Sorted Array II"
def remove_duplicates(nums):
    slow = 2
    for fast in range(2, len(nums)):
        if nums[slow - 2] != nums[fast]:
            nums[slow] = nums[fast]
            slow += 1
    return nums

print(remove_duplicates([1,1,1,2,2,2,3]))


