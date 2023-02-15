import React, { useState } from "react";
import axios from "axios";

const Card = ({ id, selected, setSelected, name, color }) => {
  const handleClick = () => {
    setSelected(prevSelected => {
      if (prevSelected.includes(id)) {
        return prevSelected.filter(selectedId => selectedId !== id);
      } else {
        return [...prevSelected, id];
      }
    });
  };

  return (
    <div
      style={{
        backgroundColor: selected.includes(id) ? "green" : "white",
        width: "70px",
        height: "100px",
        border: "1px solid black",
        color: color
      }}
      onClick={handleClick}
    >
      {name}
    </div>
  );
};

const DisplayCard = ({ name }) => {
  const suiteDict = {
    "S": "♠️",
    "C": "♣️", 
    "H":  "❤️", 
    "D": "♦️"
  }
  
  let royalDictInv = {
    "11": "J",
    "12": "Q",
    "13": "K",
    "14": "A",
  }

  const suitsColor = {
    "S": "black", 
    "C:": "black", 
    "H": "red", 
    "D": "red"
  }

  const displayName = (name) => {
    let suite = suiteDict[name[0]]
    let num = name.slice(1)
    if (num in royalDictInv) {
      num = royalDictInv[num]
    }
    return num + suite
  }
  return (
    <div
      style={{
        backgroundColor: "white",
        width: "70px",
        height: "100px",
        border: "1px solid black",
        color: suitsColor[name[0]]
      }}
    >
      {displayName(name)}
    </div>
  );
};

const CandidateRow = ({ candidate }) => {
  return (
    <div>
      <h1 style={{display: "flex", justifyContent: "center"}}>avg score = {candidate.avg} </h1>
      <div style={{display: "flex", justifyContent: "center"}}>{candidate.row_1.map((x, idx) => (<DisplayCard key={idx} name={x}></DisplayCard>))}</div>
      <div style={{display: "flex", justifyContent: "center"}}>{candidate.row_2.map((x, idx) => (<DisplayCard key={idx} name={x}></DisplayCard>))}</div>
      <div style={{display: "flex", justifyContent: "center"}}>{candidate.row_3.map((x, idx) => (<DisplayCard key={idx} name={x}></DisplayCard>))}</div>
      <p style={{display: "flex", justifyContent: "center"}}>Row 1: Ranking = {candidate.row_1_ranking}, Points = {candidate.row_1_points}</p>
      <p style={{display: "flex", justifyContent: "center"}}>Row 2: Ranking = {candidate.row_2_ranking}, Points = {candidate.row_2_points}</p>
      <p style={{display: "flex", justifyContent: "center"}}>Row 3: Ranking = {candidate.row_3_ranking}, Points = {candidate.row_3_points}</p>
    </div>

  )
  
};

const Deck = () => {
  const deck = [];
  const suits = ["♠️", "❤️", "♦️", "♣️"];
  const values = [
    "A",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K"
  ];
  const suitsColor = {
    "♠️": "black", 
    "♣️:": "black", 
    "❤️": "red", 
    "♦️": "red"
  }
  for (let i = 0; i < suits.length; i++) {
    for (let j = 0; j < values.length; j++) {
      deck.push({
        id: values[j] + suits[i],
        name: values[j] + suits[i],
        color: suitsColor[suits[i]]
      });
    }
  }

  const [selected, setSelected] = useState([]);

  const [uid, setUid] = useState("");
  const [message, setMessage] = useState("");
  const [candidates, setCandidates] = useState([]);
  const handleDeselectAll = () => {
    setSelected([]);
  };
  const handleArrange = () => {
    console.log(selected.length);
    if (selected.length != 13) {
      setMessage("13 cards must be selected")
      return
    }

    const transformCards = (cardStr) => {
      // suiteDict[x.slice(-2).charCodeAt(0)] + x[0]
      const suiteDict = {
        9824: "S",
        9827: "C", 
        10084: "H", 
        9830: "D"
      }

      let royalDict = {
        "J": "11",
        "Q": "12",
        "K": "13",
        "A": "14",
      }
      let suiteStr = suiteDict[cardStr.slice(-2).charCodeAt(0)];
      let numStr = cardStr.slice(0,-2);
      if (numStr in royalDict) {
        numStr = royalDict[numStr]
      }
      return suiteStr + numStr
    }
    let cardList = selected.map(x => transformCards(x))
    console.log(cardList)
    axios.post("http://127.0.0.1:5000/candidates", {"cards": cardList})
         .then(response => {
          setMessage(response.data.message)
          if("uid" in response.data) {
            setUid(response.data.uid)
          }
        })
         .catch(error => {
          setMessage(error)});
  };

  const handleGetCandidates = () => {
    if (uid.length == 0) {
      setMessage("The arrangements have to be generated first")
      return
    }
    axios.get("http://127.0.0.1:5000/candidates/" + uid)
      .then(
        reponse => {
          const data = reponse.data;
          setMessage(data["message"]);
          if ("candidate_list" in data) {
            console.log(data["candidate_list"]);
            setCandidates(data["candidate_list"]);
          }
        }
      ).catch(error => setMessage(error));

  }

  return (
    <div style={{ display: "flex", justifyContent: "center" }}>
      <div style={{ display: "flex", flexDirection: "column" }}>
        {suits.map(suit => (
          <div key={suit} style={{ display: "flex" }}>
            {deck
              .filter(card => card.id.includes(suit))
              .map(card => (
                <Card
                  key={card.id}
                  id={card.id}
                  selected={selected}
                  setSelected={setSelected}
                  name={card.name}
                  color={card.color}
                />
              ))}
          </div>
        ))}
        <div style={{ display: "flex", justifyContent: "center" }}>
          Selected cards:{" "}
          {selected.length > 0
            ? selected.map(id => id).join(", ")
            : "No cards selected"}
        </div>
        <div style={{ display: "flex", justifyContent: "center" }}>
          <button onClick={handleDeselectAll}>Deselect All</button>
        </div>
        <br/>
        <div style={{ display: "flex", justifyContent: "center" }}>
          <button onClick={handleArrange}>Generate Arrangements</button>
          <button onClick={handleGetCandidates}>Get Arragement Candidates</button>
        </div>
        {message.length > 0 && <p style={{ display: "flex", justifyContent: "center" }}>message = {message}</p>}
        {candidates.length > 0 && candidates.map((candidate, idx) => <CandidateRow key={idx} candidate={candidate}/>)}
      </div>
    </div>
  );
};

export default Deck;
