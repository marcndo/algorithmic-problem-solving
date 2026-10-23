## The Problem: Container With Most Water

Given `n` heights in an array, we need to choose two distinct indices `i` and `j`, with `i < j`, such that the area sustained by the heights at `i` and `j`, together with the x-axis, holds the maximum water quantity.

The water quantity is determined by the shorter of the two heights and the distance between their indices.

- **Input:** `height = [1,8,6,2,5,4,8,3,7]`
- **Output:** `49`

## Brute Force

We consider all possible pairs. For each pair, we calculate the area and then take the maximum of these areas.

This solution works, but it is slow since we have to consider all possible pairs.

- **Time complexity — O(N²):** We would need a double `for` loop to consider all possible pairs of indices `i` and `j`, where `i < j`.
- **Space complexity — O(1):** No extra space is needed apart from tracking states like the maximum area so far.

## Bottleneck

We have to consider all possible pairs to ensure that no pair is left out.

The bottleneck is the number of pairs we have to examine, which grows quadratically with the input size.

## Optimization

The problem requires finding two indices, and the distance between these two indices contributes to the solution.

Since `left = 0` and `right = n - 1` give us the maximum distance we can get, we naturally start here and optimize around the heights, starting with `maximum_water_quantity = 0`.

The `height` array is not sorted, but we can see that moving either pointer inward will always decrease the distance between `left` and `right`.

This monotonic property of the distance, together with the fact that the area depends on two boundaries, motivates considering two pointers moving in opposite directions.

At each iteration, we calculate the area, update `maximum_water_quantity`, and move the pointer with the shorter height inward.

This allows us to avoid considering all pairs, reducing the time complexity from `O(N²)` to `O(N)` while maintaining constant auxiliary space.

The justification for moving the shorter pointer and safely eliminating candidate pairs is provided in the separate correctness proof.

## Invariants

- **Brute force:** `maximum_water_quantity` always holds the maximum water quantity among all the pairs evaluated so far.

- **Two-pointer optimal solution:** `maximum_water_quantity` always holds the maximum water quantity among all the pairs evaluated so far.

**NB:** Both approaches maintain the maximum water quantity among the pairs evaluated so far. However, this invariant alone does not guarantee that the final result is the global maximum.

The brute-force approach guarantees this by considering all possible pairs, while the two-pointer approach relies on safely eliminating pairs that cannot improve the maximum area already found.

The correctness of this elimination is established in the separate proof.

## Edge Cases

**Input:** `height = [1,1]`  
**Output:** `1`

**Input:** `height = [1,2]`  
**Output:** `1`

The standard problem guarantees at least two heights, so a single-element array is outside the specified input constraints.

## Proof of Correctness

[Proof of correctness](proof.md)