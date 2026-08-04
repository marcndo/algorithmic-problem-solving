The proof of this algorithm is based on the loop invariant property below.

At the start of iteration i, A[0,..i-1] contains the ith smallest elements arranged in non-decreasing order and A[0,..i-1] remains a permutation of the original elements in the array as a whole.

## Proof
The proof uses loop invariant.
Assume that array A is 0-indexed.
We proof three things, initialization,maintainance and termination
* Initialization. We proof that the invariant property holds before the first iteration that is when i = 0.
A[0,...,-1] is an empty range.Vacously,it contains the 0 smallest element in A.Since there's nothing to violet the order coupled with being a permutation of itself, the invariant property holds trivially.

* Maintenance.We show that each iteration maintains the loop invariant.

By the invariant, A[0,...,i-1] contains exactly the i smallest elements of the entire original array. This means every element remaining in A[i,...,n-1] must be among the (n−i) largest elements, none of them can be smaller than any element already placed in A[0,...,i-1] (if one were, A[0,...,i-1] wouldn't actually hold the i smallest elements, contradicting the invariant). So whatever the minimum of A[i,...,n-1] turns out to be, it is guaranteed to be ≥ every element in A[0,...,i-1].

Additionally, since A[0,...,i-1] holds exactly the i smallest elements overall, and the selected value is the minimum of everything not in that set, that selected value must be exactly the (i+1)-th smallest element of the entire original array (it's the smallest among "everything except the i smallest," which by definition is the next one up).

Placing this element at position i (right after the sorted A[0,...,i-1], all of whose elements are ≤ it) keeps A[0,...,i] sorted, and now A[0,...,i] contains exactly the i+1 smallest elements of the original array, satisfying the invariant for i+1.


* Termination. We explore what happens when the loop terminates. The loop terminates when i = n-1's iteration completes, i.e., the invariant now holds for i = n. By the invariant, A[0,...,n-1] contains exactly the n smallest elements of the original array (which is all of them) arranged in non-decreasing order, and is a permutation of the original array. Since A[0,...,n-1] is the entire array, this means the entire array is sorted.








