<div align="center">

# 628. Maximum Product of Three Numbers

<img src="https://img.shields.io/badge/Difficulty-Easy-00C853?style=for-the-badge" alt="Easy">
<img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Topic-Array-8A2BE2?style=flat-square" alt="Array">
<img src="https://img.shields.io/badge/Topic-Math-FF1493?style=flat-square" alt="Math">
<img src="https://img.shields.io/badge/Topic-Sorting-00BCD4?style=flat-square" alt="Sorting">

</div>

---

## 🧩 Problem Summary

Given an integer array, choose three numbers whose product is as large as
possible.

Return the maximum product.

---

## 💡 Main Mathematical Idea

The important rule is:

```text
Negative × Negative = Positive
```

Therefore, the maximum product can come from either:

### Option 1: Three largest numbers

```text
largest × second largest × third largest
```

### Option 2: Two smallest numbers and the largest number

```text
smallest × second smallest × largest
```

The smallest numbers may be very negative. Multiplying two negative numbers
creates a positive number.

---

## 🧪 Example

```text
nums = [-10, -10, 5, 2]
```

After sorting:

```text
[-10, -10, 2, 5]
```

Three largest:

```text
-10 × 2 × 5 = -100
```

Two smallest and largest:

```text
-10 × -10 × 5 = 500
```

Therefore:

```text
Answer = 500
```

---

## 🪜 Approach

1. Sort the array.
2. Multiply the three largest numbers.
3. Multiply the two smallest numbers and the largest number.
4. Return the larger result.

---

## 🐍 Python Solution

```python
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        three_largest = nums[-1] * nums[-2] * nums[-3]
        two_smallest_and_largest = nums[0] * nums[1] * nums[-1]

        return max(three_largest, two_smallest_and_largest)
```

---

## ⏱️ Complexity Analysis

| Measure | Complexity | Explanation |
|---|---|---|
| Time | `O(n log n)` | The array is sorted |
| Extra variables | `O(1)` | Only a few values are stored |

---

## ⚠️ Important Edge Cases

- All numbers are positive
- All numbers are negative
- Two large negative numbers
- Array contains zero
- Duplicate values
- Exactly three values

---

## 🎯 Interview Takeaway

For maximum-product questions, do not examine only the largest values.

Always ask:

> Can two negative numbers create a larger positive result?

---

<div align="center">

[⬅️ Back to Main Repository](../../../README.md)

</div>
