from deck import Card, Suite
from hand import Hand, HandStrategyEnum, HandStrategyObject
from row import RowStrategy, RowNumber, Row

class CandidateSelector:
  def __init__(self, cards : list[Card]):
    if len(cards) != 13:
      raise Exception("A hand must contain 13 cards.")
    self.strategies = {}
    for i in range(11):
      for j in range(i + 1, 12):
        for k in range(j + 1, 13):
          self.find_best([cards[i], cards[j], cards[k]], cards[:i] + cards[i + 1:j] + cards[j+1:k] + cards[k+1:])
  
  def find_best(self, row_1 : list[Card], remainders : list[Card]):
    for idx_1 in range(6):
      for idx_2 in range(idx_1 + 1, 7):
        for idx_3 in range(idx_2 + 1, 8):
          for idx_4 in range(idx_3 + 1, 9):
            for idx_5 in range(idx_4 + 1, 10):
              row_2 = [remainders[idx_1], remainders[idx_2], remainders[idx_3], remainders[idx_4], remainders[idx_5]]
              row_3 = remainders[:idx_1] + remainders[idx_1 + 1: idx_2] + remainders[idx_2 + 1: idx_3] + remainders[idx_3 + 1: idx_4] + remainders[idx_4 + 1: idx_5] + remainders[idx_5 + 1:]
              try:
                hand = Hand(row_1, row_2, row_3)
                for hand_strategy_enum in HandStrategyEnum:
                  self.strategies[hand_strategy_enum] = hand if hand_strategy_enum not in self.strategies else CandidateSelector.__bigger_hand(self.strategies[hand_strategy_enum], hand, hand_strategy_enum)
              except Exception as e:
                continue
  
  def __bigger_hand(current : Hand, new : Hand, hand_strategy_enum: HandStrategyEnum):
    hand_strategy_enum_object = HandStrategyObject(hand_strategy_enum)
    row_strategies = hand_strategy_enum_object.row_strategies
    row_orders = hand_strategy_enum_object.row_orders
    for i in range(3):
      rowNum : RowNumber = row_orders[i]
      row_strategy : RowStrategy = row_strategies[i]  
      if row_strategy == RowStrategy.MAX:
        if new.rows[rowNum] > current.rows[rowNum]:
          return new
        elif new.rows[rowNum] < current.rows[rowNum]:
          return current
      elif row_strategy == RowStrategy.MAX_RANK:
        if new.rows[rowNum].ranking > current.rows[rowNum].ranking:
          return new
        elif new.rows[rowNum].ranking < current.rows[rowNum].ranking:
          return current
      else:
        raise Exception("row_strategy invalid")
    
    for i in range(1, -1, -1):
      rowNum : RowNumber = row_orders[i]
      if new.rows[rowNum] > current.rows[rowNum]:
        return new
      elif new.rows[rowNum] < current.rows[rowNum]:
        return current

    return current
  
  def __repr__(self) -> str:
    return f"""
------- start CandidateSelector --------
{self.strategies}
------- end CandidateSelector --------
"""
