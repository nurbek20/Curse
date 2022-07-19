import React from 'react'
import ProductItem from '../product-item/product-item';
import './product.css'

const Product = ({ data, increment, decrement }) => {
  console.log("data product>>>", data);
  return (
    <div className='product'>
      {
        data.map((element,index)=> {
          console.log(element);
          return <ProductItem {...element} key={index} increment={increment} decrement={decrement}/>
        })
      }
    </div>
  )
}

export default Product;