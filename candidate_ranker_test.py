import candidate_ranker
import time
from adapter import string_lst_to_card_lst

# card_lst_1 = ["S2", "S3", "S4", "S5", "S6", "H2", "H3", "H4", "H5", "H6", "D2", "D3", "D4"]
card_lst_1 = ['S9', 'S10', 'S11', 'S12', 'C9', 'C10', 'C11', 'C12', 'H9', 'H10', 'H11', 'H12', 'H13']
hand_1 = string_lst_to_card_lst(card_lst_1)

start = time.time()
strategies = candidate_ranker.ranker(hand_1)
print(f"time taken = {time.time() - start}")
print(strategies)
