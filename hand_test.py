import unittest
from deck import Card, Suite
from hand import Hand, HandStrategyEnum, HandStrategyObject
from row import RowNumber, RowStrategy

class HandTest(unittest.TestCase):
  def test_exception(self):
    three_kind_row_1 = [Card(Suite.DIAMONDS, 9), Card(Suite.HEARTS, 9), Card(Suite.SPADES, 9)]
    two_pair_row_3 = [Card(Suite.DIAMONDS, 4), Card(Suite.HEARTS, 4), Card(Suite.SPADES, 5), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)]
    one_pair_row_3 = [Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.CLUBS, 9), Card(Suite.DIAMONDS, 10)]
    self.assertRaises(Exception, Hand, three_kind_row_1, two_pair_row_3, one_pair_row_3)

  def test_hand_strategy_enum(self):
    max_one_two = HandStrategyObject(HandStrategyEnum.MAX_ONE_TWO)
    self.assertEqual(max_one_two.row_orders, [RowNumber.ONE, RowNumber.TWO, RowNumber.THREE])
    self.assertEqual(max_one_two.row_strategies, [RowStrategy.MAX_RANK, RowStrategy.MAX, RowStrategy.MAX])

    rank_three_two = HandStrategyObject(HandStrategyEnum.RANK_THREE_TWO)
    self.assertEqual(rank_three_two.row_orders, [RowNumber.THREE, RowNumber.TWO, RowNumber.ONE])
    self.assertEqual(rank_three_two.row_strategies, [RowStrategy.MAX_RANK, RowStrategy.MAX_RANK, RowStrategy.MAX])

if __name__ == '__main__':
    unittest.main()