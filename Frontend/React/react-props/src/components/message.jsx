import React from 'react'

const Message = (props) => {
  return (
    <div>
      <h1>message: {props.text} </h1>
      <h2>name: {props.sName}</h2>
      <h2>Phone: {props.phone}</h2>
    </div>
  )
}

export default Message;