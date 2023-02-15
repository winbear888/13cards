from enum import Enum
from deck import Card
from row import Row, RowNumber, RowStrategy

class HandStrategyEnum(Enum):
  """Either maximize a given role or just maximize the rank of that row."""
  MAX_MAX_ONE_TWO = 1
  MAX_MAX_ONE_THREE = 2
  MAX_MAX_TWO_ONE = 3
  MAX_MAX_TWO_THREE = 4
  MAX_MAX_THREE_ONE = 5
  MAX_MAX_THREE_TWO = 6
  RANK_MAX_ONE_TWO = 7
  RANK_MAX_ONE_THREE = 8
  RANK_MAX_TWO_ONE = 9
  RANK_MAX_TWO_THREE = 10
  RANK_MAX_THREE_ONE = 11
  RANK_MAX_THREE_TWO = 12

  MAX_RANK_ONE_TWO = 13
  MAX_RANK_ONE_THREE = 14
  MAX_RANK_TWO_ONE = 15
  MAX_RANK_TWO_THREE = 16
  MAX_RANK_THREE_ONE = 17
  MAX_RANK_THREE_TWO = 18
  RANK_RANK_ONE_TWO = 19
  RANK_RANK_ONE_THREE = 20
  RANK_RANK_TWO_ONE = 21
  RANK_RANK_TWO_THREE = 22
  RANK_RANK_THREE_ONE = 23
  RANK_RANK_THREE_TWO = 24

class HandStrategyObject:
  def __init__(self, hand_strategy_enum : HandStrategyEnum):
    self.hand_strategy_enum = hand_strategy_enum
    self.row_orders = self.__get_row_orders()
    self.row_strategies = self.__get_row_strategies()
  
  def __get_row_strategies(self):
    """Returns the strategies for each row."""
    if self.hand_strategy_enum.value > 12:
      return [RowStrategy.MAX_RANK, RowStrategy.MAX_RANK, RowStrategy.MAX_RANK] if self.hand_strategy_enum.value > 19 else [RowStrategy.MAX_RANK, RowStrategy.MAX, RowStrategy.MAX_RANK]
    else:
      return [RowStrategy.MAX_RANK, RowStrategy.MAX_RANK, RowStrategy.MAX] if self.hand_strategy_enum.value > 6 else [RowStrategy.MAX_RANK, RowStrategy.MAX, RowStrategy.MAX]
  
  def __get_row_orders(self):
    """Returns the row number to optimize in descending priority."""
    name = self.hand_strategy_enum.name
    parsed_name = "_".join(name.split("_")[2:])
    if parsed_name == "ONE_TWO":
      return [RowNumber.ONE, RowNumber.TWO, RowNumber.THREE]
    elif parsed_name == "ONE_THREE":
      return [RowNumber.ONE, RowNumber.THREE, RowNumber.TWO]
    elif parsed_name == "TWO_ONE":
      return [RowNumber.TWO, RowNumber.ONE, RowNumber.THREE]
    elif parsed_name == "TWO_THREE":
      return [RowNumber.TWO, RowNumber.THREE, RowNumber.ONE]
    elif parsed_name == "THREE_ONE":
      return [RowNumber.THREE, RowNumber.ONE, RowNumber.TWO]
    elif parsed_name == "THREE_TWO":
      return [RowNumber.THREE, RowNumber.TWO, RowNumber.ONE]
    else:
      raise Exception("HandStrategyEnum Error")

class Hand:
  def __init__(self, row_one: list[Card], row_two: list[Card], row_three: list[Card]):
    if len(row_one) != 3:
      raise Exception("The row_one must contain than 3 cards.")
    if len(row_two) != 5:
      raise Exception("The row_two must contain than 5 cards.")
    if len(row_three) != 5:
      raise Exception("The row_three must contain than 5 cards.")
    row_one.sort()
    row_two.sort()
    row_three.sort()
    self.rows = {}
    self.rows[RowNumber.ONE] = Row(row_one, RowNumber.ONE)
    self.rows[RowNumber.TWO] = Row(row_two, RowNumber.TWO)
    self.rows[RowNumber.THREE] = Row(row_three, RowNumber.THREE)
    if self.rows[RowNumber.ONE] > self.rows[RowNumber.TWO] or self.rows[RowNumber.TWO] > self.rows[RowNumber.THREE]:
      raise Exception("The row below must be bigger than the row above.")
  
  def __eq__(self, other):
    if self.__class__ == other.__class__:
      return self.rows[RowNumber.ONE] == other.rows[RowNumber.ONE] and self.rows[RowNumber.TWO] == other.rows[RowNumber.TWO] and self.rows[RowNumber.THREE] == other.rows[RowNumber.THREE]
    raise NotImplemented

  def __repr__(self):
    return f"""
-- Start Hand --
* row_one: {self.rows[RowNumber.ONE]}
* row_two: {self.rows[RowNumber.TWO]}
* row_three: {self.rows[RowNumber.THREE]}
-- End Hand --"""

  def beat_all(self, other):
    if self.__class__ == other.__class__:
      return self.rows[RowNumber.ONE] > other.rows[RowNumber.ONE] and self.rows[RowNumber.TWO] > other.rows[RowNumber.TWO] and self.rows[RowNumber.THREE] > other.rows[RowNumber.THREE]
    return NotImplemented

  def lose_all(self, other):
    if self.__class__ == other.__class__:
      return self.rows[RowNumber.ONE] < other.rows[RowNumber.ONE] and self.rows[RowNumber.TWO] < other.rows[RowNumber.TWO] and self.rows[RowNumber.THREE] < other.rows[RowNumber.THREE]
    return NotImplemented
  
  def settle(self, other):
    if self.__class__ == other.__class__:
      score = 0
      for row_num in RowNumber:
        score += self.rows[row_num].settle(other.rows[row_num])
      return score * 2 if self.beat_all(other) or self.lose_all(other) else score
    return NotImplemented

class HandInfo:
  def __init__(self, hand: Hand):
    self.hand = hand
    self.points_history = []
    self.sum = 0
    self.len = 0
    self.avg = 0
  
  def add_result(self, score: int):
    self.points_history.append(score)
    self.sum += score
    self.len += 1
    self.avg = self.sum / self.len

  def __repr__(self) -> str:
    return f"""
>>> Hand Info >>>
hand = {self.hand}
points average = {self.avg}
<<< Hand Info <<<
"""

def is_dragon(cards : list[Card]):
  if len(cards) != 13:
    return False
  cards.sort()
  for i in range(12):
    if cards[i].number + 1 != cards[i + 1].number:
      return False
  return True
