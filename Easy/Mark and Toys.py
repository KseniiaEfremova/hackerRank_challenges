def maximumToys(prices, k):
    # O(nlogn) time
    # O(1) space
    prices.sort()
    total_price = 0
    max_toys = 0
    for price in prices:
        total_price += price
        if total_price > k:
            return max_toys
        max_toys += 1
    return max_toys


assert maximumToys([1,2,3,4,5,10], 6) == 3
assert maximumToys([1,2,3,4,5,10], 5) == 2
assert maximumToys([1,2,3,4,5,10], 0) == 0
assert maximumToys([1,2,3,4,5,10], 16) == 5
assert maximumToys([1,2,3,4,5,10], 60) == 6
assert maximumToys([1], 1) == 1



