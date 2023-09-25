def findMedian(arr):
    # O(nlogn) time
    # O(1) spice
    arr.sort()
    return arr[len(arr) // 2]


assert findMedian([1,2,3]) == 2
assert findMedian([1,1,3]) == 1
assert findMedian([2,2,1]) == 2
assert findMedian([1,2,3, 3, 4]) == 3