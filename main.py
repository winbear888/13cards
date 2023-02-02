import candidate_ranker
from deck import Card, Suite
import time

hand1 = [Card(Suite.CLUBS, 10), Card(Suite.HEARTS, 9), Card(Suite.CLUBS, 4), Card(Suite.CLUBS, 8), Card(Suite.DIAMONDS, 8), Card(Suite.HEARTS, 5), Card(Suite.SPADES, 5), Card(Suite.HEARTS, 3), Card(Suite.DIAMONDS, 11), Card(Suite.HEARTS, 11), Card(Suite.SPADES, 11), Card(Suite.DIAMONDS, 2), Card(Suite.SPADES, 2)]

# hand2 = [Card(Suite.HEARTS, 4), Card(Suite.SPADES, 4), Card(Suite.SPADES, 14), Card(Suite.SPADES, 12), Card(Suite.DIAMONDS, 12), Card(Suite.HEARTS, 13), Card(Suite.DIAMONDS, 10), Card(Suite.DIAMONDS, 6), Card(Suite.DIAMONDS, 5), Card(Suite.CLUBS, 6), Card(Suite.HEARTS, 7), Card(Suite.SPADES, 8), Card(Suite.DIAMONDS, 9)]

# hand3 = [Card(Suite.SPADES, 9), Card(Suite.CLUBS, 9), Card(Suite.SPADES, 7), Card(Suite.HEARTS, 2), Card(Suite.CLUBS, 3), Card(Suite.DIAMONDS, 4), Card(Suite.CLUBS, 5), Card(Suite.SPADES, 6), Card(Suite.CLUBS, 2), Card(Suite.CLUBS, 7), Card(Suite.CLUBS, 11), Card(Suite.CLUBS, 12), Card(Suite.CLUBS, 13)]

# hand4 = [Card(Suite.SPADES, 3), Card(Suite.DIAMONDS, 3), Card(Suite.HEARTS, 12), Card(Suite.SPADES, 13), Card(Suite.DIAMONDS, 13), Card(Suite.HEARTS, 8), Card(Suite.DIAMONDS, 7), Card(Suite.HEARTS, 6), Card(Suite.HEARTS, 14), Card(Suite.DIAMONDS, 14), Card(Suite.CLUBS, 14), Card(Suite.HEARTS, 10), Card(Suite.DIAMONDS, 10)]

start = time.time()
strats = candidate_ranker.ranker(hand1)
print(f"time taken = {time.time() - start}")
print(strats)

