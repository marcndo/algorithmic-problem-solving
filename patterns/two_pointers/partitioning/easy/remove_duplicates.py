"Leetcode 26: Remove duplicates"

def remove_duplicates(nums):
    j = 1
    for i in range(1,len(nums)):
        if nums[j-1] != nums[i]:
            nums[j] = nums[i]
            j += 1
    return j
  

nums = [1,1,1,2,2,3]
print(remove_duplicates(nums))

