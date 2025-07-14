"""
Longest palindromic substring.

Problem Statement:
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

import time

def is_palindrom(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[-1-i]:
            return False
    return True

def longest_palindromic_substring(s):
    """
    Finds the longest palindromic substring within the given string.
    Brute force, O(n³) because of two nested loops + is_palindrom()
    """
    result = ""
    for i in range(len(s)):
        for j in range(len(s)-1, i-1, -1):
            s1 = s[i:j+1]
            if is_palindrom(s1) and len(s1) > len(result):
                result = s1
                break
        if i + len(result) > len(s):
            break
    return result

def longest_palindromic_substring_v2(s):
    """
    Expand around centers approach - O(n²) time, O(1) space
    For each possible center, expand outward while characters match
    """
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # length of palindrome
    
    for i in range(len(s)):
        # Check for odd-length palindromes (center is a single character)
        len1 = expand_around_center(i, i)
        # Check for even-length palindromes (center is between two characters)
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]

def longest_palindromic_substring_v3(s):
    """
    Dynamic Programming approach - O(n²) time, O(n²) space
    dp[i][j] = True if substring s[i:j+1] is a palindrome
    """
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]

def longest_palindromic_substring_v4(s):
    """
    Manacher's Algorithm - O(n) time, O(n) space
    The most efficient algorithm for this problem
    """
    if not s:
        return ""
    
    # Transform string to handle even-length palindromes
    # "babad" becomes "^#b#a#b#a#d#$"
    transformed = "^#" + "#".join(s) + "#$"
    n = len(transformed)
    P = [0] * n  # P[i] = radius of palindrome centered at i
    center = right = 0  # center and right boundary of rightmost palindrome
    
    max_len = 0
    center_index = 0
    
    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i
        
        # If i is within right boundary, we can use previously computed values
        if i < right:
            P[i] = min(right - i, P[mirror])
        
        # Try to expand palindrome centered at i
        while transformed[i + P[i] + 1] == transformed[i - P[i] - 1]:
            P[i] += 1
        
        # If palindrome centered at i extends past right, adjust center and right
        if i + P[i] > right:
            center, right = i, i + P[i]
        
        # Update maximum length palindrome
        if P[i] > max_len:
            max_len = P[i]
            center_index = i
    
    # Extract the longest palindrome from original string
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

def test_all_algorithms():
    """Test all algorithms with the same test cases"""
    test_cases = [
        ("", ""),
        ("a", "a"),
        ("ab", "a"),  # or "b"
        ("aba", "aba"),
        ("abac", "aba"),
        ("cabac", "cabac"),
        ("caba", "aba"),
        ("abaab", "baab"),
        ("babad", "bab"),  # "aba" is also valid
        ("cbbd", "bb"),
        ("racecar", "racecar"),
        ("abcdef", "a"),  # any single character
        ("noon", "noon"),
        ("aabbaa", "aabbaa"),
    ]
    
    algorithms = [
        ("Brute Force O(n³)", longest_palindromic_substring),
        ("Expand Centers O(n²)", longest_palindromic_substring_v2),
        ("Dynamic Programming O(n²)", longest_palindromic_substring_v3),
        ("Manacher's O(n)", longest_palindromic_substring_v4),
    ]
    
    print("Testing all algorithms:")
    print("=" * 50)
    
    for name, func in algorithms:
        print(f"\n{name}:")
        all_passed = True
        for s, expected in test_cases:
            result = func(s)
            # For some cases, multiple answers are valid (e.g., "bab" vs "aba")
            if s == "babad":
                passed = result in ["bab", "aba"]
            elif s == "abcdef":
                passed = len(result) == 1  # any single character is valid
            else:
                passed = result == expected
            
            if not passed:
                print(f"  FAILED: input='{s}', expected='{expected}', got='{result}'")
                all_passed = False
        
        if all_passed:
            print("  All tests PASSED ✓")

def benchmark_algorithms():
    """Benchmark all algorithms with different input sizes"""
    import random
    import string
    
    def generate_test_string(length):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    algorithms = [
        ("Brute Force O(n³)", longest_palindromic_substring),
        ("Expand Centers O(n²)", longest_palindromic_substring_v2),
        ("Dynamic Programming O(n²)", longest_palindromic_substring_v3),
        ("Manacher's O(n)", longest_palindromic_substring_v4),
    ]
    
    test_sizes = [50, 100, 200, 500]
    
    print("\n\nBenchmarking (time in seconds):")
    print("=" * 60)
    print(f"{'Algorithm':<25} {'n=50':<8} {'n=100':<8} {'n=200':<8} {'n=500':<8}")
    print("-" * 60)
    
    for name, func in algorithms:
        times = []
        for size in test_sizes:
            test_string = generate_test_string(size)
            
            start_time = time.time()
            func(test_string)
            end_time = time.time()
            
            times.append(f"{end_time - start_time:.4f}")
        
        print(f"{name:<25} {times[0]:<8} {times[1]:<8} {times[2]:<8} {times[3]:<8}")

# Run tests for the original implementation
print("Original tests:")
assert is_palindrom("")
assert is_palindrom("a")
assert is_palindrom("aa")
assert is_palindrom("aabbaa")
assert not is_palindrom("aaba")
assert not is_palindrom("ab")

assert longest_palindromic_substring("") == ""
assert longest_palindromic_substring("a") == "a"
assert longest_palindromic_substring("ab") == "a"
assert longest_palindromic_substring("aba") == "aba"
assert longest_palindromic_substring("abac") == "aba"
assert longest_palindromic_substring("cabac") == "cabac"
assert longest_palindromic_substring("caba") == "aba"
assert longest_palindromic_substring("abaab") == "baab"

assert longest_palindromic_substring_v2("") == ""
assert longest_palindromic_substring_v2("a") == "a"
assert longest_palindromic_substring_v2("ab") == "a"
assert longest_palindromic_substring_v2("aba") == "aba"
assert longest_palindromic_substring_v2("abac") == "aba"
assert longest_palindromic_substring_v2("cabac") == "cabac"
assert longest_palindromic_substring_v2("caba") == "aba"
assert longest_palindromic_substring_v2("abaab") == "baab"

assert longest_palindromic_substring_v3("") == ""
assert longest_palindromic_substring_v3("a") == "a"
assert longest_palindromic_substring_v3("ab") == "a"
assert longest_palindromic_substring_v3("aba") == "aba"
assert longest_palindromic_substring_v3("abac") == "aba"
assert longest_palindromic_substring_v3("cabac") == "cabac"
assert longest_palindromic_substring_v3("caba") == "aba"
assert longest_palindromic_substring_v3("abaab") == "baab"

assert longest_palindromic_substring_v4("") == ""
assert longest_palindromic_substring_v4("a") == "a"
assert longest_palindromic_substring_v4("ab") == "a"
assert longest_palindromic_substring_v4("aba") == "aba"
assert longest_palindromic_substring_v4("abac") == "aba"
assert longest_palindromic_substring_v4("cabac") == "cabac"
assert longest_palindromic_substring_v4("caba") == "aba"
assert longest_palindromic_substring_v4("abaab") == "baab"

print("All done!")

# Test all new algorithms
test_all_algorithms()

# Benchmark performance
benchmark_algorithms()

print("\n\nAlgorithm Comparison Summary:")
print("=" * 50)
print("1. Brute Force O(n³):      Simple but slow, checks all substrings")
print("2. Expand Centers O(n²):   Intuitive and efficient, good balance")
print("3. Dynamic Programming O(n²): Classic approach, uses more memory")
print("4. Manacher's O(n):        Optimal time complexity, most complex")
print("\nFor interviews: Expand Centers is usually the best choice!")
print("For competitive programming: Manacher's algorithm is optimal.")