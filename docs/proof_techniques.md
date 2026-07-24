# Proof techniques

Here, we explore the techniques we would be using to proof an algorithms correctness.

## Loop Invariant
It's a technique use to proof and iterative based algorithms.It is very similar to mathematical induction. To proof using this technique, we establish three things
* Initialization: We show that the algorithm is true before the first iteration
* Maintenance: If the algorithm is true before an iteration of the loop, it remains true before the next iteration. That is each iteration maintains the loop invariant.
* Termination: When the loop terminates, the invariant gives us a useful property that helps us proof that the algorithm is correct. 
