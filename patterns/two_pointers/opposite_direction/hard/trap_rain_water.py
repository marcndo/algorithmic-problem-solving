height = [0,2,0,3,1,0,1,3,2,1]

def trap_rain_water(height):
    l, r = 0, len(height)-1
    total = 0
    max_left, max_right = height[l], height[r]
    while l < r:
        if height[l] < height[r]:
            l +=1
            max_left = max(max_left, height[l])
            total += max_left - height[l]
        else:
            r -= 1
            max_right = max(max_right, height[r])
            total += max_right - height[r]
    return total

print(trap_rain_water(height))