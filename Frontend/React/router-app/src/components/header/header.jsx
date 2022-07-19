import { Link } from "react-router-dom"
import './header.css'
// import Header from "./header";



const Header = ({ length }) => {

    return (
        <>
            <nav>
                <div className="container">
                    <div className="navbar">
                        <div><Link className="link" to='/'>Home</Link></div>
                        <div className="list">
                            <ul>
                                <li><Link className="link" to='/cart'>Basket ({length})</Link></li>
                                {/* <li></li>
                                <li></li> */}
                            </ul>
                            <button className="btn"><Link className="link" to='/server'> Войти</Link></button>
                            <button className="btn">Регистрация</button>
                        </div>
                    </div>
                </div>
            </nav>
            
        </>
    )
}

export default Header;