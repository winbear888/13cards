import logo from './logo.svg';
import './App.css';
import Deck from './components/Deck';

function App() {
  return (
    <div>
    <h1 style={{ display: "flex", justifyContent: "center" }}>Chinese Poker Candidate Arranger</h1>
      <Deck/>
    </div>
  );
}

export default App;
