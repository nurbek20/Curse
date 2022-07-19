import Product from '../product/product'

// import Cart from '../cart';
const Home = ({
    data,
    increment,
    decrement,
    addToCart,
}) => {
    // console.log(increment, decrement);
    return (
        <div className="home">
            <Product 
            data={data} 
            increment={increment} 
            decrement={decrement} 
            addToCart={addToCart} />
            {/* <Cart addToCart={addToCart}/> */}
        </div>
    )
}

export default Home;