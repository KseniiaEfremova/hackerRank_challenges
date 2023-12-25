def circularArrayRotation(a, k, queries):
    # TC O(n), n - len(queries)
    # SC O(n), n - len(queries)
    n = len(a)
    k = k % n
    res = []
    for num in queries:
        rotated_indx = (num - k) % n
        res.append(a[rotated_indx])
    return res


assert circularArrayRotation([1,2,3,4],2,[0,1]) == [3, 4]
assert circularArrayRotation([1,2,3,4],1,[0,1]) == [4, 1]
assert circularArrayRotation([1,2,3,4],3,[0,1]) == [2, 3]
assert circularArrayRotation([1,2,3,4],4,[0,1]) == [1, 2]
assert circularArrayRotation([1,2,3,4],5,[0,1]) == [4, 1]
