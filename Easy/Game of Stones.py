def gameOfStones2(n):
    # O(n) time
    # O(n) space
    winners = {}
    winner = is_first_win(n, winners)
    if winner:
        return "First"
    return "Second"


def is_first_win(n, winners):
    if n in winners:
        return winners[n]
    if n == 0:
        winners[n] = False
        return False

    moves = [n - 2, n - 3, n - 5]
    for move in moves:
        if move >= 0:
            is_win = not is_first_win(move, winners)
            if is_win:
                winners[n] = is_win
                return is_win
    winners[n] = False
    return False


def gameOfStones(n):
    # O(n) time
    # O(n) space
    res = []
    for k in range(n+1):
        moves = [k-2, k-3, k-5]
        all_false = True
        for move in moves:
            if move == 0 or (len(res) >= move > 0 and not res[move]):
                res.append(True)
                all_false = False
                break
        if all_false:
            res.append(False)
    if res[n]:
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



