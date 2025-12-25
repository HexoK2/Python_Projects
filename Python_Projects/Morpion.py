# Constant for grid size (3x3)
SIZE = 3


def init_grid():
    """
    Initializes an empty grid of size SIZE x SIZE.

    Returns:
        list: 2D grid filled with empty strings
    """
    # Create an empty grid using list comprehension (more pythonic)
    grid = [["" for _ in range(SIZE)] for _ in range(SIZE)]
    return grid


def display_grid(grid):
    """
    Displays the game grid in the terminal in a formatted way.

    Args:
        grid (list): The 2D grid to display
    """
    print()  # Empty line for spacing
    for i in range(SIZE):
        # Display a row of the grid
        print("|", end=" ")
        for j in range(SIZE):
            # Display cell content (or a space if empty)
            content = grid[i][j] if grid[i][j] != "" else " "
            print(content, "|", end=" ")
        print()  # New line

        # Display separator line
        if i < SIZE - 1:
            print("-" * (SIZE * 4 - 1))
    print()


def check_victory(grid, symbol):
    """
    Checks if the player with the given symbol has won.
    Checks rows, columns and diagonals.

    Args:
        grid (list): The game grid
        symbol (str): The player's symbol ('X' or 'O')

    Returns:
        bool: True if the player has won, False otherwise
    """

    # Check rows
    for i in range(SIZE):
        if all(grid[i][j] == symbol for j in range(SIZE)):
            return True

    # Check columns
    for j in range(SIZE):
        if all(grid[i][j] == symbol for i in range(SIZE)):
            return True

    # Check main diagonal (top-left to bottom-right)
    if all(grid[i][i] == symbol for i in range(SIZE)):
        return True

    # Check reverse diagonal (top-right to bottom-left)
    if all(grid[i][SIZE - 1 - i] == symbol for i in range(SIZE)):
        return True

    return False


def is_grid_full(grid):
    """
    Checks if the grid is completely filled (potential draw).

    Args:
        grid (list): The game grid

    Returns:
        bool: True if all cells are filled, False otherwise
    """
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == "":
                return False
    return True


def update_grid(grid, i, j, symbol):
    """
    Places the player's symbol in the specified cell and displays the grid.

    Args:
        grid (list): The game grid
        i (int): Row index
        j (int): Column index
        symbol (str): The symbol to place ('X' or 'O')
    """
    grid[i][j] = symbol
    display_grid(grid)


def ask_for_move():
    """
    Asks the player to choose a cell and validates the input.

    Returns:
        tuple: (row, column) chosen by the player
    """
    while True:
        try:
            i = int(input(f"Row? (0 to {SIZE - 1}): "))
            j = int(input(f"Column? (0 to {SIZE - 1}): "))

            # Check that indices are within bounds
            if 0 <= i < SIZE and 0 <= j < SIZE:
                return i, j
            else:
                print(f"❌ Invalid input! Choose between 0 and {SIZE - 1}.")
        except ValueError:
            print("❌ Invalid input! Enter an integer.")


def play():
    """
    Main function that manages the game flow.
    """
    # Game initialization
    grid = init_grid()
    symbols = ["X", "O"]
    turn = 0
    game_over = False

    print("=" * 30)
    print("   WELCOME TO TIC-TAC-TOE!")
    print("=" * 30)
    display_grid(grid)

    # Main game loop
    while not game_over:
        # Determine current player's symbol
        current_symbol = symbols[turn % 2]
        print(f"\n{'=' * 30}")
        print(f"   Player {current_symbol}'s turn")
        print(f"{'=' * 30}")

        # Ask for and validate move
        valid_move = False
        while not valid_move:
            i, j = ask_for_move()

            # Check if cell is empty
            if grid[i][j] == "":
                valid_move = True
            else:
                print("⚠️  This cell is already taken! Choose another cell.")

        # Place symbol and display grid
        update_grid(grid, i, j, current_symbol)

        # Check if player has won
        if check_victory(grid, current_symbol):
            print(f"\n🎉 Congratulations! Player {current_symbol} has won! 🎉\n")
            game_over = True

        # Check if grid is full (draw)
        elif is_grid_full(grid):
            print("\n🤝 It's a draw! The grid is full. 🤝\n")
            game_over = True

        # Move to next turn
        turn += 1


# Program entry point
if __name__ == '__main__':
    play()