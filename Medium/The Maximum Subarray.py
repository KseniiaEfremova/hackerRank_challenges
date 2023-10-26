def maxSubsequences(arr):
    # n - len(arr)
    # O(n) time
    # O(n) space
    max_subsequences = 0
    for num in arr:
        if num > 0:
            max_subsequences += num
    if not max_subsequences:
        return max(arr)
    return max_subsequences


def maxSubarray(arr):
    # n - len(arr)
    # O(n**2) time
    # O(n) space
    len_subarray = 1
    max_subarray = sum(arr)
    while len_subarray <= len(arr):
        temp_subarray = sum(arr[: len_subarray-1])
        for i in range(len(arr) - len_subarray + 1):
            temp_subarray += arr[i+len_subarray-1]
            max_subarray = max(max_subarray, temp_subarray)
            temp_subarray -= arr[i]
        len_subarray += 1

    return [max_subarray, maxSubsequences(arr)]


assert maxSubarray([-1,2,3,-4,5,10]) == [16,20]
assert maxSubarray([1,2,3,4]) == [10, 10]
assert maxSubarray([2, -1, 2, 3, 4, -5]) == [10, 11]
assert maxSubarray([-2, -3, -1, -4, -6]) == [-1, -1]
assert maxSubarray([1, -100, 3]) == [3, 4]

