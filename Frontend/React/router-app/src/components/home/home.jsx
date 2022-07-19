import Product from '../product/product'

// import Cart from '../cart';
const Home = ({
    data,
    increment,
    decrement,
    addToCart
}) => {
    // console.log(increment, decrement);
    return (
        <div className="home">
            <Product 
            addToCart={addToCart}
            increment={increment} 
            decrement={decrement} 
            data={data} 
             />
            {/* <Cart addToCart={addToCart}/> */}
        </div>
    )
}

export default Home;