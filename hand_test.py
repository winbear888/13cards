import unittest
from deck import Card, Suite
from hand import Hand, HandStrategyEnum, HandStrategyObject
from row import RowNumber, RowStrategy
from adapter import string_lst_to_card_lst

class HandTest(unittest.TestCase):
  def test_exception(self):
    three_kind_row_1 = [Card(Suite.DIAMONDS, 9), Card(Suite.HEARTS, 9), Card(Suite.SPADES, 9)]
    two_pair_row_3 = [Card(Suite.DIAMONDS, 4), Card(Suite.HEARTS, 4), Card(Suite.SPADES, 5), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)]
    one_pair_row_3 = [Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.CLUBS, 9), Card(Suite.DIAMONDS, 10)]
    self.assertRaises(Exception, Hand, three_kind_row_1, two_pair_row_3, one_pair_row_3)

  def test_hand_strategy_enum(self):
    max_one_two = HandStrategyObject(HandStrategyEnum.MAX_MAX_ONE_TWO)
    self.assertEqual(max_one_two.row_orders, [RowNumber.ONE, RowNumber.TWO, RowNumber.THREE])
    self.assertEqual(max_one_two.row_strategies, [RowStrategy.MAX_RANK, RowStrategy.MAX, RowStrategy.MAX])

    rank_three_two = HandStrategyObject(HandStrategyEnum.RANK_MAX_THREE_TWO)
    self.assertEqual(rank_three_two.row_orders, [RowNumber.THREE, RowNumber.TWO, RowNumber.ONE])
    self.assertEqual(rank_three_two.row_strategies, [RowStrategy.MAX_RANK, RowStrategy.MAX_RANK, RowStrategy.MAX])

  def test_settle(self):
    hand1 = Hand([Card(Suite.CLUBS, 10), Card(Suite.HEARTS, 9), Card(Suite.CLUBS, 4)],
    [Card(Suite.CLUBS, 8), Card(Suite.DIAMONDS, 8), Card(Suite.HEARTS, 5), Card(Suite.SPADES, 5), Card(Suite.HEARTS, 3)],
    [Card(Suite.DIAMONDS, 11), Card(Suite.HEARTS, 11), Card(Suite.SPADES, 11), Card(Suite.DIAMONDS, 2), Card(Suite.SPADES, 2)])
    hand2 = Hand([Card(Suite.HEARTS, 4), Card(Suite.SPADES, 4), Card(Suite.SPADES, 14)],
    [Card(Suite.SPADES, 12), Card(Suite.DIAMONDS, 12), Card(Suite.HEARTS, 13), Card(Suite.DIAMONDS, 10), Card(Suite.DIAMONDS, 6)],
    [Card(Suite.DIAMONDS, 5), Card(Suite.CLUBS, 6), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.DIAMONDS, 9)])
    hand3 = Hand([Card(Suite.SPADES, 9), Card(Suite.CLUBS, 9), Card(Suite.SPADES, 7)],
    [Card(Suite.HEARTS, 2), Card(Suite.CLUBS, 3), Card(Suite.DIAMONDS, 4), Card(Suite.CLUBS, 5), Card(Suite.SPADES, 6)],
    [Card(Suite.CLUBS, 2), Card(Suite.CLUBS, 7), Card(Suite.CLUBS, 11), Card(Suite.CLUBS, 12), Card(Suite.CLUBS, 13)])

    self.assertEqual(hand1.settle(hand2), 1)
    self.assertEqual(hand2.settle(hand1), -1)
    
    self.assertEqual(hand2.settle(hand3), -6)
    self.assertEqual(hand3.settle(hand2), 6)
  
  def test_settle_2(self):
    hand1 = Hand(string_lst_to_card_lst(["S3", "H3", "D3"]), string_lst_to_card_lst(["S2", "H2", "D2", "S5", "H5"]), string_lst_to_card_lst(["S4", "H4", "D4", "S6", "H6"]))

    hand2 = Hand(string_lst_to_card_lst(["D4", "D3", "D2"]), string_lst_to_card_lst(["H6", "H5", "H4", "H3", "H2"]), string_lst_to_card_lst(["S6", "S5", "S4", "S3", "S2"]))
    self.assertEqual(hand1.settle(hand2), -11)

if __name__ == '__main__':
    unittest.main()