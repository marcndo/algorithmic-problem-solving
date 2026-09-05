def rotate(nums, k):
    n = len(nums)
    def reverse_array(l, r, nums):
        i, j = l, r
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums

    k = k % n
    if k == 0:
        return nums
    else:
        nums = reverse_array(0, n-1, nums)
        nums = reverse_array(k, n-1, nums)
    return reverse_array(0, k-1, nums)