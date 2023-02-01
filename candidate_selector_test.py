import unittest
from candidate_selector import CandidateSelector
from deck import Card, Suite

class HandTest(unittest.TestCase):
  def test(self):
    cards = [Card(Suite.DIAMONDS, 11), Card(Suite.HEARTS, 11), Card(Suite.SPADES, 11),
      Card(Suite.DIAMONDS, 2), Card(Suite.SPADES, 2),
      Card(Suite.HEARTS, 5), Card(Suite.SPADES, 5),
      Card(Suite.CLUBS, 8), Card(Suite.DIAMONDS, 8),
      Card(Suite.HEARTS, 3), Card(Suite.CLUBS, 4), Card(Suite.HEARTS, 9), Card(Suite.CLUBS, 10)]
    cs = CandidateSelector(cards)
    print(cs)

if __name__ == '__main__':
    unittest.main()