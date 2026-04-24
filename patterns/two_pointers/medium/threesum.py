from itertools import combinations

def tripples(nums):
    combination = combinations(nums, 3)
    tripples = []
    for tripple in combination:
        if sum(tripple) == 0:
            tripples.append(tripple)
    result = []
    for i in range(len(tripples)):
        for j in range(i, len(tripples)):
            if set(tripples[i]) != set(tripples[j]):
                result.append(list(tripples[i]))  
    return result


def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                result.append([nums[i],nums[l],nums[r]])
            # skip left duplicate
            while l < r and nums[l] == nums[l+1]:
                    l += 1
            # skip right duplicates
            while l < r and nums[r] == nums[r-1]:
                    r -= 1
            l += 1
            r -= 1
    return result


nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
print(tripples(nums))
