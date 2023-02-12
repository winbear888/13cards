from deck import Card, string_to_card, card_to_string
from hand import Hand, HandInfo
from row import RowNumber

def string_lst_to_card_lst(string_lst: str) -> list[Card]:
  return [string_to_card(card_str) for card_str in string_lst]

def card_lst_to_stringify_lst(card_lst : list[Card]) -> str:
  string_lst = [card_to_string(card) for card in card_lst]
  return " ".join(string_lst)

def dict_to_hand(dict_hand : dict[str, str]) -> Hand:
  row_1 = string_lst_to_card_lst(dict_hand["row_1"])
  row_2 = string_lst_to_card_lst(dict_hand["row_2"])
  row_3 = string_lst_to_card_lst(dict_hand["row_3"])
  return Hand(row_1, row_2, row_3)

def hand_info_to_dict(hand_info : HandInfo) -> dict:
  row_1 = [str(card) for card in hand_info.hand.rows[RowNumber.ONE].ordered_row]
  row_1_ranking = hand_info.hand.rows[RowNumber.ONE].ranking.name
  row_1_points = hand_info.hand.rows[RowNumber.ONE].points
  row_2 = [str(card) for card in hand_info.hand.rows[RowNumber.TWO].ordered_row]
  row_2_ranking = hand_info.hand.rows[RowNumber.TWO].ranking.name
  row_2_points = hand_info.hand.rows[RowNumber.TWO].points
  row_3 = [str(card) for card in hand_info.hand.rows[RowNumber.THREE].ordered_row]
  row_3_ranking = hand_info.hand.rows[RowNumber.THREE].ranking.name
  row_3_points = hand_info.hand.rows[RowNumber.THREE].points
  return {"row_1": row_1, 
          "row_1_ranking": row_1_ranking,
          "row_1_points": row_1_points,
          "row_2": row_2,
          "row_2_ranking": row_2_ranking,
          "row_2_points": row_2_points, 
          "row_3": row_3,
          "row_3_ranking": row_3_ranking,
          "row_3_points": row_3_points,  
          "avg": hand_info.avg}

def hand_info_lst_to_lst_dict(hand_info_lst : list[HandInfo]) -> list[dict]:
  return [hand_info_to_dict(hand_info) for hand_info in hand_info_lst] 
