import React from 'react'
import ProductItem from '../product-item/product-item'

const Cart = ({
  cart,
  deleteItem
}) => {
  return (
    <>
      <div className='product'>
        {cart.map((element, index) => {
          return <ProductItem
            addToCart={() => deleteItem(index)}
            click='delete'
            key={index}
            {...element}
          />
        })}
      </div>
    </>
  )
}

export default Cart;