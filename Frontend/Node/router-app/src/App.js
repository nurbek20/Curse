import './App.css';
import  React from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import About from './Components/About'
import Contact from './Components/Contact'
import Skill from './Components/Skill'
import Home from './Home'

function App() {
  return (
    <>
      <nav>
        <div className="container">
          <div className='navbar'>
            <h1><Link className='link'  to='/'>Home</Link></h1>
            <ul>
              <li><Link className='link' to='/contact'>Conatact</Link></li>
              <li><Link className='link' to='/skill'>Skill</Link></li>
              <li><Link className='link' to='/about'>About</Link></li>
            </ul>
          </div>
        </div>
      </nav>
      {/* <h1>Welcome to home</h1> */}
      <Routes>
        <Route path="skill" element={<Skill />} />
        <Route path="contact" element={<Contact />} />
        <Route path="About" element={<About />} />
        <Route path="/" element={<Home />} />
      </Routes>
      {/* <About />
      <Home /> */}

    </>
  );
}

export default App;
