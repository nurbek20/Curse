import { Route, Routes } from 'react-router-dom';
import Home from '../components/home';

const RouterMain = ({data, increment, decrement}) => {
    console.log()
    return (
        <Routes>
            <Route path='/' element={<Home data={data} increment={increment} decrement={decrement}/> } />
            <Route path='/cart' element={<Cart />} />
        </Routes>
    )
}

export default RouterMain;