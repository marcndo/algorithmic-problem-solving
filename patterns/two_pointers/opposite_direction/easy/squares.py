def squares(nums):
    i , j = 0, len(nums) - 1
    n = len(nums) - 1
    result = [0]* len(nums)
    while i <= j:
        left = nums[i] ** 2
        right = nums[j] ** 2
        if left > right:
            result[n] = left
            i += 1
        else:
            result[n] = right
            j -= 1
        n -= 1
    return result