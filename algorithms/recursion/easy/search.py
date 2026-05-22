def search(nums, target, n):
    if n == 0:
        return False
    if nums[n-1] == target:
        return n - 1
    else:
        return search(nums, target, n-1)