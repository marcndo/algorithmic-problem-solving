"https://leetcode.com/problems/container-with-most-water/"

def max_area(heights):
    left = 0
    right = len(heights) -1
    max_area = 0
    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        max_area = max(max_area, height * width)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))
