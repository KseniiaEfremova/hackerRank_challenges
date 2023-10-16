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
    if res[n]:
        return "First"
    return "Second"

print(gameOfStones(5))

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



