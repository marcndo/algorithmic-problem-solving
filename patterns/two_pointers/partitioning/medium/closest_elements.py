def find_closest_element(arr, k, x):
    by_dist = sorted(arr, key=lambda v: abs(x-v))
    return sorted(by_dist[:k])


def optimal(arr, k, x):
    l, r = 0, len(arr) - 1
    while r - l + 1 > k:
        if abs(arr[l] - x) <= abs(arr[r] - x):
            r -= 1
        else:
            l += 1
    return arr[l:r+1]