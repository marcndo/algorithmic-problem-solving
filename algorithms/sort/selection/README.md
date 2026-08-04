# Selection Sort

## How it works.
The idea is to sort an array, we pick the first smallest element and insert in postion 1, then pick the second smallest element and insert in position 2, then proceed to the third, fouth till the last element.

## Why in works
[see proof](proof.md)

## Time and Space complexity

### Space complexity
The algorithms uses fixed number of variables i, j and min_val,beyond the input itself. Mutation of the array is in-place. Since the variables never grows as the array size grows, we conclude that the array runs in constant space thus O(1) space complexity.

### Time Complexity
Following similar analysis in [Proof of Insertion sort](../insertion/proof.md), the time complexity is O(n^2), where n is the size of the array.

