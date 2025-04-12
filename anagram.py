import re
from collections import Counter

def is_anagram_v1(s1, s2):
    """
    Check if two strings are anagrams of each other.
    
    Args:
    s1 (str): First string.
    s2 (str): Second string.

    Returns:
    bool: True if s1 and s2 are anagrams, False otherwise.
    """
    # Remove spaces and convert to lowercase
    s1 = re.sub(r'[^a-zA-Z]', '', s1).lower()
    s2 = re.sub(r'[^a-zA-Z]', '', s2).lower()

    # Sort the characters of both strings and compare
    return sorted(s1) == sorted(s2)

def is_anagram_v2(s1, s2):
    """
    Check if two strings are anagrams of each other using Counter.
    
    Args:
    s1 (str): First string.
    s2 (str): Second string.

    Returns:
    bool: True if s1 and s2 are anagrams, False otherwise.
    """
    # Remove spaces and non-alphabetic characters, and convert to lowercase
    s1 = re.sub(r'[^a-zA-Z]', '', s1).lower()
    s2 = re.sub(r'[^a-zA-Z]', '', s2).lower()

    # Compare character counts using Counter
    return Counter(s1) == Counter(s2)

def is_anagram(s1, s2):
    return is_anagram_v2(s1, s2)

def tests():
    """
    Run tests to validate the is_anagram function.
    """
    assert is_anagram("listen", "silent")
    assert is_anagram("triangle", "integral")
    assert not is_anagram("apple", "pale")
    assert is_anagram("anagram", "nag a ram")
    assert not is_anagram("rat", "car")
    assert not is_anagram("hello", "world")
    assert not is_anagram("python", "java")

    assert is_anagram("New York Times", "monkeys write")
    assert is_anagram("Church of Scientology", "rich-chosen goofy cult")
    assert is_anagram("McDonald's restaurants", "Uncle Sam's standard rot")
    assert is_anagram("coronavirus", "carnivorous")
    assert is_anagram("She Sells Sanctuary", "Santa; shy, less cruel" or "Satan; cruel, less shy")
    assert is_anagram("evil", "vile")
    assert is_anagram("a gentleman", "elegant man")
    assert is_anagram("silent", "listen")
    assert is_anagram("astronomer", "moon starer")
    assert is_anagram("restful", "fluster")
    assert is_anagram("cheater", "teacher")
    assert is_anagram("funeral", "real fun")
    assert is_anagram("adultery", "true lady")
    assert is_anagram("forty five", "over fifty")
    assert is_anagram("Santa", "Satan")
    assert is_anagram("William Shakespeare", "I am a weakish speller")
    assert is_anagram("Madam Curie", "Radium came")
    assert is_anagram("George Bush", "He bugs Gore")
    assert is_anagram("Tom Marvolo Riddle", "I am Lord Voldemort")
    assert is_anagram("The Morse code", "Here come dots")

    print("All tests passed!")

if __name__ == "__main__":
    tests()