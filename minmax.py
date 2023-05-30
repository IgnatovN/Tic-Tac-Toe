from copy import deepcopy

from utils import *


def minimax(input_grid: list, is_maximizing: bool) -> list:
    """Minmax algorithm - recursively evaluates all possible variation nodes and chooses the best one
    :param input_grid: current grid
    :param is_maximizing: whether maximize or minimize
    :return: list of best move parameters, first element is the best possible evaluating score,
     second element is the best move coordinate"""
    # Base case - the game is over, so return the value of the grid
    if game_is_over(input_grid):
        return [evaluate_grid(input_grid), ""]
    # Maximize (computer turn)
    if is_maximizing:
        # The best value starts at the lowest possible value
        best_value = -float("Inf")
        best_move = ""
        # Loop through all the available moves
        for move in available_moves(input_grid):
            # Make a copy of the grid and apply the move to it
            new_grid = deepcopy(input_grid)
            select_space(new_grid, move, "X")
            # Recursively find opponent's best move
            hypothetical_value = minimax(new_grid, False)[0]
            # Update best value if better hypothetical value is found
            if hypothetical_value > best_value:
                best_value = hypothetical_value
                best_move = move
        return [best_value, best_move]
    # Minimize (player turn)
    else:
        # The best value starts at the highest possible value
        best_value = float("Inf")
        best_move = ""
        # Testing all potential moves
        for move in available_moves(input_grid):
            # Copying the grid and making the move
            new_grid = deepcopy(input_grid)
            select_space(new_grid, move, "O")
            # Passing the new grid back to the maximizing player
            hypothetical_value = minimax(new_grid, True)[0]
            # Keeping track of the best value seen so far
            if hypothetical_value < best_value:
                best_value = hypothetical_value
                best_move = move
        return [best_value, best_move]
