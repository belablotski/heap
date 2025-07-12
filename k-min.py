# not finished yet

INT_MAX = 999

def put(mins, x):
    for i in range(len(mins)-1, -1, -1):
      if x < mins[i]:
        if i < len(mins) - 1:
          mins[i+1] = mins[i]
        mins[i] = x

def kmin(arr, k):
  mins = [INT_MAX] * 5    # optimization: list

  for a in arr:
    put(a)

  return 0

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

#tst([1, 2, 3], 2, 2)
#tst([3, 2, 1], 2, 2)

print("All tests done!")