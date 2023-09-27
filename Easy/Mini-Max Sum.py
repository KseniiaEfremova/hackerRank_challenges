def miniMaxSum(arr):
    # O(nlogn) time
    # O(1) space
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    return min_sum, max_sum


print(miniMaxSum([1,3,5,7,9]))

assert miniMaxSum([1,3,5,7,9]) == (16, 24)