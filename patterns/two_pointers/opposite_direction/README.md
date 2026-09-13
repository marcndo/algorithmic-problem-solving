# Two Pointers
To understand while two pointers are efficient, we need to understand how the computer stores and retrieves data from an array in a physical hardware.

## How memory address and indices work in standard Arrays
We simplify this into how the computer stores and retrives data from the memory.

* How the computer stores data using array in memory: Unlike other data structures like hash tables,linkedlists that have data scattered in the computer's memory, array data structure is stored differently. When we create and array of size n, the computer allocates contiguous block of memory to store these data. This memory block has its elements stored next to each other without any space between them.

* How the computer retrieves this data from memory: The computer uses a mathematical formula to calculate and get the exact memory address of array's elements using only their index. Every array has a base address(a memory location of index 0). Each data type has a fixed element size for example standard integer takes 4 bytes in memory.

Address of element at index i = *Base address* + (i * element size)

Let's consider the array below
arr = [10, 20, 30]

Index:    [0]             [1]           [2]           
Value:    10              20            30     
        +---------------------------------------+
Address:|0x1000         |   0x1004   |  0x1008  |
        +---------------------------------------+
        ^
    Base address

* To read index 2, the computer computes: 0x1000 + (2 * 4) = 0x1008.
* It jumps directly to the memory address 0x1008 and retrives 30.
This explains why array lookup is O(1) time complexity no matter the size of the array.

## In-place Array sorting
Most two pointer problems relly on sorted Array. Sorting in this case must be done in-place to avoid recopying elements to a new memory location which takes extra space. Since we are not allowed to create extra space, we must sort the array while ensuring that only change the positions of the elements using swap operations.
If we want to swap two elements, arr[l] and arr[r] by simply doing
arr[l] = arr[r], we overwrite the value in arr[l] which will never be gotton again. Rather, we need a third container to do this as below.

temp = arr[l]
arr[l] = arr[r]
arr[r] = temp.
Python simplifies this by permitting arr[l], arr[r] = arr[r],arr[l] which simply automates the swap operation above.

arr.sort()(Python's Timsort/IntroSort in C++) modifies the original array directly in place. It runs in O(NlogN) time complexity and sometimes requires O(logN) or O(N) space to keep track of recursive sorting boundaries.

## Loop Invariant
The target solution lies strictly within the inclusive range [left,...right].

## How sorting and storing/retrival connects to loop invariant
Now that we understand how indices maps to physical memory and how sorting organizes data, we look at how this builds toward two pointers technique.

If we have two pointers left and right such that left points to 0x1000(index 0) and right points to 0x1008(index 2). We are looking at the absolute smallest and largest values respectively.
* Moving left += 1 adds 4 bytes to the memory address calculator. This takes us to a value we're guarenteed is greater than or equal to the one we left from. This physical certaintly is exactly what guarentees the loop invariant to discard half of the array without checking it and still getting the accurate answer.