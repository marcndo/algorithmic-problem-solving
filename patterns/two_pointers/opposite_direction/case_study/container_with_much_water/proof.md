# Proof of Correctness: Container With Most Water

## 1. Problem Definition

Given an array `height` of length `n`, we need to find two distinct indices `i` and `j`, where `i < j`, such that the area formed by the two heights and the x-axis is maximized.

The area between two indices is:

\[
A(i,j) = \min(height[i], height[j]) \times (j-i)
\]

Our goal is to find:

\[
A^* = \max_{0 \leq i < j < n} A(i,j)
\]

We assume `n >= 2`, as specified in the problem constraints.

---

## 2. Brute-Force Algorithm

### Algorithm Description

We consider all possible pairs of indices `(i,j)` where `i < j`.

For each pair, we calculate the area and update `maximum_water_quantity` if the calculated area is greater than the maximum recorded so far.

### Loop Invariant

At every iteration, `maximum_water_quantity` holds the maximum area among all pairs evaluated so far.

### Proof of Correctness

We prove the algorithm's correctness using initialization, maintenance, and termination.

#### Initialization

Before the first iteration, no pairs have been evaluated, and:

`maximum_water_quantity = 0`

Since all heights and widths are nonnegative, every possible area is nonnegative.

Therefore, initializing `maximum_water_quantity` to `0` is valid.

The invariant holds before the first iteration.

#### Maintenance

Assume the invariant holds before an iteration.

This means `maximum_water_quantity` contains the maximum area among all previously evaluated pairs.

During the current iteration, we evaluate a new pair `(i,j)` and calculate:

\[
A(i,j) = \min(height[i],height[j]) \times (j-i)
\]

We then update:

`maximum_water_quantity = max(maximum_water_quantity, A(i,j))`

There are two possible cases:

1. If the new area is greater than the recorded maximum, we update `maximum_water_quantity`.
2. Otherwise, we retain the previous maximum.

In both cases, `maximum_water_quantity` contains the maximum area among all pairs evaluated so far.

Therefore, the invariant is maintained.

#### Termination

The nested loops terminate after evaluating every valid pair `(i,j)` satisfying:

\[
0 \leq i < j < n
\]

By the loop invariant, `maximum_water_quantity` contains the maximum area among all evaluated pairs.

Since every valid pair has been evaluated, this is also the maximum area among all possible pairs.

Therefore:

\[
maximum\_water\_quantity = A^*
\]

Hence, the brute-force algorithm is correct.

### Complexity Analysis

**Time Complexity: O(n²)**

The algorithm evaluates:

\[
\frac{n(n-1)}{2}
\]

distinct pairs.

Therefore, its time complexity is `O(n²)`.

**Space Complexity: O(1)**

The algorithm uses only a constant number of variables, regardless of the input size.

Therefore, its auxiliary space complexity is `O(1)`.

---

## 3. Two-Pointer Optimal Algorithm

### Algorithm Description

We initialize:

- `left = 0`
- `right = n - 1`
- `maximum_water_quantity = 0`

At each iteration:

1. Calculate the area formed by `height[left]` and `height[right]`.
2. Update `maximum_water_quantity` if the calculated area is greater.
3. Move the pointer with the shorter height inward.
4. Repeat until `left >= right`.

If both heights are equal, either pointer may be moved inward.

### Loop Invariants

We maintain two invariants.

**Invariant 1: Maximum Area So Far**

`maximum_water_quantity` always holds the maximum area among all pairs evaluated so far.

**Invariant 2: Preservation of an Optimal Candidate**

At the beginning of every iteration, at least one of the following conditions holds:

1. `maximum_water_quantity` is already equal to the global maximum area.
2. There exists a pair `(i,j)` within the current interval `[left,right]` whose area equals the global maximum area.

The second invariant guarantees that the algorithm does not eliminate every globally optimal pair before finding the optimal area.

### Proof of Correctness

We prove both invariants using initialization, maintenance, and termination.

#### Initialization

Initially:

`left = 0`

`right = n - 1`

`maximum_water_quantity = 0`

**Invariant 1**

No pairs have been evaluated, and the maximum recorded area is initialized to `0`.

Since all possible areas are nonnegative, this initialization is valid.

Therefore, Invariant 1 holds.

**Invariant 2**

Initially, the interval `[left,right]` contains every index in the array.

Therefore, every possible pair, including at least one globally optimal pair, lies within the interval.

Hence, Invariant 2 holds.

#### Maintenance

Assume both invariants hold at the beginning of an iteration.

Let:

\[
l = left,\qquad r = right
\]

The current area is:

\[
A(l,r) = \min(height[l],height[r]) \times (r-l)
\]

We update:

`maximum_water_quantity = max(maximum_water_quantity, A(l,r))`

This preserves Invariant 1 because the recorded maximum now includes the current pair.

We must also show that moving the shorter pointer preserves Invariant 2.

### Case 1: The Left Height Is Shorter or Equal

Suppose:

\[
height[l] \leq height[r]
\]

The algorithm moves the left pointer inward.

We must show that eliminating index `l` cannot cause the algorithm to lose the global maximum.

Consider any other index `k` satisfying:

\[
l < k < r
\]

The area formed by indices `l` and `k` is:

\[
A(l,k) = \min(height[l],height[k]) \times (k-l)
\]

Since:

\[
\min(height[l],height[k]) \leq height[l]
\]

and:

\[
k-l < r-l
\]

we obtain:

\[
A(l,k) \leq height[l](k-l)
\]

and therefore:

\[
A(l,k) < height[l](r-l)
\]

Because `height[l] <= height[r]`:

\[
A(l,r) = height[l](r-l)
\]

Thus:

\[
A(l,k) \leq A(l,r)
\]

Therefore, no pair formed by keeping the left pointer fixed and moving the right pointer inward can produce an area greater than the area already evaluated.

Since `A(l,r)` has already been considered and recorded in `maximum_water_quantity`, eliminating index `l` cannot eliminate a strictly better solution.

If a globally optimal pair uses index `l`, its area cannot exceed `A(l,r)`. In that case, the algorithm has already recorded the global maximum.

Otherwise, a globally optimal pair remains within the interval after moving the left pointer.

Therefore, Invariant 2 is maintained.

### Case 2: The Right Height Is Shorter

Suppose:

\[
height[r] < height[l]
\]

The algorithm moves the right pointer inward.

Consider any index `k` satisfying:

\[
l < k < r
\]

The area formed by indices `k` and `r` is:

\[
A(k,r) = \min(height[k],height[r]) \times (r-k)
\]

Since:

\[
\min(height[k],height[r]) \leq height[r]
\]

and:

\[
r-k < r-l
\]

we obtain:

\[
A(k,r) \leq height[r](r-k)
\]

and therefore:

\[
A(k,r) < height[r](r-l)
\]

Because `height[r] < height[l]`:

\[
A(l,r) = height[r](r-l)
\]

Thus:

\[
A(k,r) \leq A(l,r)
\]

Therefore, no pair formed by keeping the right pointer fixed and moving the left pointer inward can produce an area greater than the area already evaluated.

Since `A(l,r)` has already been considered, eliminating index `r` cannot eliminate a strictly better solution.

If a globally optimal pair uses index `r`, its area cannot exceed `A(l,r)`, meaning the global maximum has already been recorded.

Otherwise, a globally optimal pair remains inside the new interval.

Therefore, Invariant 2 is maintained.

Since both cases preserve the invariants, the maintenance step is established.

#### Termination

The algorithm terminates when:

`left >= right`

At this point, the remaining interval contains fewer than two distinct indices.

Therefore, no valid pair remains within the interval.

By Invariant 2, one of two conditions must hold:

1. `maximum_water_quantity` already equals the global maximum.
2. A globally optimal pair remains within the interval.

The second condition is impossible because the interval contains fewer than two indices.

Therefore:

\[
maximum\_water\_quantity = A^*
\]

Hence, the two-pointer algorithm returns the maximum possible water quantity.

### Complexity Analysis

**Time Complexity: O(n)**

Initially, the pointers are separated by `n - 1` positions.

At every iteration, exactly one pointer moves inward by one position.

Therefore, the distance between the pointers decreases by one at each iteration.

After at most `n - 1` iterations, the pointers meet and the algorithm terminates.

Each iteration performs a constant amount of work.

Therefore, the time complexity is `O(n)`.

**Space Complexity: O(1)**

The algorithm uses only a constant number of variables:

- `left`
- `right`
- `maximum_water_quantity`
- The current calculated area

No additional data structure grows with the input size.

Therefore, the auxiliary space complexity is `O(1)`.

---

## 4. Conclusion

Both algorithms correctly find the maximum quantity of water that can be contained between two heights.

The brute-force algorithm guarantees correctness by evaluating every possible pair.

The two-pointer algorithm avoids evaluating every pair by using the relationship between the shorter height and the decreasing distance between the pointers.

The key observation is that when one pointer has the shorter height, moving the opposite pointer inward cannot produce a greater area while keeping the shorter pointer fixed.

Therefore, eliminating the shorter pointer is safe.

This reduces the time complexity from `O(n²)` to `O(n)` while maintaining `O(1)` auxiliary space.