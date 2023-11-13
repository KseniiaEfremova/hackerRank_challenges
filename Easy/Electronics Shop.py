def getMoneySpent(keyboards, drives, b):
    # O(nlogn) time
    # O(1) space
    keyboards.sort()
    drives.sort()
    k_pointer = len(keyboards)-1
    d_pointer = 0
    best_purchase = -1
    while k_pointer >= 0 and d_pointer < len(drives):
        temp_sum = keyboards[k_pointer] + drives[d_pointer]
        if temp_sum == b:
            return temp_sum
        if temp_sum < b:
            best_purchase = max(best_purchase, temp_sum)
            d_pointer += 1
        else:
            k_pointer -= 1
    return best_purchase


assert getMoneySpent([40,50,60], [5,8,12], 60) == 58
assert getMoneySpent([3,1], [5,2,8], 10) == 9
assert getMoneySpent([4], [5], 5) == -1
