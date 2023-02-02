from enum import Enum
import random

class Suite(Enum):
  CLUBS = 1
  DIAMONDS = 2
  HEARTS = 3
  SPADES = 4
  def __lt__(self, other):
    if self.__class__ is other.__class__:
      return self.value < other.value
    return NotImplemented

class Card:
  def __init__(self, suite: Suite, number: int):
    if number < 1 or number > 14:
      raise Exception("number has to be >= 1 and <= 14")
    self.suite = suite
    self.number = number
  def __repr__(self):
    return f"Card({self.suite}, {self.number})"
  
  def __eq__(self, other: object) -> bool:
    if self.__class__ is other.__class__:
      return self.number == other.number and self.suite == other.suite
    return NotImplemented
  
  def __lt__(self, other):
    if self.__class__ is other.__class__:
      if self.number < other.number:
        return True
      elif self.number > other.number:
        return False
      else:
        return self.suite < other.suite 
    return NotImplemented
  
  def __hash__(self) -> int:
    return self.suite.value * 100 + self.number

class Deck:
  def gen_deck():
    deck = []
    for suite in Suite:
      for i in range(2,15):
        deck.append(Card(suite, i))
    return deck

  def __init__(self):
    self.deck = Deck.gen_deck()

  def shuffle(self, seed: int = None):
    if seed and type(seed) == int:
      random.seed(seed)
    random.shuffle(self.deck)

class RemainingDeck:
  def __init__(self, cards : list[Card]):
    deck_set = set(Deck.gen_deck())
    cards_set = set(cards)
    remainder_set = deck_set.difference(cards_set)
    self.remainder_deck = list(remainder_set)
    self.remainder_deck_shuffled = None

  def shuffle(self, seed: int = None):
    self.remainder_deck_shuffled = self.remainder_deck[:]
    if seed and type(seed) == int:
      random.seed(seed)
    random.shuffle(self.remainder_deck_shuffled)
