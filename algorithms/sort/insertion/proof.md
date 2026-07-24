# Proof
We proof this using the loop invariant
Invariant: At index j, A[:j-1] is already sorted and contains the same elements as in the original array 
A[:j-1]

* Initialization: We proof that the algorithms is correct before the first interation.
- Before the first iteration, i = 0, A[0] is sorted by default as the only element.
* Maintenance: We show that each iteration maintains the loop invariant.
At index j, A[:j-1] is already sort. Considering the next element j+1, we have j+1 also inserted in the correct position that is A[:j-1+1] = A[:j] sorted. Which implies the invariant property is true for the next iteration.

* Termination: We explore what happens when the loop terminates
For the for loop to terminate, j > n. Since j increases by 1, j = n + 1
thus A[0:j-1] --> A[0:n+1 - 1] = A[0:n]
