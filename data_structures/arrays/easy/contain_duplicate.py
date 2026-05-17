"""
https://leetcode.com/problems/contains-duplicate/description/
"""
def contain_duplicate(arr: list[int]) -> bool:
    seen = set()
    for val in arr:
        if val in seen:
            return True
        seen.add(val)
    return False

def contain_duplicates2(nums: list[int]) -> bool:
    return len(set(nums)) !== len(nums)

