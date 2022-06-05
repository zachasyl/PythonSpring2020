from class_player import Player
import unittest


class PlayerTest(unittest.TestCase):

    # the point of this test is to make sure a color can be set to
    # a player object as well as a truth value for turn and a score
    def test_init(self):
        player3 = Player(score = 0, turn = True, color = 'Red')
        self.assertEqual(player3.color, 'Red')
        self.assertEqual(player3.score, 0)
        self.assertTrue(player3.turn)

    def test_init2(self):
        player4 = Player(3, False, 'Black')
        
        self.assertEqual(player4.color, 'Black')
        self.assertEqual(player4.score, 3)
        self.assertFalse(player4.turn)


    # testing board[maximum][chosen_column] == 'e', color should change
    def test_turn_start(self):
        player5 = Player(score = 0, turn = True, color = 'Red')

        board = [['e', 'e', 'e'], ['e', 'e', 'e']]
        x_coordinates_rows = [['e', 'e', 'e'], ['e', 'e', 'e']]
        y_coordinates_rows =  [['e', 'e', 'e'], ['e', 'e', 'e']]
        maximum = 1
        # test will succeed in changing board[1][1] to player5.color, assert equal will pass
        player5.copied_turn_start(board, 1, 1,  x_coordinates_rows, y_coordinates_rows)
        self.assertEqual(board[1][1], player5.color)


    # board[maximum][chosen_column] != 'e': maximum will decrease to maximum -=1,
    # so game can check if next row is empty (in which case it will transform 'e'
    # to player color)
    def test_turn_start2(self):
        player5 = Player(score = 0, turn = True, color = 'Red')

        board = [['e', 'e', 'e'], ['e', 'j', 'e']]
        x_coordinates_rows = [['e', 'e', 'e'], ['e', 'e', 'e']]
        y_coordinates_rows =  [['e', 'e', 'e'], ['e', 'e', 'e']]
        maximum = 1

        # maximum of 2 should decrease to 1
        player5.copied_turn_start(board, 1, 2,  x_coordinates_rows, y_coordinates_rows)
        
        self.assertEqual(maximum, 1)


def main():
    unittest.main()

main()


