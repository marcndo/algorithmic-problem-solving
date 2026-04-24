def sort_colors(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current
    return nums

nums = [2,0,2,1,1,0]
print(sort_colors(nums))