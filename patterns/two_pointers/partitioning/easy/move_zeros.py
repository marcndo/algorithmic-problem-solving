def move_zeros(nums):
    n = len(nums)
    result = [0] * n
    i = 0
    for val in nums:
        if val !=0:
            result[i] = val
            i += 1


def optimal(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
