from enum import Enum
import random

class Suite(Enum):
  CLUBS = 1
  DIAMONDS = 2
  HEARTS = 3
  SPADES = 4
  def __lt__(self, other):
    """All suites are equal. This function is just used to ensure
    the uniqueness of the order of sorted cards.
    """
    if self.__class__ is other.__class__:
      return self.value < other.value
    return NotImplemented

class Card:
  def __init__(self, suite: Suite, number: int):
    if number < 1 or number > 14:
      """Both 1 and 14 are used to represent the Ace."""
      raise Exception("number has to be >= 1 and <= 14")
    self.suite = suite
    self.number = number
  def __repr__(self):
    return card_to_string(self)
  
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

def string_to_card(card_str: str) -> Card:
  """Converts a string to a card object."""
  char_to_suite = {"C": Suite.CLUBS, "D": Suite.DIAMONDS, "H": Suite.HEARTS, "S": Suite.SPADES}
  suite_str = card_str[:1]
  suite = char_to_suite[suite_str]
  number = int(card_str[1:])
  return Card(suite, number)

def card_to_string(card: Card) -> str:
  """Converts a card object to a string."""
  suite_to_char = {Suite.CLUBS: "C", Suite.DIAMONDS: "D", Suite.HEARTS: "H", Suite.SPADES: "S"}
  number = 14 if card.number == 1 else card.number
  return suite_to_char[card.suite] + str(number)

class RemainingDeck:
  def gen_deck():
    """Generates a deck"""
    deck = []
    for suite in Suite:
      for i in range(2,15):
        deck.append(Card(suite, i))
    return deck

  def __init__(self, cards : list[Card]):
    deck_set = set(RemainingDeck.gen_deck())
    cards_set = set(cards)
    remainder_set = deck_set.difference(cards_set)
    self.remainder_deck = list(remainder_set)
    self.remainder_deck_shuffled = None

  def shuffle(self, seed: int = None):
    """Shuffles self.remainder_deck_shuffled"""
    self.remainder_deck_shuffled = self.remainder_deck[:]
    if seed and type(seed) == int:
      random.seed(seed)
    random.shuffle(self.remainder_deck_shuffled)
