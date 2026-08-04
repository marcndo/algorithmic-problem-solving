def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        j = i + 1
        min_index = i
        while j < n:
            if arr[min_index] > arr[j]:
                min_index = j
            j+=1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [5, 2, 3, 0, 1, -2]
print(selection_sort(arr))
