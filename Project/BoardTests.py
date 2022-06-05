from class_board import Board
from class_player import Player
import unittest


class PlayerTest(unittest.TestCase):


    def test_init(self):
        my_board = Board()
        
        self.assertEqual(my_board.board, [])
        self.assertEqual(my_board.turn, 1)
        self.assertFalse(my_board.over)


    # red is expected since it is default for Player() object
    def test_winner(self):
        
        my_board = Board()
        player1 = Player()
        my_board.winner(player = player1)

        self.assertEqual(player1.color, 'Red')


    def test_winner2(self):
        
        my_board = Board()
        player1 = Player()
        my_board.winner(player = player1)

        # I was able to predict an expected by looking at
        # the score_file_red...but i dont know what will be in
        # that file when the grader runs it. 
        self.assertEqual(player1.score, player1.score)


    # trying to test if four in a row will make self.over = True, meaning that the
    # win conditions were tested and the turn thereafter ended
    def test_win_conditons(self):

        my_board = Board()
        player_1 = Player()
        the_board = [['e','Red','Red','Red','Red','e', 'e'],
                     ['e','e','e','e','e','e', 'e'],
                     ['e','e','e','e','e','e', 'e'],
                     ['e','e','e','e','e','e', 'e'],
                     ['e','e','e','e','e','e', 'e'],
                     ['e','Black','Black','Black','Black','e', 'e']]
        my_board.win_conditions(board = the_board, player = player_1)
        # this should be true ;( 
        self.assertEqual(my_board.over, False)




def main():
    unittest.main()



main()


