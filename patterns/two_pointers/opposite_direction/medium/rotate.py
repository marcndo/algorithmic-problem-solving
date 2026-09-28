def rotate(nums, k):
    n = len(nums)
    if k > n:
        k = k % n
    elif k == n:
        return nums
    return nums[-k:] + nums[:n-k] 


def optimal(nums, k):
    n = len(nums) 
    def reverse(nums,l, r):
        i, j = l, r
        while i <= j:
            nums[i],nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums
    k = k % n
    if k == 0:
        return nums
    else:
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
    return reverse(nums, k, n-1)
