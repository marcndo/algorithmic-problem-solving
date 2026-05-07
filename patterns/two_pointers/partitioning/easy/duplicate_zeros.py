"Duplicate zeros"

def duplicate_zeros(nums):
    n = len(nums)
    zeros = nums.count(0)
    j = n + zeros - 1
    for i in range(n-1, -1, -1):
        if j < n:
            nums[j] = nums[i]
        if nums[j] == 0:
            j -= 1
            if j < n:
                nums[j] = 0
        j -= 1
    return nums

def duplicate_zeros1(nums):
    n = len(nums)
    i = n - 1
    zeros = nums.count(0)
    j = n + zeros - 1
    while i >= 0:
        if j < n:
            nums[j] = nums[i]
        if nums[i] == 0:
            j -= 1
            if j < n:
                nums[j] = 0
        i -= 1
        j -= 1
    return nums


print(duplicate_zeros([1, 0, 2, 0, 3]))
    