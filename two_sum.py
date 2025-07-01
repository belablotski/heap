from itertools import combinations

"""
The Problem: Two Sum
Given an array of integers nums and an integer target, return the indices of the two numbers 
in the array that add up to the target.

You can assume that each input will have exactly one solution, and you may not use the same element twice. 
You can return the answer in any order.

Example:

Input: nums = [2, 7, 11, 15], target = 9

Output: [0, 1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def two_sum_basic(arr, target):
    if arr and len(arr) >= 2:
        for c in list(combinations(range(len(arr)), 2)):
            if arr[c[0]] + arr[c[1]] == target:
                return (c[0], c[1])
    return None

def two_sum_optimized(arr, target):
    if not arr or len(arr) < 2:
        return None
    
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

two_sum = two_sum_optimized

if __name__ == "__main__":
    # Edge cases
    assert two_sum(None, 1) is None
    assert two_sum([], 1) is None
    assert two_sum([1], 1) is None
    
    # Basic functionality
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([2, 7, 11, 15], 22) == (1, 3)
    
    # Two elements array
    assert two_sum([3, 3], 6) == (0, 1)
    assert two_sum([1, 2], 3) == (0, 1)
    assert two_sum([5, -2], 3) == (0, 1)
    
    # Negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == (2, 4)
    assert two_sum([-3, 4, 3, 90], 0) == (0, 2)
    assert two_sum([1, -1, 0], 0) == (0, 1)
    
    # Zero target
    assert two_sum([0, 0], 0) == (0, 1)
    assert two_sum([1, -1], 0) == (0, 1)
    assert two_sum([5, -5, 3], 0) == (0, 1)
    
    # Larger arrays
    assert two_sum([1, 2, 3, 4, 5, 6], 10) == (3, 5)
    assert two_sum([10, 20, 30, 40, 50], 90) == (3, 4)
    assert two_sum([1, 3, 5, 7, 9, 11], 16) in [(2, 5), (3, 4)]
    
    # No solution cases (should return None based on current implementation)
    assert two_sum([1, 2, 3], 10) is None
    assert two_sum([5, 5, 5], 6) is None
    
    # Large numbers
    assert two_sum([1000000, 2000000, 3000000], 5000000) == (1, 2)
    
    # Duplicates with different targets
    assert two_sum([2, 2, 2, 2], 4) == (0, 1)
    assert two_sum([1, 1, 2, 2, 3], 4) in [(0, 4), (1, 4), (2, 3)]
    
    # Mixed positive and negative
    assert two_sum([-1, 0, 1, 2, -1, -4], -2) == (0, 4)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    
    print("All test cases passed!")
