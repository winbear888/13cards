from enum import Enum
from deck import Card
from row import Row, RowNumber, RowStrategy

class HandStrategyEnum(Enum):
  MAX_ONE_TWO = 1
  MAX_ONE_THREE = 2
  MAX_TWO_ONE = 3
  MAX_TWO_THREE = 4
  MAX_THREE_ONE = 5
  MAX_THREE_TWO = 6
  RANK_ONE_TWO = 7
  RANK_ONE_THREE = 8
  RANK_TWO_ONE = 9
  RANK_TWO_THREE = 10
  RANK_THREE_ONE = 11
  RANK_THREE_TWO = 12

class HandStrategyObject:
  def __init__(self, hand_strategy_enum : HandStrategyEnum):
    self.hand_strategy_enum = hand_strategy_enum
    self.row_orders = self.__get_row_orders()
    self.row_strategies = self.__get_row_strategies()
  
  def __get_row_strategies(self):
    return [RowStrategy.MAX_RANK, RowStrategy.MAX_RANK, RowStrategy.MAX] if self.hand_strategy_enum.value > 6 else [RowStrategy.MAX_RANK, RowStrategy.MAX, RowStrategy.MAX]
  
  def __get_row_orders(self):
    name = self.hand_strategy_enum.name
    parsed_name = "_".join(name.split("_")[1:])
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
  def __init__(self, row_one: set[Card], row_two: set[Card], row_three: set[Card]):
    if len(row_one) != 3:
      raise Exception("The row_one must contain than 3 cards.")
    if len(row_two) != 5:
      raise Exception("The row_two must contain than 5 cards.")
    if len(row_three) != 5:
      raise Exception("The row_three must contain than 5 cards.")
    self.rows = {}
    self.rows[RowNumber.ONE] = Row(row_one, RowNumber.ONE)
    self.rows[RowNumber.TWO] = Row(row_two, RowNumber.TWO)
    self.rows[RowNumber.THREE] = Row(row_three, RowNumber.THREE)
    if self.rows[RowNumber.ONE] > self.rows[RowNumber.TWO] or self.rows[RowNumber.TWO] > self.rows[RowNumber.THREE]:
      raise Exception("The row below must be bigger than the row above.")

  def __repr__(self):
    return f"""
-- Start Hand --
* row_one: {self.rows[RowNumber.ONE]}
* row_two: {self.rows[RowNumber.TWO]}
* row_three: {self.rows[RowNumber.THREE]}
-- End Hand --
"""