def remove_duplicates(nums):
    val_count = {}
    result = []
    for val in nums:
        val_count[val] = val_count.get(val, 0) + 1
    for val in val_count:
        if val_count[val] >= 2:
            result.append(val)
            result.append(val)
        else:
            result.append(val)
    return result


def optimal(nums):
    l = 2
    n = len(nums)
    if n < 2:
        return n
    for r in range(2,n):
        if nums[l-2] != nums[r]:
            nums[l] = nums[r]
            l += 1
    return l