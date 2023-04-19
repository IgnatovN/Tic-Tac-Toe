def print_grid(grid: list) -> None:
    """
    Prints the grid with actual spaces
    :param grid: list of grid actual values
    :return: none, grid print during the function running
    """
    print(f"""
    |-------------|
    | Tic Tac Toe |
    |-------------|
    |             |
    |  {grid[0][0]} | {grid[0][1]} | {grid[0][2]}  |
    | ———|———|——— |
    |  {grid[1][0]} | {grid[1][1]} | {grid[1][2]}  |
    | ———|———|——— |
    |  {grid[2][0]} | {grid[2][1]} | {grid[2][2]}  |
    |             |
    |-------------|
    """)


def select_space(grid: list, move: int, turn: str) -> bool:
    """
    Mark space of grid with сorresponding symbol
    :param grid: list of grid actual values
    :param move: space coordinate to mark
    :param turn: value to be marked
    :return: bool value if selected space is correct
    """
    # Check if selected space can be marked
    if move not in range(1, 10):
        return False

    # Define indexes to change in grid
    row = int((move - 1) / 3)
    col = (move - 1) % 3

    # Change value
    if grid[row][col] != "X" and grid[row][col] != "O":
        grid[row][col] = turn
        return True
    else:
        return False


def available_moves(grid: list) -> list:
    """
    Defines open spaces
    :param grid: list of grid actual values
    :return: list of open spaces
    """
    # Check if space not yet marked with X or O
    moves = []
    for row in grid:
        for col in row:
            if col != "X" and col != "O":
                moves.append(int(col))
    return moves


def has_won(grid: list, player: str) -> bool:
    """
    Check whether player won
    :param grid: list of grid actual values
    :param player: player's symbol (X or Y) to be checked
    :return: bool value whether player already won or not
    """
    # Check for win by horizontal row
    for row in grid:
        if row.count(player) == 3:
            return True
    # Check for win by vertical row
    for i in range(3):
        if grid[0][i] == player and grid[1][i] == player and grid[2][i] == player:
            return True
    # Check for win by \ diagonal row
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    # Check for win by / diagonal row
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True

    return False


def game_is_over(grid: list) -> bool:
    """
    Check for three conditions of game finishing
    :param grid: list of grid actual values
    :return: bool value whether game ended or not
    """
    return has_won(grid, "X") or has_won(grid, "O") or len(available_moves(grid)) == 0


def evaluate_grid(grid: list) -> int:
    """
    Evaluate result of finished game
    :param grid: list of grid actual values
    :return: 1, -1 or 0 1 indicates win of X player, -1 indicates win of O player, 0 indicates draw
    """
    if has_won(grid, "X"):
        return 1
    elif has_won(grid, "O"):
        return -1
    else:
        return 0
