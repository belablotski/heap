# Longest monotone sequence

def lms(arr):
  result = 0
  if arr:
    prev = arr[0]
    curr_len = 1
    for a in arr[1:]:
      if prev <= a:
        curr_len += 1
      else:
        if curr_len > result:
          result = curr_len
        curr_len = 1
      prev = a
    if curr_len > result:
      result = curr_len
  return result

def tst(arr, expected_lms_len):
  r = lms(arr)
  assert r == expected_lms_len, f"TEST FAILED: Expected {expected_lms_len}, got {r}"

tst([], 0)
tst([1], 1)
tst([1, 1, 2, 1, 2, 1, 2, 3, 3, 3], 5)
tst([1, 2, 3], 3)
tst([1, 2, 3, 1, 2, 3], 3)
tst([1, 1, 1], 3)
tst([1, 2, 1, 5, 1, 7, 1, 9, 1], 2)
print("All tests passed")
