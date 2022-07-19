import React from 'react'
import './product-item.css'
import { useState } from 'react';
const ProductItem = (props) => {
    console.log(props);
    const { id, title, descrection, img, price, discount, count, increment, decrement } = props;
    const [pri, setPri] = useState(price)
    const [counter, setCounter] = useState(count)

    const btnClick = () => {
        setPri(price + pri)
        setCounter(count + counter)
        increment()
    };

    const btnClickk = () => {
        setPri(price - pri)
        setCounter(count - counter)
        decrement()
    }
    return (
        <>
            <div className='card'>
                <h2>{title}</h2>
                <p>{descrection}</p>
                <img width={200} height={200} src={img} alt="" />
                <div className='btn-group'>
                    <button onClick={(increment) => btnClick(increment)}>+</button>
                    <span>{count}</span>
                    <button onClick={() => btnClickk()}>-</button>
                </div>
                <span>{price}</span>

            </div>
        </>
    )
}

export default ProductItem;