import './App.css';
import {React, useState } from 'react';
import { data } from './data/data';
import Header from './components/header';
import Home from './components/home'
import Cart from './components/cart'
import { Routes, Route } from 'react-router-dom';
// import RouterMain from './utils/router';
// import { Form } from 'react-bootstrap';

const App = (props) => {
  console.log(props);
  const Increment = () => {
    console.log('Increment>>>', product.id);
  }
  const Decrement = () => {
    console.log('Decrement>>>');
  }

  const [product, setProduct] = useState(data);

  return (
    <>
      <Header />
      {/* <RouterMain /> */}
      <Routes>
        <Route path='/' element={<Home data={product} 
        increment={Increment} 
        decrement={Decrement} />} />
        <Route path='/cart' element={<Cart />} />
      </Routes>
    </>
  );
}

export default App;
