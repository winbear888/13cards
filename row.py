from enum import Enum
from deck import Card

class RowStrategy(Enum):
  MAX = 1
  MAX_RANK = 2

class RowState(Enum):
  INCOMPLETE = 1
  COMPLETE = 2

class RowNumber(Enum):
  ONE = 1
  TWO = 2
  THREE = 3

class Ranking(Enum):
  HIGH_CARD = 1
  PAIR = 2
  TWO_PAIR = 3
  THREE_KIND = 4
  STRAIGHT = 5
  FLUSH = 6
  FULL_HOUSE = 7
  FOUR_KIND = 8
  STRAIGHT_FLUSH = 9
  def __lt__(self, other):
    if self.__class__ is other.__class__:
      return self.value < other.value
    return NotImplemented

class Row:
  def __init__(self, raw_row: list[Card], row_num: RowNumber):
    self.row_num = row_num
    self.raw_row = raw_row
    if (row_num is RowNumber.ONE and len(raw_row) < 3) or ((row_num is not RowNumber.ONE) and len(raw_row) < 5):
      self.state = RowState.INCOMPLETE
    else:
      self.state = RowState.COMPLETE
      self.__process_row()

  def __eq__(self, other):
    if self.__class__ is other.__class__:
      return self.ordered_row == other.ordered_row
    return NotImplemented
    
  def __lt__(self, other):
    if self.__class__ is other.__class__:
      if self.ranking != other.ranking:
        return self.ranking < other.ranking
      return self.freq_lst < other.freq_lst
    return NotImplemented

  def __repr__(self) -> str:
    if self.state == RowState.COMPLETE:
      return f"Row: ranking = {self.ranking}, freq_lst = {self.freq_lst}, points = {self.points}, row_num = {self.row_num}, ordered_row = {self.ordered_row}"
    else:
      return f"Incomplete Row: raw_row = {self.raw_row}, row_num = {self.row_num}"
  
  def settle(self, other):
    if self.__class__ is other.__class__:
      if self.row_num != other.row_num:
        raise Exception("Can only settle the same row.")
      if self.state == RowState.INCOMPLETE or other.state == RowState.INCOMPLETE:
        raise Exception("Row Incomplete")
      if self > other:
        return self.points
      elif self < other:
        return -1 * other.points
      else:
        return 0    
    return NotImplemented

  # assigns attribute self.freq_lst : [[freq, number]]
  def __create_freq_lst(self):
    dic ={}
    for card in self.raw_row:
      if card.number == 1:
        card.number =  14
      if card.number in dic:
        dic[card.number] += 1
      else:
        dic[card.number] = 1
    freq_lst = [[x[1], x[0]] for x in dic.items()]
    freq_lst.sort(reverse=True)
    # Ace can be considered a 1 in a straight.
    if freq_lst == [[1,14], [1,5], [1,4], [1,3], [1,2]]:
      freq_lst = [[1,5], [1,4], [1,3], [1,2], [1,1]]
      for card in self.raw_row:
        if card.number == 14:
          card.number = 1
          break
    self.freq_lst = freq_lst
  
  def __create_ordered_row(self):
    nested_lst = [[] for _ in range(len(self.freq_lst))]
    for card in self.raw_row:
      for i in range(len(self.freq_lst)):
        if card.number == self.freq_lst[i][1]:
          nested_lst[i].append(card)
          break
    self.ordered_row = []
    for lst in nested_lst:
      lst.sort(reverse=True)
      self.ordered_row.extend(lst)

  # This function assigns
  # self.ranking
  # self.freq_lst
  # self.points
  def __process_row(self):
    self.__create_freq_lst()
    self.__create_ordered_row()
    num_ace = 0
    for [freq, num] in self.freq_lst:
      if num == 14:
        num_ace = freq
    points = 1
    if self.__is_straight_flush():
      points = 6
      if num_ace == 1:
        points = 7
      self.ranking = Ranking.STRAIGHT_FLUSH
    elif self.__is_four_kind():
      if num_ace == 4:
        points = 7
      self.ranking = Ranking.FOUR_KIND
    elif self.__is_full_house():
      if num_ace == 3 and self.row_num is RowNumber.TWO:
        points = 2
      self.ranking = Ranking.FULL_HOUSE
    elif self.__is_flush():
      self.ranking = Ranking.FLUSH
    elif self.__is_straight():
      self.ranking = Ranking.STRAIGHT
    elif self.__is_three_kind():
      if num_ace == 3:
        if self.row_num is RowNumber.ONE:
          points = 6
        elif self.row_num is RowNumber.TWO:
          points = 2
      self.ranking = Ranking.THREE_KIND
    elif self.__is_two_pair():
      self.ranking = Ranking.TWO_PAIR
    elif self.__is_pair():
      if num_ace == 2 and self.row_num is RowNumber.ONE:
        points = 2
      self.ranking = Ranking.PAIR
    else:
      self.ranking = Ranking.HIGH_CARD
    self.points = points
    
  def __is_straight_flush(self):
    return self.__is_flush() and self.__is_straight()
  
  def __is_four_kind(self):
    if self.row_num is RowNumber.ONE:
      return False
    return len(self.freq_lst) == 2 and self.freq_lst[0][0] == 4
  
  def __is_full_house(self):
    if self.row_num is RowNumber.ONE:
      return False
    return len(self.freq_lst) == 2 and self.freq_lst[0][0] == 3
  
  def __is_flush(self):
    if self.row_num is RowNumber.ONE:
      return False    
    suite_set = set([card.suite for card in self.raw_row])
    return len(suite_set) == 1

  def __is_straight(self):
    if self.row_num is RowNumber.ONE:
      return False
    return len(self.freq_lst) == 5 and self.freq_lst[0][1] - self.freq_lst[4][1] == 4
  
  def __is_three_kind(self):
    if self.row_num is RowNumber.ONE:
      return len(self.freq_lst) == 1
    return len(self.freq_lst) == 3 and self.freq_lst[0][0] == 3

  def __is_two_pair(self):
    if self.row_num is RowNumber.ONE:
      return False
    return self.freq_lst[0][0] == 2 and self.freq_lst[1][0] == 2

  def __is_pair(self):
    if self.row_num is RowNumber.ONE:
      return len(self.freq_lst) == 2
    return len(self.freq_lst) == 4
