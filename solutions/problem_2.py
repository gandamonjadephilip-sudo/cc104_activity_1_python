
"""
Problem 2: Find Missing Element in Sorted Array

Given a sorted array of unique integers from 1 to n+1,
with exactly one integer missing, return the missing integer.
"""
from typing import List


class Problem2:
    @staticmethod
    def find_missing_element_linear(nums: List[int]) -> int:
        """Find the missing element using linear search."""
        expected = 1

        for number in nums:
            if number != expected:
                return expected
            expected += 1

        return expected

    @staticmethod
    def find_missing_element_binary(nums: List[int]) -> int:
        """Find the missing element using binary search."""
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == mid + 1:
                left = mid + 1
            else:
                right = mid

        return left + 1
