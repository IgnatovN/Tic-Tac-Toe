from utils import *
from minmax import minimax

# Initialize grid with coordinates
my_grid = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]


def main():
    order = input('Choose your turn order (1 or 2): ')

    # The game (player makes first move)
    if order == '1':
        print_grid(my_grid)
        while not game_is_over(my_grid):
            # Player turn
            select_space(my_grid, int(input('Choose the number of space to mark: ')), "O")
            # Computer turn
            if not game_is_over(my_grid):
                select_space(my_grid, minimax(my_grid, True)[1], "X")
                print_grid(my_grid)

    # The game (computer makes first move)
    if order == '2':
        while not game_is_over(my_grid):
            # Computer turn
            select_space(my_grid, minimax(my_grid, True)[1], "X")
            print_grid(my_grid)
            # Player turn
            if not game_is_over(my_grid):
                select_space(my_grid, int(input('Choose the number of space to mark: ')), "O")

    result = evaluate_grid(my_grid)
    if result == 1:
        print('Computer wins')
    elif result == -1:
        print('You win')
    else:
        print('Draw')

    if input('Want to play again? (y or n): ') == 'y':
        main()


if __name__ == '__main__':
    print('Welcome to Tic-Tac-Toe!')
    main()
