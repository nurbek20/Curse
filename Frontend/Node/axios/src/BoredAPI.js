import React, { useEffect, useState } from 'react';
import axios from 'axios'
import ReactStars from 'react-stars'

function BoredAPI() {
    const num = [1, 2, 3, 4]
    const [text, setText] = useState('')
    const [number, setNumber] = useState('')
    const ratingChanged = (newRating) => {
        console.log(newRating)
    }
    const itemClick = (e) => {
        setNumber(e)
    }
    const showClick = () => {
        axios.get('http://www.boredapi.com/api/activity?participants=' + number)
            .then((bored) => {
                setText(bored.data.activity)
                console.log(bored);
                itemClick()
            })
    }
  
    return (
        <>
            <ReactStars
                count={5}
            onChange={ratingChanged}
            size={24}
            color2={'#ffd700'} />
            {
                num.map((item) => {
                    return (
                        <>
                            <button onClick={() => itemClick(item)}>{item}</button>
                        </>
                    )
                })
            }

            <br />
            <button onClick={() => showClick()}>SHOW</button>
            <h1>{text}</h1>
        </>
    )
}
export default BoredAPI;