import './App.css';
import React from 'react';
import axios from 'axios'
import { useState, useEffect } from 'react';
import BoredAPI from './BoredAPI'

function App() {
  const [obj, setObj] = useState('');
  const btnClick = () => {
    axios.get('https://api.kanye.rest/')
      .then((res) => {
        setObj(res.data.quote);
        console.log(res);
      })
  }
  useEffect(() => {
    btnClick()
  }, [])

  return (
    <div className="App">
      <button onClick={() => btnClick()}>click</button>
      <h1>{obj}</h1>
      <BoredAPI />
    </div>
  );
}

export default App;
