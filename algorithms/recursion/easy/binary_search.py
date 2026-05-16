def recur_binary_search(nums, target, left, right):
    if left > right:
        return False
    else:
        mid = (left + right) // 2
    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return recur_binary_search(nums, target, mid + 1, right)
    else:
        return recur_binary_search(nums, target, left, mid-1)

nums = [2, 4, 5, 6,7,9]
target = 0
print(recur_binary_search(nums,target, 0, len(nums)-1))