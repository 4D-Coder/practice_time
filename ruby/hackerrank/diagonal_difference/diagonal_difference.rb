
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

# Sample Input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# The primary diagonal is:

# 11
#    5
#      -12

# The secondary diagonal is:

#      4
#    5
# 10

# Sum across the secondary diagonal: 4 + 5 + 10 = 19

# Difference: |4 - 19| = 15


def diagonalDifference(arr)
  count = arr.count
  ltr_diag = 0
  rtl_diag = 0

  while count > 0
    arr.each_with_index do |ar, index|
      ltr_diag += ar[index]
      rtl_diag += ar[count - 1]
      count -= 1
    end
  end

  return (ltr_diag - rtl_diag).abs
end

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

p diagonalDifference(arr)


