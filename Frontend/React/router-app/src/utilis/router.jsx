import { Route, Routes } from 'react-router-dom';
import Home from '../components/home';
import Cart from '../components/cart';

const RouterMain = ({
    data,
    increment,
    decrement,
    addToCart,
    cart,
    deleteItem
}) => {
    console.log(" cart >>> ", cart);
    return (
        <Routes>
            <Route path='/' element={<Home
                addToCart={addToCart}
                data={data}
                increment={increment}
                decrement={decrement} />} />
            <Route path='/cart' element={<Cart
                deleteItem={deleteItem}
                cart={cart}
            />} />
        </Routes>
    )
}

export default RouterMain;