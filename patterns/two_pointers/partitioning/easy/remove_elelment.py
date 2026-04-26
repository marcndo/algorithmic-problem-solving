"Leetcode 27. Remove Element"

def remove_element(nums, val):
    slow = 0
    for i in range(len(nums)):
        if nums[i] != val and slow == i:
            slow += 1
        elif nums[i] == val:
            continue
        else:
            nums[slow], nums[i] = nums[i], nums[slow]
            slow += 1
    return slow


nums = [3,2,2,3]
val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element(nums, val))