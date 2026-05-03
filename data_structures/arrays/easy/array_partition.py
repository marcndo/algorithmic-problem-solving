"Leetcode 561: Array Partition"
def partition_array(nums):
    nums.sort()
    total = 0
    for i in range(len(nums)//2):
        total += sum(nums[2*i:(2*i + 1)])
    return total

nums = [1, 4, 3, 2]
#nums = [6, 2, 6, 5, 1, 2]
print(partition_array(nums))