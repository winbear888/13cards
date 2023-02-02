from deck import Card
from hand import HandInfo
from candidate_selector import CandidateSelector
from game import tournament

class CandidateRanker:
  def __init__(self, cards_1 : list[Card], cards_2 : list[Card], cards_3 : list[Card], cards_4 : list[Card]):
    cs_1 = CandidateSelector(cards_1)
    candidates_1 = [HandInfo(hand) for hand in cs_1.unique_strategies]
    cs_2 = CandidateSelector(cards_2)
    candidates_2 = [HandInfo(hand) for hand in cs_2.unique_strategies]
    cs_3 = CandidateSelector(cards_3)
    candidates_3 = [HandInfo(hand) for hand in cs_3.unique_strategies]
    cs_4 = CandidateSelector(cards_4)
    candidates_4 = [HandInfo(hand) for hand in cs_4.unique_strategies]

    tournament(candidates_1, candidates_2, candidates_3, candidates_4)
    
    candidates_1.sort(key=lambda x: x.avg, reverse=True)
    candidates_2.sort(key=lambda x: x.avg, reverse=True)
    candidates_3.sort(key=lambda x: x.avg, reverse=True)
    candidates_4.sort(key=lambda x: x.avg, reverse=True)

    self.ranked_1 = candidates_1
    self.ranked_2 = candidates_2
    self.ranked_3 = candidates_3
    self.ranked_4 = candidates_4

