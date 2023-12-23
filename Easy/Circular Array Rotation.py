def circularArrayRotation(a, k, queries):
    # TC O(n), n - len(a)
    # SC O(n), n - len(a)
    n = len(a)
    k = k % n
    rotated_array = [0 for _ in a]
    for i in range(n):
        rotated_indx = (i + k) % n
        rotated_array[rotated_indx] = a[i]
    return [rotated_array[number] for number in queries]


assert circularArrayRotation([1,2,3,4],2,[0,1]) == [3, 4]
assert circularArrayRotation([1,2,3,4],1,[0,1]) == [4, 1]
assert circularArrayRotation([1,2,3,4],3,[0,1]) == [2, 3]
assert circularArrayRotation([1,2,3,4],4,[0,1]) == [1, 2]
assert circularArrayRotation([1,2,3,4],5,[0,1]) == [4, 1]


