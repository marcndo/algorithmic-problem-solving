def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        j = i - 1
        key_val = arr[i]
        while j >= 0 and key_val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key_val
    return arr


