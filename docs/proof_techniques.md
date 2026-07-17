# Proof techniques

Here, we explore the techniques we would be using to proof an algorithms correctness.

## Loop Invariant
It's a technique use to proof and iterative based algorithms.It is very similar to mathematical induction. To proof using this technique, we establish three things
* Initialization: We show that the algorithm is true before the first iteration
* Maintenance: If the algorithm is true before an iteration of the loop, it remains true before the next iteration. That is each iteration maintains the loop invariant.
* Termination: Prove that the loop terminates, and the invariant gives us a useful result for the final answer. 

Example. Prove that the code below is correct using loop invariant.

def count_value(A, target):
    count = 0
    for i in range(len(A)):
        if A[i] == target:
            count += 1
    return count

invariant Property: At the start of loop iteration i,
count contain the number of times A[i-1] == target or 
number of occurance of target in A[0,..i-1].

Proof
i = 0, A[0,-1] contain no element thus count is zero.
Which is correct.

Suppose at the start of iteration i, count contain the total
number of occurance of target in A[0, i-1].

Consider iteration i
If A[i] equal target then count increase by 1. Which 
means count contain the total number of occurancies of 
target in A[0,..,i]. This maintains the invariant Property
If A[i] is not equal to target, then count is not increased.
We move to the next iteration, meaning that A[0,..i]
now contain a count of all occurancies of target in A[0,..,i],
Which also maintain the invariant property.

Termination. Loop terminates when i = n(array length). Invariant says
at iteration i count countain the total number of occurance of
target in A[0,..n-1], which means count contain a count 
of the total occurance of target in the entire array.

## Mathematical Induction
Two types of induction exists.
#### Weak induction(Principle).
Let P be a predicate on nonnegative integers.
If 
P(0) is true, and 
P(n) implies P(n+1) for all nonnegative integers n, then P(m) is true for all nonenegative integers m.

#### Strong induction(Principle)
It is similar to weak induction except for the inductive case. While weak induction assumes that P(n) is true to establish P(n+1), strong induction assumes that P(0), P(1), ...,P(n) are all true to establish P(n+1)

Example. Prove the following using mathematical induction.
1) 1 + 3 + 5 + ... + 2n-1 = n^2 , n >= 1
2) 2^0 + 2^1 + ... + 2^n = 2^(n+1) - 1, n >= 0

1) Proof
We use weak induction on n.
Let P(n) be the predicate
1 + 3 + ... + 2n-1 = n^2 , n >= 1
P(1): 1 + 3 + ... + 2(1) - 1 = 1 = 1^1 = 1
thus P(1) is true
Suppose P(n) is true for n > 1, that is
1 + 3 + ... + 2n - 1 = n^2
Consider P(n+1)
1 + 3 + ... + 2n-1 + 2(n + 1) - 1 = n^2 + 2n + 1
                                  = (n+1)^2
Thus P(n) is true for all n >= 1

2) Proof
We use weak induction on n.
Let P(n) be the predicate.
2^0 + 2^1 + ... + 2^n = 2^(n+1) - 1, n >= 0
P(0) is true since 2^0 = 1 = 2^1 - 1
Suppose P(n) is true, that is 
2^0 + 2^1 + ... + 2^n = 2^(n+1) - 1, n > 0.
Consider P(n+1).
2^0 + 2^1 + ... + 2^n + 2^n+ 1 = 2^(n+1) - 1 + 2^n+ 1
                               = 2.2^(n+1)- 1
                               = 2^(n+2) - 1

