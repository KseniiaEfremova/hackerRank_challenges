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
    winners = {}
    for m in range(n+1):
        if m < 2:
            winners[m] = False
            continue
        moves = [m - 2, m - 3, m - 5]
        for move in moves:
            if move in winners and (winners[move] is False):
                winners[m] = True
                break
            if move < 0:
                winners[m] = True
                break

            if move == 0:
                winners[move] = False
            elif move in winners:
                winners[m] = not winners[move]
            else:
                winners[move] = False
    if winners[n]:
        return "First"
    return "Second"


print(gameOfStones(1))

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




