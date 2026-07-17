def max_min(nums, l, r):
    if l == r:
        return nums[l], nums[l] 
    else:
        m = (l+r) // 2
        left_val = max_min(nums,l, m)
        right_val = max_min(nums,m+1,r)
    return [min(min(left_val), min(right_val)), max(max(left_val), max(right_val))]

nums = [5, 2, 6, 1, 3]
print(max_min(nums, 0, 4))