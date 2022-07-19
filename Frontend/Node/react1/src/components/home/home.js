import Product from '../product/product'

const Home = ({
    data, increment, decrement
}) => {
    console.log(increment, decrement);
    return (
        <div className="home">
            <Product data={data} increment={increment} decrement={decrement} />
        </div>
    )
}

export default Home;