"""
Problem Statement:

There are n students in a class. Some of them are friends, while others are not. 
The friendship relationship is transitive. This means if A is a friend of B, and B is a friend of C, 
then A is indirectly a friend of C. A friend circle is a group of students who are directly or indirectly friends.

You are given an n x n matrix M representing the friendship relationship where M[i][j] = 1 if the i-th and j-th 
students are direct friends, and M[i][j] = 0 otherwise. The diagonal elements are always 1 (every student is a friend 
of themselves).

Write a function that returns the total number of friend circles in the class.

Example 1:

Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]

Output: 2
Explanation: The 0th and 1st students are direct friends, so they are in the same friend circle. The 2nd student is not friends with anyone, so they are in their own friend circle. Therefore, there are 2 friend circles.


Example 2:

Input:
[[1,1,1],
 [1,1,1],
 [1,1,1]]

Output: 1
Explanation: All students are directly or indirectly friends, so they are all in the same friend circle.


Example 3:

Input:
[[1,1,1,0],
 [1,1,0,0],
 [1,0,1,0],
 [0,0,0,1]]

Output: 2
Explanation: 0, 1 and 2 are in the same friend circle, and 3 is in another friend circle. 
"""

def find_circle_num_v1(M):
    if not M:
        return 0

    n = len(M)
    visited = [False] * n
    circles = 0

    def dfs(i):
        for j in range(n):
            if M[i][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            circles += 1

    return circles

def find_circle_num_v2(M):

    visited = [False] * len(M)

    def find_circle(i):
        if not visited[i]:
            visited[i] = True
            for j in range(len(M[i])):
                if M[i][j]:
                    find_circle(j)

    cnt = 0

    for person in range(len(visited)):
        if not visited[person]:
            find_circle(person)
            cnt += 1

    return cnt

def test_find_circle_num():
    assert find_circle_num([[1,1,0],[1,1,0],[0,0,1]]) == 2
    assert find_circle_num([[1,1,1],[1,1,1],[1,1,1]]) == 1
    assert find_circle_num([[1,1,1,0],[1,1,0,0],[1,0,1,0],[0,0,0,1]]) == 2
    assert find_circle_num([[1]]) == 1
    assert find_circle_num([]) == 0
    print("All tests passed.")

def find_circle_num(M):
    return find_circle_num_v2(M)

if __name__ == "__main__":
    test_find_circle_num()

