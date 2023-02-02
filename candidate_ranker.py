from deck import Card, RemainingDeck
from hand import HandInfo, is_dragon
from candidate_selector import CandidateSelector
from game import tournament

# Returns the top 10 best arrangements or less. Does not rank if the cards contain a dragon.
def ranker(target_cards : list[Card]):
  if is_dragon(target_cards):
    return "IS_DRAGON"
  target_cs = CandidateSelector(target_cards)
  target_strat = [HandInfo(hand) for hand in target_cs.unique_strategies]
  num_sim = 3
  for _ in range(num_sim):
    # TODO: while has Dragon
    has_dragon = True
    while has_dragon:
      rd = RemainingDeck(target_cards)
      rd.shuffle()
      cards_2 = rd.remainder_deck_shuffled[:13]
      cards_3 = rd.remainder_deck_shuffled[13:26]
      cards_4 = rd.remainder_deck_shuffled[26:]
      has_dragon = is_dragon(cards_2) or is_dragon(cards_3) or is_dragon(cards_4)

    hand_2_cs = CandidateSelector(cards_2)
    hand_2_strat = [HandInfo(hand) for hand in hand_2_cs.unique_strategies]
    hand_3_cs = CandidateSelector(cards_3)
    hand_3_strat = [HandInfo(hand) for hand in hand_3_cs.unique_strategies]
    hand_4_cs = CandidateSelector(cards_4)
    hand_4_strat = [HandInfo(hand) for hand in hand_4_cs.unique_strategies]
    tournament(target_strat, hand_2_strat, hand_3_strat, hand_4_strat)
  
  target_strat.sort(key=lambda x: x.avg, reverse=True)
  return target_strat if len(target_strat) <= 10 else target_strat[:10]
