def closest_three_sum(nums, target):
    min_distance = float("inf")
    total = None
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                curr_sum = nums[i] + nums[j] + nums[k]
                curr_distance = abs(curr_sum - target)
                if curr_distance == 0:
                    return curr_sum
                elif curr_distance < min_distance:
                    min_distance = curr_distance
                    total = curr_sum
    return total

def optimal(nums, target):
    total = None
    min_dist = float("inf")
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        l, r = i+1, n - 1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            curr_dist = abs(curr_sum - target)
            if curr_dist == 0:
                return curr_sum
            if curr_dist < min_dist:
                min_dist = curr_dist
                total = curr_sum
            if curr_sum < target:
                l += 1
            else: r -= 1
    return total

print(optimal(nums, target))


