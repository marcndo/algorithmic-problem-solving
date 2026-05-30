def search(matrix:list[list[int]], target:int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    l, r = 0, m * n - 1
    while l <= r:
        mid = (l+r) // 2
        row = mid // m
        col = mid % m
        val = matrix[row][col]
        if val == target:
            return True
        elif val < target:
            l = mid + 1
        else:
            r = mid - 1
    return False




