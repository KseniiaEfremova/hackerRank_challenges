def maxMin(k, arr):
    # n - len(arr)
    # O(nlogn) time
    # O(1) space
    arr.sort()
    rigth_pointer = k - 1
    min_unfairness = arr[-1]
    for i in range(len(arr)-rigth_pointer):
        cur = arr[rigth_pointer] - arr[i]
        min_unfairness = min(min_unfairness, cur)
        rigth_pointer += 1
    return min_unfairness


assert maxMin(3, [10,100,300,200,1000,20,30]) == 20
assert maxMin(2, [1,4,7,2]) == 1
assert maxMin(2, [1,2,1,2,1]) == 0

