def miniMaxSum(arr):
    # O(n) time
    # O(1) space
    sum_arr = 0
    min_num = 9999999
    max_num = 0
    for number in arr:
        sum_arr += number
        min_num = min(min_num, number)
        max_num = max(max_num, number)

    return sum_arr-max_num, sum_arr-min_num


assert miniMaxSum([1,3,5,7,9]) == (16, 24)