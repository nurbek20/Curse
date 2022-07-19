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
    return (
        <Routes>
            <Route path='/' element={<Home
                data={data}
                addToCart={addToCart}
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