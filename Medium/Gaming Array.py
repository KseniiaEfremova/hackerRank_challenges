def gamingArray(arr):
    # n - len(arr)
    # O(n) time
    # O(1) space
    move = 0
    cur_max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > cur_max:
            move ^= 1
            cur_max = arr[i]
    if move == 0:
        return "BOB"
    return "ANDY"


assert gamingArray([2,3,5,4,1]) == "BOB"
assert gamingArray([5,2,6,3,4]) == "ANDY"
assert gamingArray([3,1]) == "BOB"
assert gamingArray([1,3]) == "ANDY"
