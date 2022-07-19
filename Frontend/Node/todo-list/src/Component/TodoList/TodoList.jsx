import React from 'react'

const TodoList = ({
    item,
    btnDel,
    btnToggle,
    btnChange,
    btnAfterChange
}) => {



    return (
        <>
            <div key={item.id}>
                <span>
                    {item.text}
                </span>
                <button>Change</button>
                <button onClick={() => btnDel(item.id)}>
                    X
                </button>
            </div>
        </>
    )
}

export default TodoList;