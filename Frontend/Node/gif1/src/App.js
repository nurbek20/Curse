import './App.css';
import React from 'react';
import { Button, Spinner } from 'react-bootstrap';
import { useEffect, useState } from 'react';
import axios from 'axios';
import Batery from './Batery';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  let [data, setData] = useState([])
  const [val, setVal] = useState('')
  const [spin, setSpin] = useState(false)



  useEffect(() => {
    setSpin(true)
    axios.get('https://api.giphy.com/v1/gifs/trending?api_key=do6JaTti8ReVIaLQ8mPTCa3RMPif6tm3&limit=4')
      .then((res) => {
        setData(res.data.data)
        console.log(res.data.data);
        setSpin(false)
        console.log("res data>>",res);
      })
  }, [])
  const btnSearch = () => {
    setSpin(true)
    axios.get(`https://api.giphy.com/v1/gifs/search?api_key=do6JaTti8ReVIaLQ8mPTCa3RMPif6tm3&g=rating&q=${val}&limit=10`)
      .then((event) => {
        setData(event.data.data)
        console.log(event.data.data);
        setSpin(false)
      })
  }
 
 
  return (
    <>

      <div>
        <input onChange={(e) => setVal(e.target.value)} type="text" name="" id="" />
        <Button disabled={spin} onClick={btnSearch}>
          {spin ? 'loading..' : 'Search'}</Button>
      </div>
      <br /><br />
      {spin == true ?
        <div className={"loader"}></div>
        :
        data.map((item, i) => {
          return (
            <>
              <img key={i} style={{ width: 300, height: 200, padding: 5 }} src={item.images.original.url} alt="" />
            </>
          )
        })
      }
      <div>
        <Batery  />
      </div>
     
    </>
  );
}


export default App;
