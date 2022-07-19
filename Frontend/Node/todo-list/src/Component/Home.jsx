import React from 'react';
import TodoForm from './TodoForm/TodoForm';
import { useState } from 'react';
import TodoList from './TodoList/TodoList';

const Home = () => {
    const [todos, setTodos] = useState([])
    const [val, setVal] = useState('')


    const btnDel = (id) => {
        setTodos([...todos.filter((item) => item.id !== id )])
    }
    const btnToggle = () => { }
    const btnChange = () => { }
    const btnAfterChange = () => { }



    const btnAdd = (inpVal) => {
        if (inpVal) {
            const newItem = {
                id: Math.random().toString(36).slice(3, 9),
                text: inpVal,
                complete: false,
                change: false
            }
            setTodos([...todos, newItem])
        }
    }
    return (
        <>
            <h1>Number of Todos {todos.length}</h1>
            <TodoForm
                todos={todos}
                setTodos={setTodos}
                btnAdd={btnAdd}
                val={val}
                setVal={setVal}
            />
            {todos.map((item) => {
                return (
                    <TodoList
                        item={item}
                        todos={todos}
                        setTodos={setTodos}
                        btnDel={btnDel}
                        btnToggle={btnToggle}
                        btnChange={btnChange}
                        btnAfterChange={btnAfterChange}
                    />
                )
            })}
        </>
    )
}

export default Home;
