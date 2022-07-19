import { Link } from "react-router-dom"
// import Header from "./header";


const Header = () => {
    return(
        <div className="header">
            <div><Link to='/'>Home</Link></div>
            <div><Link to='/cart'>Basket {0}</Link></div>
        </div>
    )
}

export default Header;