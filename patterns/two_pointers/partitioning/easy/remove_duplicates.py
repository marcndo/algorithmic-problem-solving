def remove_duplicates(nums):
    result = []
    duplicates = []
    seen = set()
    for val in nums:
        if val in seen:
            duplicates.append(val)
        else:
            result.append(val)
            seen.add(val)
    result.extend(duplicates)
    return len(seen)


def optimal(nums):
    n = len(nums)
    if n == 0:
        return 0
    slow = 0
    for fast in range(1, n):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
