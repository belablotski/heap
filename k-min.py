"""
This module provides functions to find the k-th minimum element in a list.
"""

INT_MAX = 999

# This function should be inside the kmin() itself, I externalized it for the testing purposes only.
def put(mins, x):
    if x not in mins:
      for i in range(len(mins)-1, -1, -1):
        if x < mins[i]:
          if i < len(mins) - 1:
            mins[i+1] = mins[i]
          mins[i] = x

def kmin(arr, k):
  mins = [INT_MAX] * k    # optimization: list

  for a in arr:
    put(mins, a)

  return mins[-1]

def tst(arr, k, expected_kmin):
  r = kmin(arr, k)
  assert r == expected_kmin, f"TEST FAILED: Expected {expected_kmin}, got {r}"

def put_tst(arr, x, expected_arr):
  put(arr, x)
  assert arr == expected_arr, f"TEST FAILED: Expected {expected_arr}, got {arr}"

put_tst([9, 9, 9], 1, [1, 9, 9])
put_tst([1, 9, 9], 2, [1, 2, 9])
put_tst([1, 2, 9], 0, [0, 1, 2])
put_tst([0, 1, 2], 0, [0, 1, 2])

tst([1, 2, 3], 2, 2)
tst([3, 2, 1], 2, 2)
tst([1, 2, 1], 1, 1)
tst([1, 2, 1], 2, 2)
tst([1, 2, 1, 3, 1, 4, 5], 3, 3)


print("All tests done!")