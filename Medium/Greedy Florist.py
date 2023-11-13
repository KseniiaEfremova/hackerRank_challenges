def getMinimumCost(k, c):
    # O(nlogn) time
    # O(1) space
    if len(c) <= k:  # if number of friends more than number of flowers
        return sum(c)
    c.sort(reverse=True)
    total_sum = 0
    counter_purchases = k
    prev_purchase = 0
    for flower in c:
        if counter_purchases == 0:
            prev_purchase += 1
            counter_purchases = k
        total_sum += flower * (1 + prev_purchase)
        counter_purchases -= 1
    return total_sum


assert getMinimumCost(3, [1,2,3,4]) == 11
assert getMinimumCost(3, [2,5,6]) == 13
assert getMinimumCost(3, [1,3,5,7,9]) == 29
