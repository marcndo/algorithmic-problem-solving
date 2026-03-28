# 📘 Data Structures & Algorithms Practice

## 🎯 Objective

This repository contains my structured practice of Data Structures and Algorithms (DSA) aimed at:

* Strengthening problem-solving skills
* Preparing for technical interviews
* Mastering core algorithmic patterns
* Building strong algorithmic thinking

---

## 🧠 Topics Covered

### 🟢 Core Data Structures

* Arrays
* Strings
* Hash Tables
* Linked Lists
* Stacks & Queues
* Trees (Binary Trees, BST)
* Graphs

---

### 🔵 Algorithmic Patterns

* Two Pointers
* Sliding Window
* Binary Search
* Recursion & Backtracking
* Depth-First Search (DFS)
* Breadth-First Search (BFS)
* Dynamic Programming (DP)
* Greedy Algorithms
* Divide & Conquer

---

## 📂 Repository Structure

```
dsa/
│── fundamentals/
│   ├── sorting/
│   ├── searching/
│
│── data_structures/
│   ├── arrays/
│   ├── strings/
│   ├── hashmaps/
│   ├── linked_lists/
│   ├── stacks_queues/
│   ├── trees/
│   ├── graphs/
│
│── algorithms/
│   ├── dfs/
│   ├── bfs/
│   ├── recursion/
│
│── patterns/
│   ├── sliding_window/
│   ├── two_pointers/
│   ├── binary_search/
│   ├── backtracking/
│   ├── dynamic_programming/
│   ├── greedy/
│
│── problems/
│── notes/
│── templates/
```

---

## 📝 Problem Format

Each problem includes:

* Problem description
* Approach / intuition
* Time & space complexity
* Clean implementation

---

### 📌 Example

**Problem:** Two Sum

**Approach:**
Use a hash map to store visited numbers and their indices.

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```

---

## 🧪 Practice Strategy

* Solve problems daily
* Focus on understanding patterns
* Revisit difficult problems
* Optimize solutions after solving

---

## 📊 Progress Tracking

| Topic   | Problems Solved |
| ------- | --------------- |
| Arrays  |                 |
| Strings |                 |
| Trees   |                 |
| Graphs  |                 |
| DP      |                 |

---

## 🧠 Key Learnings

* Breaking problems into smaller parts
* Identifying patterns quickly
* Writing clean and efficient code
* Analyzing time and space complexity

---

## 🚀 Goal

To become highly proficient in algorithmic problem solving and confidently handle coding interviews at top tech companies.

---

## 🔗 Notes

Additional notes and explanations are available in the `/notes` directory.

---

