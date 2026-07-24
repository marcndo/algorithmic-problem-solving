# Insertion sort

## How it works
Consider the example A = <5, 6, 3, 1, 0>
* We start with the assumptions that the first element 5 is already sorted thus we divide the array into two, the sorted half(the left of |) and the unsorted half(the right of |) as below
A = <5,| 6, 3, 1, 0>
* We pick the first element from the right half(key) and insert in the correct position to the left half. 
A = <5, 6,| 3, 1, 0>
A[:1] is now sorted with index from 0
* We repeat this process till the entire array is sorted, as below

           key                         key
            |                           |
A = <5, 6,| 3, 1, 0> --> A = <3, 5, 6,| 1, 0> --> 

                 key
                  |
A = <1, 3, 5, 6,|,0> --> A = <0, 1, 3, 5, 6> 

* NB The point of insertion is determine by comparing the key with the elements in the sorted half. If the key is smaller than the current compared element, we shift the current element to the right. Repeated shifting is made until the correct insertion point is found.

## Why it works

See the proof in proof.md(same directory)

## Time and Space complexity

### Space complexity
Since the operation is simply a reordering which is done in-place, no extra space is used. Thus the space complexity is O(1)

### Time complexity
For each key we pick at j, we would perform j - 1 comparisons and shiftings in the worse case scenario. For the last element, j = n we would peform n-1 comparisms given O(n(n-1)) --> O(n^2) time complexity.
