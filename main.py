# NOTE: DO NOT TOUCH ANYTHING IN THIS FILE

from solutions.problem_1 import Problem1
from solutions.problem_2 import Problem2

# Test runner
if __name__ == "__main__":
    # Problem 1 tests
    print("=== Problem 1: Count Target Occurrences ===")
    nums1_1 = [1, 2, 2, 2, 3, 4, 5]
    print(f"Test 1.1 Linear: {Problem1.count_occurrences_linear(nums1_1, 2)} (Expected: 3)")
    print(f"Test 1.1 Binary: {Problem1.count_occurrences_binary(nums1_1, 2)} (Expected: 3)")
    
    nums1_2 = [1, 1, 1, 1, 1]
    print(f"Test 1.2 Linear: {Problem1.count_occurrences_linear(nums1_2, 1)} (Expected: 5)")
    print(f"Test 1.2 Binary: {Problem1.count_occurrences_binary(nums1_2, 1)} (Expected: 5)")
    
    # Problem 2 tests
    print("\n=== Problem 2: Find Missing Element ===")
    nums2_1 = [1, 2, 3, 4, 6]
    print(f"Test 2.1 Linear: {Problem2.find_missing_element_linear(nums2_1)} (Expected: 5)")
    print(f"Test 2.1 Binary: {Problem2.find_missing_element_binary(nums2_1)} (Expected: 5)")
    
    nums2_2 = [2, 3, 4, 5, 6]
    print(f"Test 2.2 Linear: {Problem2.find_missing_element_linear(nums2_2)} (Expected: 1)")
    print(f"Test 2.2 Binary: {Problem2.find_missing_element_binary(nums2_2)} (Expected: 1)")