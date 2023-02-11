import unittest
from row import Row, RowNumber
from deck import Card, Suite
from adapter import string_lst_to_card_lst

class RowTest(unittest.TestCase):
    
    def test_ranking_comparison(self):
      straight_flush_row = Row([Card(Suite.DIAMONDS, 2), Card(Suite.DIAMONDS, 3), Card(Suite.DIAMONDS, 4), Card(Suite.DIAMONDS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)
      four_kind_row = Row([Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 7), Card(Suite.CLUBS, 7), Card(Suite.DIAMONDS, 8)], RowNumber.THREE)
      full_house_row = Row([Card(Suite.DIAMONDS, 9), Card(Suite.HEARTS, 9), Card(Suite.SPADES, 9), Card(Suite.CLUBS, 10), Card(Suite.DIAMONDS, 10)], RowNumber.THREE)
      flush_row = Row([Card(Suite.DIAMONDS, 2), Card(Suite.DIAMONDS, 4), Card(Suite.DIAMONDS,5), Card(Suite.DIAMONDS, 6), Card(Suite.DIAMONDS, 7)], RowNumber.THREE)
      straight_row = Row([Card(Suite.HEARTS, 8), Card(Suite.DIAMONDS, 9), Card(Suite.CLUBS, 10), Card(Suite.SPADES, 11), Card(Suite.DIAMONDS, 12)], RowNumber.THREE)
      three_kind_row = Row([Card(Suite.DIAMONDS, 9), Card(Suite.HEARTS, 9), Card(Suite.SPADES, 9), Card(Suite.CLUBS, 2), Card(Suite.DIAMONDS, 3)], RowNumber.THREE)
      two_pair_row = Row([Card(Suite.DIAMONDS, 4), Card(Suite.HEARTS, 4), Card(Suite.SPADES, 5), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)
      one_pair_row = Row([Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.CLUBS, 9), Card(Suite.DIAMONDS, 10)], RowNumber.THREE)
      high_card_row = Row([Card(Suite.DIAMONDS, 13), Card(Suite.HEARTS, 2), Card(Suite.SPADES, 3), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)

      self.assertGreater(straight_flush_row, four_kind_row)
      self.assertGreater(four_kind_row, full_house_row)
      self.assertGreater(full_house_row, flush_row)
      self.assertGreater(flush_row, straight_row)
      self.assertGreater(straight_row, three_kind_row)
      self.assertGreater(three_kind_row, two_pair_row)
      self.assertGreater(two_pair_row, one_pair_row)
      self.assertGreater(one_pair_row, high_card_row)

    def test_straight_flush(self):
      diamonds_row = Row([Card(Suite.DIAMONDS, 2), Card(Suite.DIAMONDS, 3), Card(Suite.DIAMONDS, 4), Card(Suite.DIAMONDS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)
      hearts_row = Row([Card(Suite.HEARTS, 2), Card(Suite.HEARTS, 3), Card(Suite.HEARTS, 4), Card(Suite.HEARTS, 5), Card(Suite.HEARTS, 6)], RowNumber.THREE)
      self.assertEqual(diamonds_row.settle(hearts_row), 0)

      hearts_2_row = Row([Card(Suite.HEARTS, 3), Card(Suite.HEARTS, 4), Card(Suite.HEARTS, 5), Card(Suite.HEARTS, 6), Card(Suite.HEARTS, 7)], RowNumber.THREE)
      self.assertGreater(hearts_2_row, hearts_row)

      low_ace_row = Row([Card(Suite.HEARTS, 14), Card(Suite.HEARTS, 2), Card(Suite.HEARTS, 3), Card(Suite.HEARTS, 4), Card(Suite.HEARTS, 5)], RowNumber.THREE)
      self.assertGreater(hearts_row, low_ace_row)

    def test_four_kind(self): 
      row = Row([Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 7), Card(Suite.CLUBS, 7), Card(Suite.DIAMONDS, 10)], RowNumber.THREE)
      row_2 = Row([Card(Suite.DIAMONDS, 8), Card(Suite.HEARTS, 8), Card(Suite.SPADES, 8), Card(Suite.CLUBS, 8), Card(Suite.DIAMONDS, 9)], RowNumber.THREE)
      
      self.assertEqual(row, row)
      self.assertGreater(row_2, row)

    def test_full_house(self):
      row = Row([Card(Suite.DIAMONDS, 2), Card(Suite.HEARTS, 2), Card(Suite.SPADES, 2), Card(Suite.CLUBS, 10), Card(Suite.DIAMONDS, 10)], RowNumber.THREE)
      row_2 = Row([Card(Suite.DIAMONDS, 3), Card(Suite.HEARTS, 3), Card(Suite.SPADES, 3), Card(Suite.CLUBS, 4), Card(Suite.DIAMONDS, 4)], RowNumber.THREE)
      
      self.assertEqual(row, row)
      self.assertGreater(row_2, row)
    
    def test_flush(self):
      row = Row([Card(Suite.HEARTS, 3), Card(Suite.HEARTS, 4), Card(Suite.HEARTS,5), Card(Suite.HEARTS, 6), Card(Suite.HEARTS, 8)], RowNumber.THREE)
      row_2 = Row([Card(Suite.DIAMONDS, 2), Card(Suite.DIAMONDS, 4), Card(Suite.DIAMONDS,5), Card(Suite.DIAMONDS, 6), Card(Suite.DIAMONDS, 10)], RowNumber.THREE)
      
      self.assertEqual(row, row)
      self.assertGreater(row_2, row)
    
    def test_straight(self):
      low_ace_row = Row([Card(Suite.DIAMONDS, 14), Card(Suite.HEARTS, 2), Card(Suite.HEARTS, 3), Card(Suite.HEARTS, 4), Card(Suite.HEARTS, 5)], RowNumber.THREE)
      two_row = Row([Card(Suite.SPADES, 2), Card(Suite.DIAMONDS, 3), Card(Suite.DIAMONDS, 4), Card(Suite.DIAMONDS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)
      high_ace_row = Row([Card(Suite.DIAMONDS, 10), Card(Suite.HEARTS, 11), Card(Suite.HEARTS, 12), Card(Suite.HEARTS, 13), Card(Suite.HEARTS, 1)], RowNumber.THREE)
      
      self.assertEqual(two_row, two_row)
      self.assertGreater(two_row, low_ace_row)
      self.assertGreater(high_ace_row, two_row)
    
    def test_three_kind(self):
      row = Row([Card(Suite.DIAMONDS, 9), Card(Suite.HEARTS, 9), Card(Suite.SPADES, 9), Card(Suite.CLUBS, 2), Card(Suite.DIAMONDS, 3)], RowNumber.THREE)
      row_2 = Row([Card(Suite.DIAMONDS, 10), Card(Suite.HEARTS, 10), Card(Suite.SPADES, 10), Card(Suite.CLUBS, 2), Card(Suite.SPADES, 3)], RowNumber.THREE)
      
      self.assertEqual(row, row)
      self.assertGreater(row_2, row)
    
    def test_two_pair(self):
      row = Row([Card(Suite.DIAMONDS, 4), Card(Suite.HEARTS, 4), Card(Suite.SPADES, 5), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)

      row_2 = Row([Card(Suite.SPADES, 4), Card(Suite.CLUBS, 4), Card(Suite.HEARTS, 5), Card(Suite.DIAMONDS, 5), Card(Suite.DIAMONDS, 7)], RowNumber.THREE)
      row_3 = Row([Card(Suite.SPADES, 3), Card(Suite.CLUBS, 3), Card(Suite.HEARTS, 6), Card(Suite.DIAMONDS, 6), Card(Suite.DIAMONDS, 7)], RowNumber.THREE)

      self.assertEqual(row, row)
      self.assertGreater(row_2, row)
      self.assertGreater(row_3, row_2)

    def test_one_pair(self):
      row = Row([Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.CLUBS, 9), Card(Suite.DIAMONDS, 10)], RowNumber.THREE)
      row_2 = Row([Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.CLUBS, 9), Card(Suite.DIAMONDS, 12)], RowNumber.THREE)
      row_3 = Row([Card(Suite.DIAMONDS, 10), Card(Suite.HEARTS, 10), Card(Suite.SPADES, 4), Card(Suite.CLUBS, 3), Card(Suite.DIAMONDS, 2)], RowNumber.THREE)

      self.assertEqual(row, row)
      self.assertGreater(row_2, row)
      self.assertGreater(row_3, row_2)

    def test_high_card(self):
      row = Row([Card(Suite.DIAMONDS, 13), Card(Suite.HEARTS, 2), Card(Suite.SPADES, 3), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)
      row_2 = Row([Card(Suite.DIAMONDS, 14), Card(Suite.HEARTS, 2), Card(Suite.SPADES, 3), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)

      self.assertEqual(row, row)
      self.assertGreater(row_2, row)
    
    def test_points(self):
      straight_flush_row = Row([Card(Suite.DIAMONDS, 2), Card(Suite.DIAMONDS, 3), Card(Suite.DIAMONDS, 4), Card(Suite.DIAMONDS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)
      straight_flush_high_ace_row = Row([Card(Suite.HEARTS, 10), Card(Suite.HEARTS, 11), Card(Suite.HEARTS, 12), Card(Suite.HEARTS, 13), Card(Suite.HEARTS, 1)], RowNumber.THREE)
      self.assertEqual(straight_flush_row.points, 6)
      self.assertEqual(straight_flush_high_ace_row.points, 7)

      four_kind_ace = Row([Card(Suite.DIAMONDS, 1), Card(Suite.HEARTS, 1), Card(Suite.SPADES, 1), Card(Suite.CLUBS, 1), Card(Suite.DIAMONDS, 8)], RowNumber.THREE)
      self.assertEqual(four_kind_ace.points, 7)

      three_kind_row_1 = Row([Card(Suite.DIAMONDS, 1), Card(Suite.HEARTS, 1), Card(Suite.SPADES, 1)], RowNumber.ONE)
      three_kind_row_2 = Row([Card(Suite.DIAMONDS, 1), Card(Suite.HEARTS, 1), Card(Suite.SPADES, 1), Card(Suite.CLUBS, 2), Card(Suite.DIAMONDS, 3)], RowNumber.TWO)
      three_kind_row_3 = Row([Card(Suite.DIAMONDS, 1), Card(Suite.HEARTS, 1), Card(Suite.SPADES, 1), Card(Suite.CLUBS, 2), Card(Suite.DIAMONDS, 3)], RowNumber.THREE)
      self.assertEqual(three_kind_row_1.points, 6)
      self.assertEqual(three_kind_row_2.points, 2)
      self.assertEqual(three_kind_row_3.points, 1)

      one_pair_ace_row_1 = Row([Card(Suite.DIAMONDS, 1), Card(Suite.HEARTS, 1), Card(Suite.SPADES, 8)], RowNumber.ONE)
      one_pair_ace_row_2 = Row([Card(Suite.DIAMONDS, 1), Card(Suite.HEARTS, 1), Card(Suite.SPADES, 8), Card(Suite.CLUBS, 9), Card(Suite.DIAMONDS, 10)], RowNumber.TWO)
      self.assertEqual(one_pair_ace_row_1.points, 2)
      self.assertEqual(one_pair_ace_row_2.points, 1)
  
    def test_row_one(self):
      three_kind_row = Row([Card(Suite.DIAMONDS, 9), Card(Suite.HEARTS, 9), Card(Suite.SPADES, 9)], RowNumber.ONE)
      one_pair_row = Row([Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8)], RowNumber.ONE)
      high_card_row = Row([Card(Suite.DIAMONDS, 13), Card(Suite.HEARTS, 2), Card(Suite.SPADES, 3)], RowNumber.ONE)
      self.assertGreater(three_kind_row, one_pair_row)
      self.assertGreater(one_pair_row, high_card_row)
    
    def test_inter_row(self):
      three_kind_row_1 = Row([Card(Suite.DIAMONDS, 9), Card(Suite.HEARTS, 9), Card(Suite.SPADES, 9)], RowNumber.ONE)
      one_pair_row_1 = Row([Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8)], RowNumber.ONE)

      two_pair_row_3 = Row([Card(Suite.DIAMONDS, 4), Card(Suite.HEARTS, 4), Card(Suite.SPADES, 5), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)
      one_pair_row_3 = Row([Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.CLUBS, 9), Card(Suite.DIAMONDS, 10)], RowNumber.THREE)
      high_card_row_3 = Row([Card(Suite.DIAMONDS, 13), Card(Suite.HEARTS, 2), Card(Suite.SPADES, 3), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)
      
      self.assertGreater(three_kind_row_1, two_pair_row_3)
      self.assertGreater(three_kind_row_1, one_pair_row_3)
      self.assertGreater(three_kind_row_1, high_card_row_3)
      self.assertGreater(one_pair_row_1, high_card_row_3)
    
    def test_settle(self):
      one_pair_row = Row([Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.CLUBS, 9), Card(Suite.DIAMONDS, 10)], RowNumber.THREE)
      high_card_row = Row([Card(Suite.DIAMONDS, 13), Card(Suite.HEARTS, 2), Card(Suite.SPADES, 3), Card(Suite.CLUBS, 5), Card(Suite.DIAMONDS, 6)], RowNumber.THREE)
      self.assertEqual(one_pair_row.settle(one_pair_row), 0)
      self.assertEqual(one_pair_row.settle(high_card_row), 1)
      self.assertEqual(high_card_row.settle(one_pair_row), -1)
    
    def test_settle_2(self):
      a_row_one = Row(string_lst_to_card_lst(["S3", "H3", "D3"]), RowNumber.ONE)
      a_row_two = Row(string_lst_to_card_lst(["S2", "H2", "D2", "S5", "H5"]), RowNumber.TWO)
      a_row_three = Row(string_lst_to_card_lst(["S4", "H4", "D4", "S6", "H6"]), RowNumber.THREE)
      
      b_row_one = Row(string_lst_to_card_lst(["D4", "D3", "D2"]), RowNumber.ONE)
      b_row_two = Row(string_lst_to_card_lst(["H6", "H5", "H4", "H3", "H2"]), RowNumber.TWO)
      b_row_three = Row(string_lst_to_card_lst(["S6", "S5", "S4", "S3", "S2"]), RowNumber.THREE)
      self.assertEqual(a_row_one.settle(b_row_one), 1)
      self.assertEqual(a_row_two.settle(b_row_two), -6)
      self.assertEqual(a_row_three.settle(b_row_three), -6)

if __name__ == '__main__':
    unittest.main()