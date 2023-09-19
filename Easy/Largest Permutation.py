import bisect


def largestPermutation(k, arr):
    if k >= len(arr):
        arr.sort(reverse=True)
        return arr
    value_indexes_pairs = []
    for i in range(len(arr)):
        value_indexes_pairs.append((arr[i], i))
    value_indexes_pairs.sort()
    j = 0
    while k > 0 and j < len(arr):
        # find values to swap
        first_value_arr = arr[j]
        max_val = value_indexes_pairs[-1 - j]
        if first_value_arr == max_val[0]:
            j += 1
            continue
        # swap values in array
        arr[j] = max_val[0]
        arr[max_val[1]] = first_value_arr
        # swap indexes in list of tuples
        indx = bisect.bisect_left(value_indexes_pairs, first_value_arr, key=lambda tup: tup[0])
        value_indexes_pairs[-1 - j] = (max_val[0], value_indexes_pairs[indx][1])
        value_indexes_pairs[indx] = (value_indexes_pairs[indx][0], max_val[1])
        j += 1
        k -= 1
    return arr


assert largestPermutation(1, [1,2,3,4]) == [4,2,3,1]
assert largestPermutation(2, [1,2,3,4]) == [4,3,2,1]
assert largestPermutation(1, [4, 2, 3, 5, 1]) == [5, 2, 3, 4, 1]
assert largestPermutation(1, [3,2,1]) == [3,2,1]
assert largestPermutation(3, [1,2,3,4]) == [4,3,2,1]
assert largestPermutation(10, [1,2,3,4]) == [4,3,2,1]
assert largestPermutation(1, [1]) == [1]
assert largestPermutation(1, [10, 9, 8, 20]) == [20, 9,8,10]
assert largestPermutation(2, [10, 9, 8, 20]) == [20, 10,8,9]
assert largestPermutation(1, [5, 1, 2, 3, 4]) == [5, 4, 2, 3, 1]
