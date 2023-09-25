def diagonalDifference(arr):
    # O(len(arr)) time
    # O (1) space
    diagonal_1 = 0
    diagonal_2 = 0
    n = len(arr)
    for i in range(n):
        diagonal_1 += arr[i][i]
        diagonal_2 += arr[n-1 - i][i]
    return abs(diagonal_1-diagonal_2)


print(diagonalDifference([[1,2,3], [1,-2,1], [0,0,0]]))
assert diagonalDifference([[1,2,3], [1,2,3], [0,0,0]]) == 2
assert diagonalDifference([[3,2,3], [1,2,3], [0,-1,0]]) == 0
assert diagonalDifference([[1,2,3], [1,-2,1], [0,0,0]]) == 2
assert diagonalDifference([[1,2,3], [1,2,3], [0,0,0]]) == 2