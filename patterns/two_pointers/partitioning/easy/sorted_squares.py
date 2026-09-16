def square_sorted_array(nums):
    result = []
    for val in nums:
        result.append(val*val)
    result.sort()
    return result

def optimal(nums):
    n = len(nums)
    l = 0
    w = r = n - 1
    res = [0] * n
    while l <= r:
        if abs(nums[l]) < abs(nums[r]):
            res[w] = nums[r] * nums[r]
            r -= 1
        else:
            res[w] = nums[l] * nums[l]
            l += 1
        w -= 1
    return res
