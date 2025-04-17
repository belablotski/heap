"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[1,4],[0,4]]
Output: [[0,4]]
"""

def merge_intervals_v1(intervals):
    if len(intervals) == 0:
        raise ValueError('Empty input')
    result = []
    intervals = sorted(intervals, key=lambda x: x[0])
    l, r = intervals[0]
    for interval in intervals[1:]:
        if l <= interval[0] <= r:
            r = max(r, interval[1])
        else:
            result.append([l, r])
            l, r = interval
    result.append([l, r])
    return result

def merge_intervals(intervals):
    if len(intervals) == 0:
        raise ValueError('Empty input')
    
    result = []
    intervals = sorted(intervals, key=lambda x: x[0])
    l = r = None

    for interval in intervals:
        if l is not None and r is not None and l <= interval[0] <= r:
            r = max(r, interval[1])
        else:
            if l is not None and r is not None:
                result.append([l, r])
            l, r = interval
            
    result.append([l, r])
    return result

def test_merge_intervals():
    assert merge_intervals([[1,2]]) == [[1,2]]
    assert merge_intervals([[1,2], [2,3]]) == [[1,3]]
    assert merge_intervals([[1,2], [2,3], [1,3]]) == [[1,3]]
    assert merge_intervals([[1,2], [2,3], [1,3], [4,5], [4,6], [5,7]]) == [[1,3], [4,7]]
    assert merge_intervals([[1,2], [2,3], [1,3], [4,5], [4,6], [5,7], [2,6]]) == [[1,7]]
    assert merge_intervals([[1,2], [2,3], [1,3], [4,5], [4,6], [5,7], [2,6], [0,8], [1,9]]) == [[0,9]]
    assert merge_intervals([[1,2], [2,3], [1,3], [4,5], [4,6], [5,7], [2,6], [0,8], [1,9], [13,15], [10,16], [11,14]]) == [[0,9],[10,16]]
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge_intervals([[1,4],[4,5]]) == [[1,5]]
    assert merge_intervals([[1,4],[0,4]]) == [[0,4]]

test_merge_intervals()