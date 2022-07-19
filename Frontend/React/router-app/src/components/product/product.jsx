import React from 'react'
import ProductItem from '../product-item/product-item';
import './product.css'

const Product = ({ data, increment, decrement, addToCart }) => {
  // console.log("data product>>>", data);
  return (
    <>
      <div className="container">
        <div className='product'>
          {
            data.map((element, index) => {
              // console.log(element);
              return <ProductItem
                click='add to cart'
                addToCart={() => addToCart(element.id)}
                increment={() => increment(index)}
                decrement={() => decrement(index)}
                {...element}
                key={index}
              />
            })
          }
        </div>
      </div>
    </>
  )
}

export default Product;