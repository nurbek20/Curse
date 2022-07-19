import instance from './settings'
import Cookies from 'js-cookie'

const register = (object) => {
    return instance.post("email/register", object)
}
const login = (object) => {
    return instance.post("email/login", object)
}
const getMe = (object) => {
    return instance.get("me")
}
   // import React from 'react'
        // import { Link } from 'react-router-dom'
        // import { useForm } from 'react-hook-form'
        // import { useState } from 'react';

        // let counter = 0;
        // const Server = () => {
        //     const { register, handleSubmit } = useForm();
        //     const [data, setData]=useState("")
        //     // const onSubmit = (d) => {
        //     //     console.log(JSON.stringify(d))
        //     // };
        //     return (
        //         <>
        //             <div className="container">
        //                 <div className="form__content">
        //                     <div className="contact">
        //                         <form onSubmit={handleSubmit((data)=>setData(JSON.stringify(data)))}>
        //                             <div>
        //                                 <input  type="text" {...register("FirstName")} placeholder='First Name' name="" />
        //                             </div>
        //                             <div>
        //                                 <input type="text" {...register("LastName")} placeholder='Last Name' name="" />
        //                             </div>
        //                             <div>
        //                                 <input {...register("Email")} type="email" placeholder='Email' name="" id="" />
        //                             </div>
        //                             <div>
        //                                 <p>Render: <span>{counter++}</span></p>
        //                             </div>
        //                             <div className="button">
        //                                 <button className='btn' type="submit">Войти</button>
        //                             </div>
        //                             <p>{data}</p>
        //                             <div><h3><Link className='link' to='/cart'>Регистрация</Link></h3></div>
        //                         </form>

        //                     </div>
        //                 </div>
        //             </div>
        //         </>

        //     )
        // }

        // export default Server;