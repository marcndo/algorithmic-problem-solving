# Selection Sort

## How it works.
The idea is to sort an array by repeatedly finding the smallest element and swapping into it's correct position. That is we find the ovarall smallest element and swap with 0, then the next smallest element in the remaining section of the array and swap with 1, then continue till the full array is eventually sorted.

## Why in works
[see proof](proof.md)

## Time and Space complexity

### Space complexity
The algorithms uses fixed number of variables i, j and min_val,beyond the input itself. Mutation of the array is in-place. Since the variables never grows as the array size grows, we conclude that the array runs in constant space thus O(1) space complexity.

### Time Complexity
Following similar analysis in [Proof of Insertion sort](../insertion/proof.md), the time complexity is O(n^2), where n is the size of the array.

