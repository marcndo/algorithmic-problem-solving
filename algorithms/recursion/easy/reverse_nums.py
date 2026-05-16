def recur_reverse(nums, left, right):
    if left == right:
        return nums
    else:
        nums[left], nums[right] = nums[right], nums[left]
    return recur_reverse(nums, left+1, right-1)
