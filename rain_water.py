"""
The Problem: Trapping Rain Water
You are given a non-negative integer array height representing an elevation map where the width of each bar is 1.
Your task is to compute how much water it can trap after raining.

Examples:

Input: heights = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

# wall, ~ water

       #
   #~~~##~#
 #~##~######
010210132121


Input: heights = [4,2,0,3,2,5]
Output: 9

     #
#~~~~#
#~~#~#
##~###
##~###
420325
"""

def count_level(heights, level):
    if level == 0 or level > max(heights):
        return 0
    else:
        total = count = 0
        first_wall_found = False
        for h in heights:
            if h >= level:
                if not first_wall_found:
                    first_wall_found = True
                else:
                    total += count
                count = 0
            else:
                count += 1
    return total

def count_reservoir(heights):
    count = 0
    for level in range(max(heights)):
        count += count_level(heights, level + 1)
    return count


if __name__ == "__main__":
    assert count_level([0, 0, 0], 0) == 0
    assert count_level([0, 0, 0], 1) == 0
    assert count_level([1, 0, 0], 1) == 0
    assert count_level([1, 1, 0], 1) == 0
    assert count_level([1, 0, 1], 1) == 1
    assert count_level([1, 1, 1], 1) == 0
    assert count_level([0, 1, 1], 1) == 0
    assert count_level([0, 0, 1], 1) == 0
    assert count_level([0, 1, 0, 0, 1, 0, 1], 1) == 3
    assert count_level([0, 1, 0, 0, 1, 0, 0], 1) == 2
    assert count_level([0, 1, 0, 1, 1, 0, 0], 1) == 1
    assert count_level([0, 1, 1, 1, 1, 1, 0], 1) == 0

    assert count_level([0, 1, 2, 1, 2, 1, 0], 1) == 0
    assert count_level([0, 1, 2, 1, 2, 1, 0], 2) == 1
    assert count_reservoir([0, 1, 2, 1, 2, 1, 0]) == 1

    assert count_level([0, 1, 2, 3, 2, 1, 4], 1) == 0
    assert count_level([0, 1, 2, 3, 2, 1, 4], 2) == 1
    assert count_level([0, 1, 2, 3, 2, 1, 4], 3) == 2
    assert count_reservoir([0, 1, 2, 3, 2, 1, 4]) == 3

    assert count_level([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 0) == 0
    assert count_level([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 1) == 2
    assert count_level([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 2) == 4
    assert count_level([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 3) == 0
    assert count_reservoir([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    assert count_level([4, 2, 0, 3, 2, 5], 0) == 0
    assert count_level([4, 2, 0, 3, 2, 5], 1) == 1
    assert count_level([4, 2, 0, 3, 2, 5], 2) == 1
    assert count_level([4, 2, 0, 3, 2, 5], 3) == 3
    assert count_level([4, 2, 0, 3, 2, 5], 4) == 4
    assert count_level([4, 2, 0, 3, 2, 5], 5) == 0
    assert count_reservoir([4, 2, 0, 3, 2, 5]) == 9
