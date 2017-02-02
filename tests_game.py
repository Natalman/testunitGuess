import unittest

from unittest.mock import patch
import guess_game

class TestGame(unittest.TestCase):

    # #@patch ('guess_game.RamdomGuess', return_value = 4)
    # def test_game_lose(self, mock_game):
    #     self.assertFalse(guess_game.win())
    #
    # @patch ('guess_game.RamdomGuess', return_value = 2)
    # def test_game_win(self, mock_game):
    #     self.assertTrue(guess_game.win())
    #
    # @patch('guess_game.RamdomGuess', return_value = 2)
    # @patch ('builtins.print')
    # def test_main(self, mock_print, mock_game):
        #
        # guess_game.main()
        #
        # mock_game.assert_any_call('you win')


    @patch ('builtins.input', side_effect = [3, 6, 2, 4, 1])
    @patch ('builtins.print')
    def test_user_input(self, mock_print, mock_input):
        self.assertEqual(3, guess_game.UserGuess())
        self.assertEqual(6, guess_game.UserGuess())


    @patch('random.randint', return_value = 4)
    def test_guess(self, mock_random):
        self.assertTrue(4, guess_game.RamdomGuess())

if __name__ == '__main__':
    unittest.main()
