"""https://leetcode.com/problems/two-sum/
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    prev_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[nums[i]] = i
    