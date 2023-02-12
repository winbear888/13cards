import unittest
from deck import Card, Suite
from adapter import string_lst_to_card_lst, card_lst_to_stringify_lst, hand_info_to_dict
from hand import Hand, HandInfo

class AdapterTest(unittest.TestCase):
  def test_string_lst_to_card_lst(self):
    stringify_lst = ["D14", "H14", "S5", "C5", "D6"]
    card_lst = [Card(Suite.DIAMONDS, 14), Card(Suite.HEARTS, 14), Card(Suite.SPADES, 5), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)]
    self.assertEqual(string_lst_to_card_lst(stringify_lst), card_lst)
  
  def test_card_lst_to_stringify_lst(self):
    stringify_lst = "D14 H14 S5 C5 D6"
    # The ace should be converted from 1 to 14
    card_lst = [Card(Suite.DIAMONDS, 1), Card(Suite.HEARTS, 14), Card(Suite.SPADES, 5), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)]
    self.assertEqual(card_lst_to_stringify_lst(card_lst), stringify_lst)
  
  def test_hand_info_to_dict(self):
    hand1 = Hand([Card(Suite.CLUBS, 10), Card(Suite.HEARTS, 9), Card(Suite.CLUBS, 4)],
    [Card(Suite.CLUBS, 8), Card(Suite.DIAMONDS, 8), Card(Suite.HEARTS, 5), Card(Suite.SPADES, 5), Card(Suite.HEARTS, 3)],
    [Card(Suite.DIAMONDS, 11), Card(Suite.HEARTS, 11), Card(Suite.SPADES, 11), Card(Suite.DIAMONDS, 2), Card(Suite.SPADES, 2)])
    hand_info_1 = HandInfo(hand1)
    dic = hand_info_to_dict(hand_info_1)
    self.assertEqual(dic['row_2'], ['D8', 'C8', 'S5', 'H5', 'H3'])
    self.assertEqual(dic['row_2_ranking'], "TWO_PAIR")
    self.assertEqual(dic['row_2_points'], 1)

if __name__ == '__main__':
    unittest.main()