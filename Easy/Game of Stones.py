def gameOfStones2(n):
    # O(n) time
    # O(n) space
    res = [False]
    moves = [-2, -3, -5]
    for k in range(1, n+1):
        has_win_moves = False
        for x in moves:
            move = k + x
            if move < 0:
                continue
            if not res[move]:
                has_win_moves = True
                break
        res.append(has_win_moves)
        print(res)
    if res[n]:
        return "First"
    return "Second"




def gameOfStones(n):
    # O(n) time
    # O(1) space
    res = [False, False, True, True, True]
    if n < len(res):
        if res[n]:
            return "First"
        return "Second"
    moves = [3, 2, 0]
    for k in range(5, n+1):
        has_win_moves = False
        for move in moves:
            if not res[move]:
                has_win_moves = True
                break
        res.append(has_win_moves)
        res.pop(0)
    if res[-1]:
        return "First"
    return "Second"


print(gameOfStones(9))

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



