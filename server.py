from flask import Flask, jsonify, request
import threading
import adapter
from candidate_ranker import ranker
from deck import Card
import hashlib
from flask_cors import CORS #comment this on deployment

app = Flask(__name__)
CORS(app) #comment this on deployment

# None, list(HandInfo), or 'IS_DRAGON'
top_ten_dict = {}

@app.post('/candidates')
def candidates_post():
  # data is a dict
  card_lst = adapter.string_lst_to_card_lst(request.get_json()["cards"])
  card_lst.sort()
  uid = gen_uid(card_lst)
  # Indicates that the processing has started
  status_code = 202
  if uid not in top_ten_dict:
    top_ten_dict[uid] = None
    thread = threading.Thread(target=process_request, args=(card_lst,uid))
    thread.start()
    msg = "POST: Generating new candidates." 
  else:
    if top_ten_dict[uid] == None:
      msg = "POST: Candidate generation in progress."
    else:
      msg = "POST: Candidates generated. Call the GET endpoint to retreive the results."
      status_code = 201
  response = jsonify({'message': msg, "uid":uid})
  response.status_code = status_code
  return response

def process_request(card_lst : list[Card], uid : str):
  candidate_lst = ranker(card_lst)
  top_ten_dict[uid] = candidate_lst if candidate_lst == "IS_DRAGON" else adapter.hand_info_lst_to_lst_dict(candidate_lst)

def gen_uid(card_lst : list[Card]) -> int:
  str_lst = [str(card) for card in card_lst]
  string = "".join(str_lst)
  # Create a SHA-256 hash object
  sha256 = hashlib.sha256()
  # Update the hash with the input string
  sha256.update(string.encode())
  # Return the hexadecimal representation of the hash
  return sha256.hexdigest()

@app.get('/candidates/<uid>')
def candidates_get(uid):
  msg = "GET: Candidates have not been generated"
  has_candidates = False
  if uid in top_ten_dict:
    if top_ten_dict[uid] == None:
      msg = "GET: Candidate generation in progress"
    elif top_ten_dict[uid] == "IS_DRAGON":
      msg = "GET: IS_DRAGON"
    else:
      msg = "GET: Candidates Generated"
      has_candidates = True
  return jsonify({'message': msg, 'candidate_list': top_ten_dict[uid]}) if has_candidates else jsonify({'message': msg})

if __name__ == '__main__':
    app.run()