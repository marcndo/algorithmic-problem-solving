def search2(nums,target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l+r) // 2
        if nums[m] == target:
            return True
        # handle duplicates
        if nums[l] == nums[m] == nums[r]:
            l += 1
            r -= 1
            continue

        # left half is sorted
        elif nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        # right half is sorted
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return False