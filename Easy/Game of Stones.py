def gameOfStones(n):
    # O(3**n) time
    # O()
    turn_to_move = 0
    winners = {}
    winner = try_all_options(n, turn_to_move, winners)
    if winner == 0:
        return "First"
    return "Second"


def try_all_options(n, turn_to_move, winners):
    if n in winners:
        return winners[n] ^ turn_to_move
    if n == 0 or n == 1:
        winners[n] = 1
        return turn_to_move ^ 1
    if 1 < n < 7:
        winners[n] = 0
        return turn_to_move

    moves = [n - 2, n - 3, n - 5]
    for move in moves:
        winner = try_all_options(move, turn_to_move ^ 1, winners)
        if winner == turn_to_move:
            winners[move] = 1
            return turn_to_move
    winners[n] = 0
    return turn_to_move ^ 1


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
