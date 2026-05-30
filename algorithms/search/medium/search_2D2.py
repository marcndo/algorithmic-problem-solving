def search(matrix: list[list[int]], target: int) ->bool:
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        val = matrix[row][col]
        print(val)
        if val == target:
            return True
        elif val < target:
            row += 1
        else:
            col -= 1
    return False
