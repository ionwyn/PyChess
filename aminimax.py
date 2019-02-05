from .test_helpers import heuristic_gen, get_successors

def minimax(board_state, heuristic, next_moves, current_depth=0, max_depth=4):
    current_depth += 1
    if current_depth == max_depth:
        # get heuristic of each node
        return next(heuristic)
    if current_depth % 2 == 0:
        # min player's turn
        return min([minimax(node, heuristic, current_depth, max_depth) for node in next_moves()])
    else:
        # max player's turn
        return max([minimax(node, heuristic, current_depth, max_depth) for node in next_moves()])