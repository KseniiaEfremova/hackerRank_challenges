def nimGame(pile):
    # 0(n) time
    # O(1) space
    res = 0
    for one_pile in pile:
        res ^= one_pile
    if res == 0:
        return "Second"
    return "First"


assert nimGame([1,1]) == "Second"
assert nimGame([1,0]) == "First"
assert nimGame([1,1, 1]) == "First"
assert nimGame([1,1, 2]) == "First"
assert nimGame([1,1, 1, 1]) == "Second"
assert nimGame([1,1, 1, 2]) == "First"
assert nimGame([3,5]) == "First"
