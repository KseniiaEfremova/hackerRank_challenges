def twoArrays(k, A, B):
    # O(nlogn) time
    # O(1) space
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


assert twoArrays(4,[1,2,3], [1,2,4]) == "YES"
assert twoArrays(4,[1,2,3], [1,2,1]) == "NO"
assert twoArrays(1,[1,2,3], [1,2,4]) == "YES"
assert twoArrays(20,[1,1,1], [1,2,4]) == "NO"
assert twoArrays(4,[1,2,3], [1,2,4]) == "YES"
assert twoArrays(4,[1,2,3], [1,2,4]) == "YES"