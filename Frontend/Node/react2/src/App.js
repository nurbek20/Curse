import './App.css';
import react , { Component}  from 'react';
import         { render   }  from 'react-dom';
import { React, useState } from 'react';
import { data } from './data/data';
import Header from './components/header';
import Home from './components/home'
import Cart from './components/cart'
import { Routes, Route } from 'react-router';


const App = (props) => {

  const [product, setProduct] = useState(data);
  const [cart, setCart] = useState(JSON.parse(localStorage.getItem('cart')) || [])
  const lenght = cart.length

  // let arr = [1, 2, 3, 4, 5, 6, 7]
  // let before = arr.slice(0, 3)
  // let after = arr.slice(4)
  // const newArr = [...before, ...after]
  // console.log(newArr)


  const increment = (i) => {
    console.log('Increment>>>', i);
    const index = product.findIndex((elem, index) => index === i)
    const old = product[index]
    const newElem = {
      ...old,
      count: old.count + 1,
    }

    const newArr = [...product.slice(0, index), newElem, ...product.slice(index + 1)]
    setProduct(newArr)
  }
  const decrement = (i) => {
    console.log('Decrement>>>', i);
    const index = product.findIndex((elem, index) => index === i)
    console.log('index product', index)
    const old = product[index]
    const newElem = {
      ...old,
      count: old.count === 1 ? 1 : old.count - 1

    }

    const newArr = [...product.slice(0, index), newElem, ...product.slice(index + 1)]
    setProduct(newArr)
  }
  const deleteItem = (i) => {
    console.log(i)
    const index = cart.findIndex((elem, index) => index === i)
    const newArr = [...cart.slice(0, index), ...cart.slice(index + 1)]
    setCart(newArr)

  }

  const addToCart = (i) => {
    console.log("cart >>>", i)
    const check = cart.every(elem => elem.id !== i)
    if (!check) {
      return alert('tovar dobavlen')
    } else {
      const elem = product.find(elem => elem.id === i)
      console.log(elem)
      const newArr = [...cart, elem]
      localStorage.setItem('cart', JSON.stringify(newArr))
      setCart(newArr)
    }
  }

  return (
    <>
      <Header lenght={lenght} />
      {/* <RouterMain /> */}
      <Routes>
        <Route path='/' element={<Home
          cart={cart}
          addToCart={addToCart}
          data={product}
          increment={increment}
          decrement={decrement} />} />
        <Route path='/cart' element={<Cart />} />
      </Routes>
    </>
  );
}

export default App;
