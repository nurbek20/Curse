'use strict'

let btn = document.querySelector('button');
let span = document.querySelector('span');
let i = 0;
let func = () => {
    document.body.style.backgroundColor = 'black'
    document.body.style.color = '#fff'
}
let white = () => {
    document.body.style.backgroundColor = 'white';
    document.body.style.color = '#333';
}
if (localStorage.getItem('text') == 'black') {
    func()
} else {
    white()
}

btn.addEventListener('click', () => {
    if (i % 2 == 0) {
        i++
        localStorage.setItem('text', 'black')
        func()
    } else {
        localStorage.setItem('text', 'white')
        white()
        i = 0;
    }
})

localStorage.getItem('text')

let h1 = document.querySelector('h1');
let obj = {
    name: 'aziz',
    age: 18
}

localStorage.setItem('car', JSON.stringify(obj))
h1.innerHTML = localStorage.getItem('car')
let model = 123n
console.log(typeof(model)); 