import React from "react";
import { useState, useEffect } from "react";

const Batery = () => {
    const [count, setCount] = useState(0)
    let color = 'red'
    count >= 2 ? (count === 3 ? color = 'green' : color = 'yellow') : color = 'red';
    useEffect(() => {
        let int = setInterval(() => {
            setCount(count => count === 3 ? setCount(0) : setCount(count + 1))
        }, 1000)
        return () => clearInterval(int)
    }, [])


    return (
        <>
            <section className={"batery"}>
                <div className={"batery__box"}>
                    <div style={{ backgroundColor: color }} className={count >= 1 ? 'box1' : ''}></div>
                    <div style={{ backgroundColor: color }} className={count >= 2 ? 'box2' : ''}></div>
                    <div style={{ backgroundColor: color }} className={count >= 3 ? 'box3' : ''}></div>
                </div>
                <div className={"box"}></div>
            </section>

        </>
    )
}
export default Batery;