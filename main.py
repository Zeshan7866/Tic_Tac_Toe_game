import random
import os

class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def print_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 9)

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move. That position is already taken.")

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def is_full(self):
        return " " not in self.board

    def make_computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] == " "]

        # Check if computer can win on the next move
        for move in available_moves:
            self.board[move] = "0"
            if self.check_winner() == "O":
                self.board[move] = " "
                self.make_move(move)
                return
            self.board[move] = " "  # Undo the move

        # Check if player X can win on the next move and block it
        for move in available_moves:
            self.board[move] = "X"
            if self.check_winner() == "X":
                self.board[move] = " "
                self.make_move(move)
                return
            self.board[move] = " "  # Undo the move

        # If no winning move found, make a random move
        if available_moves:
            move = random.choice(available_moves)
            self.make_move(move)
            return

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            self.print_board()
            print(f"Player {self.current_player}'s turn.")
            if self.current_player == "X":
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if move < 0 or move > 8:
                        raise ValueError
                    self.make_move(move)
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")
                    continue
            else:
                self.make_computer_move()

            winner = self.check_winner()
            if winner:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
                self.print_board()
                if winner == "X":
                    print("Player X wins!")
                else:
                    print("Computer wins!")
                break
            elif self.is_full():
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
                self.print_board()
                print("It's a draw!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
