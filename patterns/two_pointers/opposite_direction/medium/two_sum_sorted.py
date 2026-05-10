"167. Two Sum II - Input Array Is Sorted"

def two_sum(nums, target):
    i, j = 0, len(nums) - 1
    while i < j:
        result = nums[i] + nums[j]
        if result == target:
            return [i, j]
        elif result < target:
            i += 1
        else:
            j -= 1

nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))
