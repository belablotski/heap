from datetime import datetime

def top_n_v1(data, n):
    """
    Return the top n elements from the data list.
    
    :param data: List of elements to be sorted
    :param n: Number of top elements to return
    :return: List of top n elements
    """
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    return sorted(data, reverse=True)[:n]

class NSet(object):
    def __init__(self, size):
        self.data = set()
        self.size = size

    def add(self, value):
        self.data.add(value)
        if len(self.data) > self.size:
            self.data.remove(min(self.data))
    
    def to_sorted_list(self, reverse=True):
        return sorted(self.data, reverse=reverse)

def top_n_v2(data, n):
    """
    Return the top n elements from the data list (without sorting).
    
    :param data: List of elements
    :param n: Number of top elements to return
    :return: List of top n elements
    """
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    max_elements = NSet(n)

    for d in data:
        max_elements.add(d)
    
    return max_elements.to_sorted_list(reverse=True)

def top_n(data, n):
    result1 = top_n_v1(data, n)
    result2 = top_n_v2(data, n)
    assert result1 == result2, f"Results do not match: {result1} != {result2}"
    print(f"Top {n} of {data} elements: {result1}")
    return result1

def tests():
    """
    Run tests to validate the top_n function.
    """
    assert top_n([1, 2, 3, 4, 5], 3) == [5, 4, 3]
    assert top_n([5, 4, 3, 2, 1], 2) == [5, 4]
    assert top_n([1, 2, 3], 0) == []
    assert top_n([], 3) == []
    assert top_n([1], 1) == [1]
    assert top_n([1, 2, 3], 5) == [3, 2, 1]
    assert top_n([5, 3, 8, 6, 2], 2) == [8, 6]
    assert top_n([1, 2, 3, 4, 5], 1) == [5]
    assert top_n([1, 2, 3], 2) == [3, 2]
    assert top_n([1, 2, 3], 3) == [3, 2, 1]
    assert top_n([1, 2, 3], 4) == [3, 2, 1]
    assert top_n([1, 2, 3], 0) == []
    
    try:
        top_n("not a list", 3)
    except ValueError as e:
        assert str(e) == "Data must be a list."
    
    try:
        top_n([1, 2, 3], -1)
    except ValueError as e:
        assert str(e) == "n must be a non-negative integer."

def load_tests(func, repetitions=100):
    t0 = datetime.now()
    for r in range(repetitions):
        data = [i for i in range(1000000)]
        func(data, 10)
    t1 = datetime.now()
    print(f"Loaded tests completed with {repetitions} in {t1 - t0} seconds.")

if __name__ == "__main__":
    tests()
    print("All tests passed.")

    load_tests(top_n_v1)
    load_tests(top_n_v2)