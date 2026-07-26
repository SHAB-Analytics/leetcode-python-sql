from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Return the maximum product that can be formed using three numbers.

        The maximum product must come from either:
        1. The three largest numbers.
        2. The two smallest numbers and the largest number.
        """

        nums.sort()

        three_largest = nums[-1] * nums[-2] * nums[-3]
        two_smallest_and_largest = nums[0] * nums[1] * nums[-1]

        return max(three_largest, two_smallest_and_largest)
