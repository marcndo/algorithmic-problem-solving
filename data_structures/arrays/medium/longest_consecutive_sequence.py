def longest_sequence(nums):
    nums = set(nums)
    best = 0
    for n in nums:
        if n - 1 not in nums:
            length = 1
            while n + length in nums:
                length += 1
                best = max(best, length)
    return best


nums = [100,4,200,1,3,2]
print(longest_sequence(nums))