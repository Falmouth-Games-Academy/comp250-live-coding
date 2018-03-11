import random


def heuristic(board):
    for y in xrange(6):
        for x in xrange(7):
            if board.get_square(x, y) != 0:
                return (6-y) / 8.0


def minimax(board, depth):
    result = board.get_result(2)
    if result is not None:
        return result
    elif depth == 0:
        return heuristic(board)
    elif board.current_player == 2:
        best_value = -1000
        for move in board.get_moves():
            board.do_move(move)
            v = minimax(board, depth-1)
            board.undo_move(move)
            best_value = max(best_value, v)
            if best_value >= 1:
                return best_value
        return best_value
    elif board.current_player == 1:
        best_value = 1000
        for move in board.get_moves():
            board.do_move(move)
            v = minimax(board, depth-1)
            board.undo_move(move)
            best_value = min(best_value, v)
            if best_value <= -1:
                return best_value
        return best_value


def choose_move(board):
    """ Takes a game board, and returns a move to play
    """

    best_value = -1000
    best_moves = []

    for move in board.get_moves():
        board.do_move(move)
        v = minimax(board, 0)
        print move, v
        board.undo_move(move)
        if v > best_value:
            best_value = v
            best_moves = [move]
        elif v == best_value:
            best_moves.append(move)

    print

    return random.choice(best_moves)
