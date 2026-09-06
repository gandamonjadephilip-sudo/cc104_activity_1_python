from typing import List

"""
Problem 2: Find Missing Element in Sorted Array

Given a sorted array of `unique` integers `nums` that contains all integers from 
`a` to `b` except for exactly one missing integer, return the missing integer.

The array represents a sequence of consecutive integers where exactly one integer 
is missing. The array length is at least 2.

Implement two versions of the solution:

1. Using `linear search` (O(n) time complexity)
2. Using `binary search` (O(log n) time complexity)
"""
class Problem2:
    @staticmethod
    def find_missing_element_linear(nums: List[int]) -> int:
        return -1;

    @staticmethod
    def find_missing_element_binary(nums: List[int]) -> int:
        return -1
