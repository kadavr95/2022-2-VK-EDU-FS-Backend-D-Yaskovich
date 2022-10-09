"""Tic-Tac-Toe"""


class TicTacToeGame:
    """Tic-Tac-Toe class"""

    def __init__(self):
        """Class initialization"""
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.turn_number = 0

    def show_board(self):
        """Game board display"""
        print("    1   2   3\n",
              "  ┌───┬───┬───┐\n",
              "A │ "
              + self.board[0][0] + " │ "
              + self.board[0][1] + " │ "
              + self.board[0][2] + " │\n",
              "  ├───┼───┼───┤\n",
              "B │ "
              + self.board[1][0] + " │ "
              + self.board[1][1] + " │ "
              + self.board[1][2] + " │\n",
              "  ├───┼───┼───┤\n",
              "C │ "
              + self.board[2][0] + " │ "
              + self.board[2][1] + " │ "
              + self.board[2][2] + " │\n",
              "  └───┴───┴───┘\n", sep='')

    def make_move(self):
        """Handler of the players moves"""
        while True:
            next_move = list(input())
            try:
                row, column = self.validate_input(next_move)
                if self.turn_number % 2 == 0:
                    self.board[row][column] = 'x'
                else:
                    self.board[row][column] = 'o'

                self.show_board()
                self.turn_number += 1
                if self.check_winner(row, column):
                    break
            except ValueError as err:
                print(str(err))

    def validate_input(self, next_move):
        """Validation of the input correctness"""
        if len(next_move) != 2:
            raise ValueError('Error: Position should consist of the two symbols in format A1')
        if not next_move[0].isalpha():
            raise ValueError('Error: First symbol of the position should be a letter')
        if not next_move[1].isdecimal():
            raise ValueError('Error: Second symbol of the position should be a number')

        row = ord(next_move[0].upper()) - ord('A')
        column = int(next_move[1]) - 1

        if not (0 <= row <= 2 and 0 <= column <= 2):
            raise ValueError('Error: Cell position is out of range!')
        if self.board[row][column] != ' ':
            raise ValueError('Error: This position is already filled!')
        return row, column

    def start_game(self):
        """Game initialization"""
        print('Controls: cell position in the format RowColumn, e.g. A1')
        self.show_board()
        self.make_move()

    def check_winner(self, row, column):
        """Handler of game ending"""
        if self.turn_number % 2 != 0:
            fig = 'x'
        else:
            fig = 'o'

        if any([sum(map(lambda n: n == fig, map(lambda m: self.board[m][column], range(3)))) == 3,
                sum(map(lambda n: n == fig, map(lambda m: self.board[row][m], range(3)))) == 3,
                row == column and
                sum(map(lambda n: n == fig, map(lambda m: self.board[m][m], range(3)))) == 3,
                row + column == 2 and
                sum(map(lambda n: n == fig, map(lambda m: self.board[m][2 - m], range(3)))) == 3]):
            print(f'{fig} won!')
            return True

        if self.turn_number == 9:
            print("It's a draw!")
            return True
        return False


if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
