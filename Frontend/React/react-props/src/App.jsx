import './App.css';
import { Routes, Route } from 'react-router-dom';
// import Message from './components/message';
// import Login from './lodin';

const App = () => {
  // const text = [
  //   {
  //     text: 'hello',
  //     sName: 'ulukman',
  //     phone: 550505979
  //   },
  //   {
  //     text: 'world',
  //     sName: 'nurbek',
  //     phone: 550505979
  //   },
  //   {
  //     text: 'front',
  //     sName: 'abzi',
  //     phone: 23234534647
  //   },
  //   {
  //     text: 'beckend',
  //     sName: 'shaabolot',
  //     phone: 3476398729
  //   },
  //   {
  //     text: 'beckend2',
  //     sName: 'jumagul',
  //     phone: 98289374748
  //   },
  //   {
  //     text: 'beckend4',
  //     sName: 'mubina',
  //     phone: 909112938
  //   },
  //   {
  //     text: 'beckend5',
  //     sName: 'baiel',
  //     phone: 550505979
  //   },]


  return (
    <div className="App">
      <nav>
        <div className="container">
          <div className='navbar'>
            <img src="" alt="IMG" />
            <div className='list'>
              <button>Войти</button>
              <button>Регистрация</button>
            </div>
          </div>
          {/* <Login /> */}
          {/* <div>heelo itc bootcamp</div>
        <div>heelo itc bootcamp</div>
        <div>heelo itc bootcamp</div>
        <div>heelo itc bootcamp</div>
        <div>heelo itc bootcamp</div>
        <div>heelo itc bootcamp</div>
        <div>heelo itc bootcamp</div>
        <div>heelo itc bootcamp</div>
        <div>heelo itc bootcamp</div>
        <div>heelo itc bootcamp</div> */}
          {/* {text.map((element, index) => {
          return (
            <Message
              {...element}
              key={index} />
          )
        })} */}


        </div>
      </nav>

    </div>
  );
}

export default App;
