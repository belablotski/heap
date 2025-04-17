"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course 
bi first if you want to take course ai.

Return the ordering of courses you should take to finish all courses.
If it is impossible to finish all courses (due to a cycle), return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. 
Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. 
Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
"""

import itertools

def cource_schedule(num_of_courses, prereq):
    def get_all_dependencies(course):
        return [p[1] for p in prereq if p[0] == course]

    courses = list(range(num_of_courses))
    schedule = []

    repeat_cnt = 0
    while courses:
        c = courses.pop(0)
        dep_satisfied = True
        for d in get_all_dependencies(c):
            if d not in schedule:
                dep_satisfied = False
                break
        if dep_satisfied:
            schedule.append(c)
            repeat_cnt = 0 
        else:
            courses.append(c)
            repeat_cnt += 1
            if repeat_cnt >= len(courses):
                return []

    return schedule

def test_cource_schedule():
    assert cource_schedule(3, []) in [list(x) for x in itertools.permutations([0, 1, 2])]
    assert cource_schedule(3, [[1, 0], [2,1]]) == [0, 1, 2]
    assert cource_schedule(3, [[1, 0], [2,1], [0, 2]]) == []
    assert cource_schedule(4, [[1,0],[2,0],[3,1],[3,2]]) in ([0,1,2,3], [0,2,1,3])
    assert cource_schedule(4, [[1,0],[2,0],[3,1],[3,2],[3,0]]) in ([0,1,2,3], [0,2,1,3])
    assert cource_schedule(4, [[1,0],[2,0],[3,1],[3,2],[3,0],[2,1]]) == [0,1,2,3]
    print('All tests passed')

test_cource_schedule()
