def chessboardGame(x, y):
    # O(len(winners)) time
    # O(len(winners)) space
    turn_to_move = 0
    winners = {}
    winner = is_first_win(x,y,turn_to_move,winners)
    if winner == 0:
        return "First"
    return "Second"


def is_first_win(x,y, turn_to_move, winners):
    if (x,y) in winners:
        return winners[(x,y)] ^ turn_to_move
    moves = [(x - 2, y + 1),
             (x - 2, y - 1),
             (x + 1, y - 2),
             (x - 1, y - 2)]
    options_to_move = []
    for move in moves:
        if not (move[0] < 1 or move[0] > 15 or move[1] < 1 or move[1] > 15):
            options_to_move.append(move)

    if len(options_to_move) == 0:
        winners[(x, y)] = 1
        return turn_to_move ^ 1

    for i in range(len(options_to_move)):
        x, y = options_to_move[i]
        winner = is_first_win(x,y,turn_to_move^1, winners)
        if winner == turn_to_move:
            winners[(x, y)] = 1
            return turn_to_move
    winners[(x, y)] = 0
    return turn_to_move ^ 1

print(chessboardGame(5,4))

assert chessboardGame(5,3) == "First"
assert chessboardGame(5,2) == "Second"
assert chessboardGame(8,8) == "First"
assert chessboardGame(2,2) == "Second"
assert chessboardGame(1,1) == "Second"