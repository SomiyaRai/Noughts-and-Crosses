import random
import os.path
import json

random.seed()

def draw_board(board):
    """
    Draws the noughts and crosses board.

    Arguments:
    - board: A 3x3 list representing the current state of the board.

    Returns: None
    """
    print(" ----------- ")  # Adds horizontal line at the top
    for row in board:
        print("| " + " | ".join(row) + " |")
        print(" ----------- ")
    pass

def welcome(board):
    """
    Prints the welcome message and displays the initial board layout.

    Arguments:
    - board: A 3x3 list representing the current state of the board.

    Returns: None
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board Layout is shown below:")
    draw_board(board)
    pass

def initialise_board(board):
    """
    Sets all elements of the board to one space ' '.

    Arguments:
    - board: A 3x3 list representing the current state of the board.

    Returns:
    - board: The board with all elements set to ' '.
    """
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    """
    Asks the user for the cell to put the X in, and returns row and col.

    Arguments:
    - board: A 3x3 list representing the current state of the board.

    Returns:
    - row: The row number chosen by the player.
    - col: The column number chosen by the player.
    """
    while True:
        try:
            print("                    1 2 3")
            print("                    4 5 6")
            print("Choose your square: 7 8 9 :", end=" ")
            move = int(input())
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Square already taken. Choose another one.")
            else:
                print("Invalid move. Choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def choose_computer_move(board):
    """
    Lets the computer choose a cell to put a nought in, and returns row and col.

    Arguments:
    - board: A 3x3 list representing the current state of the board.

    Returns:
    - row: The row number chosen by the computer.
    - col: The column number chosen by the computer.
    """
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)
    return row, col

def check_for_win(board, mark):
    """
    Checks if either the player or the computer has won.

    Arguments:
    - board: A 3x3 list representing the current state of the board.
    - mark: The mark ('X' or 'O') to check for a win.

    Returns:
    - True if someone won, False otherwise.
    """
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
    """
    Checks if all cells are occupied.

    Arguments:
    - board: A 3x3 list representing the current state of the board.

    Returns:
    - True if all cells are occupied, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game(board):
    """
    Plays the game.

    Arguments:
    - board: A 3x3 list representing the current state of the board.

    Returns:
    - The score (1 if player wins, -1 if computer wins, 0 if draw).
    """
    initialise_board(board)
    player_score = 0
    
    while True:
        # Player's turn
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)

        # Checks for player win or draw
        if check_for_win(board, 'X'):
            print("You won!")
            player_score += 1
            return player_score
        elif check_for_draw(board):
            print("It's a draw!")
            return 0

        # Computer's turn
        print("Computer move:")
        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = 'O'
        draw_board(board)

        # Checks for computer win or draw
        if check_for_win(board, 'O'):
            print("You lose!")
            player_score -= 1
            return player_score
        elif check_for_draw(board):
            print("It's a draw!")
            return 0
        
def menu():
    """
    Gets user input of either '1', '2', '3' or 'q'.

    Returns:
    - choice: The user's choice ('1', '2', '3', or 'q').
    """
    print("Enter one of the following options:")
    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard.txt'")
    print("3 - Load and display the scores from the 'leaderboard.txt")
    print("q - End the program")
    return input("1, 2, 3 or q?  ")
    return choice

def load_scores():
    """
    Loads the leaderboard scores from the file 'leaderboard.txt'.

    Returns:
    - leaders: A dictionary with player names as keys and scores as values.
    """
    if os.path.isfile('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            try:
                leaders = json.load(file)
            except json.JSONDecodeError:
                print("Error decoding leaderboard file. Creating a new one.")
                leaders = {}
    else:
        print("Leaderboard file not found. Creating a new one.")
        leaders = {}
    
    return leaders

def save_score(score):
    """
    Saves the player's score to the file 'leaderboard.txt'.

    Arguments:
    - score: The current score to be saved.
    """
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)
    print(f"Score {score} saved for {name}.")
    return

def display_leaderboard(leaders):
    """
    Displays the leaderboard scores.

    Arguments:
    - leaders: A dictionary with player names as keys and scores as values.
    """
    print("Leaderboard:")
    for name, score in leaders.items():
        print(f"{name}: {score}")
        pass
