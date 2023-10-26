# True - first wins
# False - second wins
def gameOfStones(n):
    # O(1) time
    # O(len(res)) space
    res = [False, False, True, True, True, True, True]
    if res[n % 7]:
        return "First"
    return "Second"


assert gameOfStones(1) == "Second"
assert gameOfStones(7) == "Second"
assert gameOfStones(8) == "Second"
assert gameOfStones(2) == "First"
assert gameOfStones(4) == "First"
assert gameOfStones(6) == "First"
assert gameOfStones(9) == "First"
assert gameOfStones(22) == "Second"
assert gameOfStones(21) == "Second"
assert gameOfStones(20) == "First"
assert gameOfStones(14) == "Second"
assert gameOfStones(12) == "First"
