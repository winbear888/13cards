from deck import Card, string_to_card, card_to_string
from hand import Hand, HandInfo
from row import RowNumber

def stringify_lst_to_card_lst(stringify_lst: str) -> list[Card]:
  string_lst = stringify_lst.split(" ")
  return [string_to_card(card_str) for card_str in string_lst]

def card_lst_to_stringify_lst(card_lst : list[Card]) -> str:
  string_lst = [card_to_string(card) for card in card_lst]
  return " ".join(string_lst)

def dict_to_hand(dict_hand : dict[str, str]) -> Hand:
  row_1 = stringify_lst_to_card_lst(dict_hand["row_1"])
  row_2 = stringify_lst_to_card_lst(dict_hand["row_2"])
  row_3 = stringify_lst_to_card_lst(dict_hand["row_3"])
  return Hand(row_1, row_2, row_3)

def hand_info_to_dict(hand_info : HandInfo) -> dict:
  row_1 = [str(card) for card in hand_info.hand.rows[RowNumber.ONE].ordered_row]
  row_2 = [str(card) for card in hand_info.hand.rows[RowNumber.TWO].ordered_row]
  row_3 = [str(card) for card in hand_info.hand.rows[RowNumber.THREE].ordered_row]
  return {"row_1": row_1, "row_2": row_2, "row_3": row_3, "avg": hand_info.avg}

def hand_info_lst_to_lst_dict(hand_info_lst : list[HandInfo]) -> list[dict]:
  return [hand_info_to_dict(hand_info) for hand_info in hand_info_lst] 
