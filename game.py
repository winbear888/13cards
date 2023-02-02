from hand import HandInfo

def round(hand_infos : list[HandInfo]):
  scores = [[] for _ in range(len(hand_infos))]
  beat_all = []
  for i in range(len(hand_infos)):
    j = 0
    win_all = True 
    while j < len(hand_infos):
      if i != j:
        hand_i = hand_infos[i].hand
        hand_j = hand_infos[j].hand
        win_all = win_all and hand_i.beat_all(hand_j)
      j += 1
    beat_all.append(win_all)

  for i in range(len(hand_infos) - 1):
    for j in range(i + 1, len(hand_infos)):
      hand_i = hand_infos[i].hand
      hand_j = hand_infos[j].hand
      score = hand_i.settle(hand_j)
      if beat_all[i] or beat_all[j]:
        score *= 2
      scores[i].append(score)
      scores[j].append(-score)
  sum_scores = [sum(score) for score in scores ]
  for i in range(len(hand_infos)):
    hand_infos[i].points_history.append(sum_scores[i])
