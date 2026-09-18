
def four_sum(nums, target):
    result = []
    nums.sort()
    n = len(nums)
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, n-1):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue

                for l in range(k+1, n):
                    if l > k + 1 and nums[l] == nums[l-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] + nums[l]== target:
                        result.append([nums[i],nums[j],nums[k], nums[l]])
    return result


def optimal(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n-3):
        #skip i duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        #skip j duplicates
        for j in range(i+1, n-2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            left, right = j+1, n-1
            while left < right:
                total = nums[left] + nums[right] + nums[i] + nums[j]
                if total == target:
                    result.append([
                        nums[i],
                        nums[j], 
                        nums[left], 
                        nums[right]
                        ])
                    left += 1
                    right -= 1

                    #skip left duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
    
                    #skip right duplicates
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

