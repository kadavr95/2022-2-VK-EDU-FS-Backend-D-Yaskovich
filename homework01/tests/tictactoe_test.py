"""Tic-Tac-Toe unit tests"""
import unittest

from unittest.mock import patch
from homework01.tictactoe import TicTacToeGame


class TicTacToeTestCase(unittest.TestCase):
    """Tic-Tac-Toe test suite"""

    @patch('builtins.print')
    def test_empty_board_output(self, mock_print):
        """Test output of empty board"""
        game = TicTacToeGame()
        game.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        game.show_board()
        mock_print.assert_called_with(
            "    1   2   3\n",
            "  ┌───┬───┬───┐\n",
            "A │   │   │   │\n",
            "  ├───┼───┼───┤\n",
            "B │   │   │   │\n",
            "  ├───┼───┼───┤\n",
            "C │   │   │   │\n",
            "  └───┴───┴───┘\n", sep='')

    @patch('builtins.print')
    def test_filled_board_output(self, mock_print):
        """Test output of the filled board"""
        game = TicTacToeGame()
        game.board = [
            ['x', 'o', 'x'],
            ['x', 'x', 'o'],
            ['o', 'x', 'o']
        ]
        game.show_board()
        mock_print.assert_called_with(
            "    1   2   3\n",
            "  ┌───┬───┬───┐\n",
            "A │ x │ o │ x │\n",
            "  ├───┼───┼───┤\n",
            "B │ x │ x │ o │\n",
            "  ├───┼───┼───┤\n",
            "C │ o │ x │ o │\n",
            "  └───┴───┴───┘\n", sep='')

    def test_correct_input(self):
        """Test of correct input cases"""
        game = TicTacToeGame()
        game.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        param_list = [(["A", "1"], (0, 0, None)),
                      (["c", "3"], (2, 2, None))]
        for input_data, expected_output in param_list:
            with self.subTest():
                self.assertEqual(game.validate_input(input_data), expected_output)

    def test_incorrect_input(self):
        """Test incorrect input cases"""
        game = TicTacToeGame()
        game.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', 'x', ' ']
        ]
        param_list = [([],
                       (-1, -1, 'Error: Position should consist of the two symbols in format A1')),
                      (["c"],
                       (-1, -1, 'Error: Position should consist of the two symbols in format A1')),
                      (["c", "5", "a"],
                       (-1, -1, 'Error: Position should consist of the two symbols in format A1')),
                      (["я", "1"], (-1, -1, 'Error: Cell position is out of range!')),
                      (["c", "4"], (-1, -1, 'Error: Cell position is out of range!')),
                      (["1", "2"],
                       (-1, -1, 'Error: First symbol of the position should be a letter')),
                      (["c", "b"],
                       (-1, -1, 'Error: Second symbol of the position should be a number')),
                      (["c", "2"], (-1, -1, 'Error: This position is already filled!'))]
        for input_data, expected_output in param_list:
            with self.subTest():
                self.assertEqual(game.validate_input(input_data), expected_output)

    @patch('builtins.print')
    def test_draw_condition(self, mock_print):
        """Test draw algorithm"""
        game = TicTacToeGame()
        game.board = [
            ['x', 'o', 'x'],
            ['x', 'x', 'o'],
            ['o', 'x', 'o']
        ]
        game.turn_number = 9
        self.assertEqual(game.check_winner(1, 1), True)
        game.check_winner(1, 1)
        mock_print.assert_called_with("It's a draw!")

    @patch('builtins.print')
    def test_win_positions(self, mock_print):
        """Test win detection algorithm"""
        game = TicTacToeGame()
        param_list = [([['x', 'o', ' '],
                        ['x', 'x', 'o'],
                        [' ', 'x', 'o']
                        ], 7, False),
                      ([['o', 'o', ' '],
                        ['x', 'x', 'x'],
                        [' ', 'x', 'o']
                        ], 7, True),
                      ([['x', 'x', ' '],
                        ['o', 'x', 'o'],
                        [' ', 'x', 'o']
                        ], 7, True),
                      ([['x', 'o', ' '],
                        ['o', 'x', 'o'],
                        [' ', 'x', 'x']
                        ], 7, True),
                      ([[' ', 'o', 'x'],
                        [' ', 'x', 'o'],
                        ['x', 'x', 'o']
                        ], 7, True),
                      ([['x', ' ', 'o'],
                        ['x', 'o', 'x'],
                        ['o', 'x', ' ']
                        ], 8, True)
                      ]
        for board, turn_number, expected_output in param_list:
            with self.subTest():
                game.board = board
                game.turn_number = turn_number
                self.assertEqual(game.check_winner(1, 1), expected_output)
                if expected_output:
                    game.check_winner(1, 1)
                    if turn_number == 7:
                        mock_print.assert_called_with("x won!")
                    if turn_number == 8:
                        mock_print.assert_called_with("o won!")


if __name__ == '__main__':
    unittest.main()
