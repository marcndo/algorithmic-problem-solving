def linear_sum(nums, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return nums[start]
    else:
        mid = (start + stop) // 2
    return linear_sum(nums, start, mid) + linear_sum(nums,mid,stop)
