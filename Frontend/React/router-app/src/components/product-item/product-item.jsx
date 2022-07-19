import React from 'react'
import './product-item.css'
// import { useState } from 'react';

const ProductItem = (props) => {
    // console.log(props);
    const { title, descrection, count, img, price, discount, increment, decrement, addToCart, click } = props;

    return (
        <>
                <div className='card'>
                    {discount !== null ? <p style={{
                        backgroundColor: 'red',
                        display: 'inline-block',
                        borderRadius: '50%',
                        padding: '10px',
                        color: '#fff'
                    }}>{discount} %</p> : null}
                    <h2>{title}</h2>
                    <p>{descrection}</p>
                    <img width={200} height={200} src={img} alt="" />
                    <div className='btn-group'>
                        <button onClick={decrement}>-</button>
                        <span>{count}</span>
                        <button onClick={increment}>+</button>
                    </div>
                    <span>{price}</span>
                    <button style={{ marginLeft: '50px' }} onClick={addToCart}>{click}</button>
                </div>
        </>
    )
}

export default ProductItem;