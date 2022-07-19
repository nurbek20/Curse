import { Link } from "react-router-dom"
// import Header from "./header";


const Header = ({ length }) => {
    return (
        <div className="header">

            <form>
                <h1>to: Mozilla</h1>

                <div id="from">
                    <label for="name">from:</label>
                    <input type="text" id="name" name="user_name"/>
                </div>

                <div id="reply">
                    <label for="mail">reply:</label>
                    <input type="email" id="mail" name="user_email"/>
                </div>

                <div id="message">
                    <label for="msg">Your message:</label>
                    <textarea id="msg" name="user_message"></textarea>
                </div>

                <div class="button">
                    <button type="submit">Send your message</button>
                </div>
            </form>
            <div><Link to='/'>Home</Link></div>
            <div><Link to='/cart'>Basket {length}</Link></div>
        </div>
    )
}

export default Header;