def getWays(n, c):
    # m - len(c)
    # O(n*m) time
    # O(n) space
    ways = [0 for _ in range(n+1)]
    ways[0] = 1
    for coin in c:
        for amount in range(n+1):
            if amount >= coin:
                ways[amount] += ways[amount-coin]
    return ways[n]
