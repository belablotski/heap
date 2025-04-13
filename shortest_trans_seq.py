"""
Problem Statement:

Given a beginWord, an endWord, and a wordList of valid words, find the length of the shortest transformation 
sequence from beginWord to endWord such that:

Only one letter can be changed at a time.
Each transformed word must exist in the wordList.1 Note that the beginWord is not required to be in the wordList.

Example 1:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

Example 2:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

def str_cmp_1(s1, s2):
    """Compares two strings and returns True if they are different by exactly 1 symbol."""
    diff_found = False
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff_found:
                    return False
                else:
                    diff_found = True
        return diff_found
    else:
        return False

def build_graph(word_list):
    """Builds graph adjacency matrix."""

    sz = len(word_list)
    result = [[0 for i in range(sz)] for j in range(sz)]
    # TODO: optimize, the matrix is symmetric
    for i in range(sz):
        for j in range(sz):
            result[i][j] = str_cmp_1(word_list[i], word_list[j])
    return result

def shortest_path_bfs(stop_v, G):
    """Finds the shortest path to stop_v in graph g defined by adjucency matrix."""
    
    def get_neighbors(i):
        result = []
        for j in range(len(G)):
            if G[i][j]:
                result.append(j)
        return result
    
    sz = len(G)
    paths_to_stop_v = [None for i in range(sz)]
    paths_to_stop_v[stop_v] = 0
    neighbors = [(x, 1) for x in get_neighbors(stop_v)]
    while neighbors:
        v, level = neighbors.pop(0)
        if paths_to_stop_v[v] is None or paths_to_stop_v[v] > level:
            paths_to_stop_v[v] = level
            neighbors += [(x, level+1) for x in get_neighbors(v)]
    return paths_to_stop_v

def shortest_transformation_seq(start_word, stop_word, word_list):
    wl = [start_word] + word_list
    stop_v = wl.index(stop_word)
    G = build_graph(wl)
    return shortest_path_bfs(stop_v, G)[0]

def test_str_cmp_1():
    assert str_cmp_1("hit", "hot")
    assert str_cmp_1("dog", "log")
    assert str_cmp_1("cat", "bat")

    assert not str_cmp_1("hit", "lot")
    assert not str_cmp_1("dog", "cat")
    assert not str_cmp_1("abc", "xyz")

    assert not str_cmp_1("hit", "hit")
    assert not str_cmp_1("dog", "dog")

    assert not str_cmp_1("hit", "hitting")
    assert not str_cmp_1("dog", "dogs")
    print("All tests for str_cmp_1(str, str) passed")

def test_build_graph():
    g = [[0, 1, 0, 1, 0, 0],
         [1, 0, 1, 1, 0, 0],
         [0, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 1],
         [0, 0, 1, 0, 1, 0]]
    assert build_graph(["hot","dot","dog","lot","log","cog"]) == g

    g = [[0, 1, 1, 0],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [0, 0, 1, 0]]
    assert build_graph(["abc", "abd", "abe", "zbe"]) == g

    print("All tests for build_graph(list) passed")

def test_shortest_path_bfs():
    G = [[0, 1, 0],
         [1, 0, 1],
         [0, 1, 0]]
    assert shortest_path_bfs(2, G) == [2, 1, 0]

    # 
    # A -- B -- C -- D
    #  \------E-----/
    # 
    G = [[0, 1, 0, 0, 1],
         [1, 0, 1, 0, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 0, 1, 0]]
    assert shortest_path_bfs(3, G) == [2, 2, 1, 0, 1]

    # 
    # A -- B    C -- D
    #  \------E-----/
    # 
    G = [[0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 0, 1, 0]]
    assert shortest_path_bfs(3, G) == [2, 3, 1, 0, 1]

    # 
    # A -- B    C -- D
    #  \------E-----/
    # 
    G = [[0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 0, 1, 0]]
    assert shortest_path_bfs(2, G) == [3, 4, 0, 1, 2]

    print("All tests for shortest_path_bfs(int, list[list[int]]) passed")

def test_shortest_transformation_seq():
    assert shortest_transformation_seq("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 4

test_str_cmp_1()
test_build_graph()
test_shortest_path_bfs()
test_shortest_transformation_seq()
