# Proof
We proof this using the loop invariant.
The proof is based on the assumption of a 1-index based array.

Invariant: At index j, A[1:j-1] is already sorted and contains the same elements as in the original array 
A[1:j-1].

* Initialization: We proof that the algorithms is correct before the first interation.
- Before the first iteration, j = 1, loop starts at the second element.The subarray 1 through to j-1 which is 1 through to 0, A[1,0] contains no element. Since there's no element in A[1,0] which not initially there, A[1,0] is vacously sorted.

* Maintenance: We show that each iteration maintains the loop invariant. Suppose the invariant holds before iteration j that is the array with elements 1 through to j-1 are sorted and these elements are the same element originally in A[1, j-1] before being sorted. We consider the element at position j that is A[j], the key.

+ If A[j] >= A[j-1], no shifting takes place, thus the key A[j] is written in the same position, next to A[j-1]. Since A[1,...,j-1] is sorted in non-decreasing order by the loop invariant property and A[j] which is right next to A[j-1] is greater than any other element in A[1,...,j-1], A[1,..., j] is also sorted.
+ If A[j] < A[j-1], we shift A[j-1] one position to the right and compare it now with A[j-2], if it's greater than A[j-2] we shift A[j-2] one position to the right and compare the A[j] with the next element A[j-3]. We continue this way until we find A[j-k], where k is some integer such that A[j] >= A[j-k]. At this point, 
A[j] >= any element in A[1,j-k] and is placed at A[j-k+1] since all the elements from A[j-k+1,j-1] have been shifted one position to the right.
A[1,..,j] is sorted because, A[j-k+1] is greater than any element in A[1,j-k] which explains why the comparism stops at this point. Also, the element to the right of A[j-k+1] that is A[j-k+1,...,j-1] are aready sorted among each other by the loop invariant and they are all greater than the key. These means that A[1,...,j] is sorted.

Additionally, no elements are created or destroyed in both cases. Case 1 does not move any element. 
Case 2 only reallocate elements in adjacent positions(a permuation of the same elements) before inserting 
the key into the freed space. Thus A[1,...,j] is a rearrangement of exactly the same elements in A[1,...,j]

* Termination: We explore what happens when the loop terminates
For the for loop to terminate, j > n. Since j increases by 1, j = n + 1
thus A[1:j-1] --> A[1:n+1 - 1] = A[1:n]
