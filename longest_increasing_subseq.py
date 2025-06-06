"""
Given an integer array nums, find the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence 
of 1 [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3].
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.
"""

def longest_inc_seq(arr):

    def lis(i, prev_el):
        if i >= len(arr):
            return 0
        if prev_el is None or prev_el < arr[i]:
            return max(1 + lis(i+1, arr[i]), lis(i+1, prev_el))
        else:
            return lis(i+1, prev_el)

    return lis(0, None)

def test_longest_inc_seq():
    assert longest_inc_seq([5,2,0,4,5,6]) == 4
    assert longest_inc_seq([10,9,2,5,3,7,101,18]) == 4
    assert longest_inc_seq([0,1,0,3,2,3]) == 4
    assert longest_inc_seq([0,1,0,3,2,3,5,1,2,3,4,5,6]) == 7
    assert longest_inc_seq([7, 7, 7]) == 1
    assert longest_inc_seq([0,1,0,3,2,3,5,1,2,3,4,5,6,8,9,10,7,8,9,10,11,12]) == 13
    assert longest_inc_seq([0,1,0,3,2,3,5,1,2,3,4,5,6,8,9,10,7,11,12,12,13,14]) == 14

test_longest_inc_seq()