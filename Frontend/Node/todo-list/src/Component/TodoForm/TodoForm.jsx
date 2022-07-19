import React from 'react'
import TodoList from '../TodoList/TodoList';

const TodoForm = ({
    todos,
    setTodos,
    btnAdd,
    val,
    setVal
}) => {
    const btnForm = () => {
        btnAdd(val)
        setVal('')
    }
    const keyPress = (e) => e.key == 'Enter' ? btnForm() : '';
    return (
        <>
            <div>
                <input type="text" placeholder='New Todo...' value={val} onChange={(e) => setVal(e.target.value)} onKeyPress={(e) => keyPress(e)} name="" id="" />
                <button onClick={() => btnForm()}>Add</button>
            </div>
        </>
    )
}

export default TodoForm;