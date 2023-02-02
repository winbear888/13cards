import unittest

from deck import Card, Suite
from hand import Hand, HandInfo
import game
class GameTest(unittest.TestCase):
  def test_round(self):
    hand1 = Hand([Card(Suite.CLUBS, 10), Card(Suite.HEARTS, 9), Card(Suite.CLUBS, 4)],
    [Card(Suite.CLUBS, 8), Card(Suite.DIAMONDS, 8), Card(Suite.HEARTS, 5), Card(Suite.SPADES, 5), Card(Suite.HEARTS, 3)],
    [Card(Suite.DIAMONDS, 11), Card(Suite.HEARTS, 11), Card(Suite.SPADES, 11), Card(Suite.DIAMONDS, 2), Card(Suite.SPADES, 2)])
    hand_info_1 = HandInfo(hand1)

    hand2 = Hand([Card(Suite.HEARTS, 4), Card(Suite.SPADES, 4), Card(Suite.SPADES, 14)],
    [Card(Suite.SPADES, 12), Card(Suite.DIAMONDS, 12), Card(Suite.HEARTS, 13), Card(Suite.DIAMONDS, 10), Card(Suite.DIAMONDS, 6)],
    [Card(Suite.DIAMONDS, 5), Card(Suite.CLUBS, 6), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.DIAMONDS, 9)])
    hand_info_2 = HandInfo(hand2)

    hand3 = Hand([Card(Suite.SPADES, 9), Card(Suite.CLUBS, 9), Card(Suite.SPADES, 7)],
    [Card(Suite.HEARTS, 2), Card(Suite.CLUBS, 3), Card(Suite.DIAMONDS, 4), Card(Suite.CLUBS, 5), Card(Suite.SPADES, 6)],
    [Card(Suite.CLUBS, 2), Card(Suite.CLUBS, 7), Card(Suite.CLUBS, 11), Card(Suite.CLUBS, 12), Card(Suite.CLUBS, 13)])
    hand_info_3 = HandInfo(hand3)

    hand4 = Hand([Card(Suite.SPADES, 3), Card(Suite.DIAMONDS, 3), Card(Suite.HEARTS, 12)], 
    [Card(Suite.SPADES, 13), Card(Suite.DIAMONDS, 13), Card(Suite.HEARTS, 8), Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 6)],[Card(Suite.HEARTS, 14), Card(Suite.DIAMONDS, 14), Card(Suite.CLUBS, 14), Card(Suite.HEARTS, 10), Card(Suite.DIAMONDS, 10)])
    hand_info_4 = HandInfo(hand4)
    game.round([hand_info_1, hand_info_2, hand_info_3, hand_info_4])
    self.assertEqual(hand_info_1.points_history, [-1])
    self.assertEqual(hand_info_2.points_history, [-8])
    self.assertEqual(hand_info_3.points_history, [8])
    self.assertEqual(hand_info_4.points_history, [1])
  
  def test_beat_all_round(self):
    hand1 = Hand([Card(Suite.CLUBS, 10), Card(Suite.HEARTS, 9), Card(Suite.CLUBS, 4)],
    [Card(Suite.CLUBS, 8), Card(Suite.DIAMONDS, 8), Card(Suite.HEARTS, 5), Card(Suite.SPADES, 5), Card(Suite.HEARTS, 3)],
    [Card(Suite.DIAMONDS, 11), Card(Suite.HEARTS, 11), Card(Suite.SPADES, 11), Card(Suite.DIAMONDS, 2), Card(Suite.SPADES, 2)])
    hand_info_1 = HandInfo(hand1)

    hand2 = Hand([Card(Suite.HEARTS, 4), Card(Suite.SPADES, 4), Card(Suite.SPADES, 14)],
    [Card(Suite.SPADES, 12), Card(Suite.DIAMONDS, 12), Card(Suite.HEARTS, 13), Card(Suite.DIAMONDS, 10), Card(Suite.DIAMONDS, 6)],
    [Card(Suite.DIAMONDS, 5), Card(Suite.CLUBS, 6), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.DIAMONDS, 9)])
    hand_info_2 = HandInfo(hand2)

    hand3 = Hand([Card(Suite.SPADES, 7), Card(Suite.DIAMONDS, 7), Card(Suite.SPADES, 6)],
    [Card(Suite.SPADES, 9), Card(Suite.CLUBS, 9), Card(Suite.HEARTS, 2), Card(Suite.DIAMONDS, 4), Card(Suite.CLUBS, 5)],
    [Card(Suite.CLUBS, 2),  Card(Suite.CLUBS, 7), Card(Suite.CLUBS, 11), Card(Suite.CLUBS, 12), Card(Suite.CLUBS, 13)])
    hand_info_3 = HandInfo(hand3)

    hand4 = Hand([Card(Suite.SPADES, 13), Card(Suite.DIAMONDS, 13), Card(Suite.HEARTS, 12)], 
    [Card(Suite.SPADES, 3), Card(Suite.DIAMONDS, 3), Card(Suite.CLUBS, 3), Card(Suite.HEARTS, 8), Card(Suite.HEARTS, 6)],
    [Card(Suite.HEARTS, 14), Card(Suite.DIAMONDS, 14), Card(Suite.CLUBS, 14), Card(Suite.HEARTS, 10), Card(Suite.DIAMONDS, 10)])
    hand_info_4 = HandInfo(hand4)
    game.round([hand_info_1, hand_info_2, hand_info_3, hand_info_4])
    self.assertEqual(hand_info_1.points_history, [-10])
    self.assertEqual(hand_info_2.points_history, [-14])
    self.assertEqual(hand_info_3.points_history, [-12])
    self.assertEqual(hand_info_4.points_history, [36])


if __name__ == '__main__':
    unittest.main()