# Insertion sort

## How it works
We would use a 1-indexed based array for this analysis. The array has positions 1 through n and the j-th element has j-1-th elelment to the left
Consider the example A = <5, 6, 3, 1, 0>
* We start with the assumptions that the first element 5 is already sorted thus we divide the array into two, the sorted half(the left of |) and the unsorted half(the right of |) as below
A = <5,| 6, 3, 1, 0>
* We pick the first element from the right half(key) and insert in the correct position to the left half. 
A = <5, 6,| 3, 1, 0>
A[:2] is now sorted
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
For each key we pick at j, we would perform j - 1 comparisons and shiftings in the worse case scenario. For the last element, j = n we would peform n-1 comparisms given 
n        
∑​(j−1) = n(n-1)/2 = O(n^2) time complexity.
j=1        

* Best case O(n)
When the array is already sorted reach key requires exactly one comparism and 0 shifting.

* Average case O(n^2)
Same order as the worse case about half the comparism.

Let's us assume that it take c<sub>i</sub> to executes the ith line. where i is a constant.
Let t<sub>i</sub> denote the number of time the while loop test is executed.
<table>
  <tr>
    <th>Pseudocode</th>
    <th>Cost</th>
    <th>Time</th>
  </tr>
  <tr>
    <td><code>Insertion_Sort(arr)</code></td>
    <td>—</td>
    <td>—</td>
  </tr>
  <tr>
    <td><code>for i in range(1, len(arr)):</code></td>
    <td><i>c</i><sub>1</sub></td>
    <td><i>n</i> − 1</td>
  </tr>
  <tr>
    <td><code>j = i - 1</code></td>
    <td><i>c</i><sub>2</sub></td>
    <td><i>n</i> − 1</td>
  </tr>
  <tr>
    <td><code>key_val = arr[i]</code></td>
    <td><i>c</i><sub>3</sub></td>
    <td><span>&sum;<sub>i=2</sub><sup>n</sup> t<sub>i</sub></span></td>
  </tr>
  <tr>
    <td><code>while j ≥ 0 and key_val &lt; arr[j]:</code></td>
    <td><i>c</i><sub>4</sub></td>
    <td><span>&sum;<sub>i=2</sub><sup>n</sup> t<sub>i</sub></span></td>
  </tr>
  <tr>
    <td><code>arr[j+1] = arr[j]</code></td>
    <td><i>c</i><sub>5</sub></td>
    <td><span>&sum;<sub>i=2</sub><sup>n</sup>(t<sub>i</sub>−1)</span></td>
  </tr>
  <tr>
    <td><code>j = j - 1</code></td>
    <td><i>c</i><sub>6</sub></td>
    <td><span>&sum;<sub>i=2</sub><sup>n</sup>(t<sub>i</sub>−1)</span></td>
  </tr>
  <tr>
    <td><code>arr[j+1] = key_val</code></td>
    <td><i>c</i><sub>7</sub></td>
    <td><i>n</i> − 1</td>
  </tr>
</table>

To compute T(n) the total running time for the algorithm, We sum the products of the cost and time columns.
T(n) = c<sub>1</sub>(n − 1) + c<sub>2</sub>(n − 1) + c<sub>3</sub>(n − 1) + c<sub>4</sub>&sum;<sub>i=2</sub><sup>n</sup>t<sub>i</sub> + c<sub>5</sub>&sum;<sub>i=2</sub><sup>n</sup>(t<sub>i</sub>−1) + c<sub>6</sub>&sum;<sub>i=2</sub><sup>n</sup>(t<sub>i</sub>−1) + c<sub>7</sub>(n − 1)

#### Best case analysis.
This occurs when the array is already sorted, thus no shifting of elements takes place. This means that c<sub>5</sub>=c<sub>6</sub>=0.
We now have that,

T(n) = (c<sub>1</sub> + c<sub>2</sub> + c<sub>3</sub> + c<sub>4</sub> + c<sub>7</sub>)n
− (c<sub>1</sub> + c<sub>2</sub> + c<sub>3</sub> + c<sub>4</sub> + c<sub>7</sub>)

In this case T(n) is a linear function of the form an + b. With time complexity of o(n).

#### Worse case analysis

From descrete mathematics we know that 
&sum;<sub>i=2</sub><sup>n</sup> t<sub>i</sub> =
<span style="white-space: nowrap;">
<nobr><sup>n(n + 1)</sup>&frasl;<sub>2</sub></nobr>
</span> − 1

&sum;<sub>i=2</sub><sup>n</sup> (t<sub>i</sub> − 1) =
<span style="white-space: nowrap;">
<nobr><sup>n(n − 1)</sup>&frasl;<sub>2</sub></nobr>
</span>

T(n) = c<sub>1</sub>(n − 1) + c<sub>2</sub>(n − 1) + c<sub>3</sub>(n − 1) + c<sub>4</sub>(n(n + 1)/2 − 1) + c<sub>5</sub>(n(n − 1)/2) + c<sub>6</sub>(n(n − 1)/2) + c<sub>7</sub>(n − 1) =
((c<sub>4</sub> + c<sub>5</sub> + c<sub>6</sub>)/2)n²
+
(c<sub>1</sub> + c<sub>2</sub> + c<sub>3</sub> + c<sub>4</sub>/2 − c<sub>5</sub>/2 − c<sub>6</sub>/2 + c<sub>7</sub>)n
− (c<sub>1</sub> + c<sub>2</sub> + c<sub>3</sub> + c<sub>4</sub> + c<sub>7</sub>).

Therefore, 

T(n) = an<sup>2</sup> + bn + c, which is a quadratic function with time complexity O(n^2).




