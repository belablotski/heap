"""
Given an array of meeting time intervals where each interval consists of a start and end time ([start, end]),
find the minimum number of meeting rooms required.

Example:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation:
We have three meetings:
[0, 30]
[5, 10]
[15, 20]
One room can take [0, 30] then [15, 20].
Another room can take [5, 10].
So we need 2 meeting rooms.
"""

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    # Create a list of all start and end times
    times = []
    for interval in intervals:
        times.append((interval[0], 'start'))
        times.append((interval[1], 'end'))

    # Sort the times
    times.sort(key=lambda x: (x[0], x[1]))

    max_rooms = 0
    current_rooms = 0

    # Iterate through the times
    for time in times:
        if time[1] == 'start':
            current_rooms += 1
            max_rooms = max(max_rooms, current_rooms)
        else:
            current_rooms -= 1

    return max_rooms

assert min_meeting_rooms([[0,30],[5,10],[15,20]]) == 2
assert min_meeting_rooms([[7,10],[2,4]]) == 1
assert min_meeting_rooms([[1,2],[2,3],[3,4],[4,5]]) == 1
assert min_meeting_rooms([[0,5],[10,15],[5,10]]) == 1
assert min_meeting_rooms([[0,10],[5,15],[10,20],[15,25]]) == 3
assert min_meeting_rooms([[1,3],[2,4],[3,5]]) == 2
assert min_meeting_rooms([[1,2],[3,4],[5,6]]) == 1
