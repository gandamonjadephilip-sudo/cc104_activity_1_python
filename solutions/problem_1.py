
"""
Count Target Occurrences

Given a sorted array of integers nums and an integer target,
return how many times target appears in nums.
"""
from typing import List


class Problem1:
    @staticmethod
    def count_occurrences_linear(nums: List[int], target: int) -> int:
        """Count target occurrences using linear search."""
        count = 0

        for number in nums:
            if number == target:
                count += 1

        return count

    @staticmethod
    def count_occurrences_binary(nums: List[int], target: int) -> int:
        """Count target occurrences using binary search."""
        def find_bound(find_first: bool) -> int:
            left, right = 0, len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target or (
                    not find_first and nums[mid] == target
                ):
                    left = mid + 1
                else:
                    right = mid

            return left

        first = find_bound(True)
        last = find_bound(False)

        return last - first
