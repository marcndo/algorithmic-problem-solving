"Leetcode 27. Remove Element"

def remove_elem(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i] = nums[j]
            j += 1
    return j


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


