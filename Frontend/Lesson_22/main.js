// ? Первый вариант
// let text =document.getElementsByClassName('text')
// let h3 =document.getElementById('h3')
// let h1 = document.getElementsByTagName('h1')

// ? Второй вариант
// let text = document.querySelectorAll('.text')
// let h3 = document.querySelector('#h3')
// let h1 = document.querySelectorAll('h1')

// ? 1 createElement AppendChild
// ? 2 Event
// ? 3 OnClick onchange
// ? 4 if else тернарные условия
// ? 5 повторения все темы


// let btn = document.createElement('button');
// btn.className = 'btn';
// btn.innerHTML = 'Click';
// document.body.appendChild(btn);
// let i = 0
// btn.onclick = function () {
//     console.log(i)
//     i++
// }
// btn.onclik = () => {
//     console.log(1);
// }

// btn.addEventListener('click', () => {
//     console.log(2);
// })
// let inp = document.createElement('input');
// inp.className='inp'
// document.body.appendChild(inp)

// inp.onchange=()=> {
//     // h1.innerHTML=inp
//     console.log(inp.value);
// }

// let menu = document.getElementsByClassName('menu')[0];
// let content = document.getElementsByClassName('content')[0];
// let close = document.getElementsByClassName('close')[0];

// content.style.display = 'none'
// close.style.display = 'none'


// menu.addEventListener('click', () => {
//     content.style.display = 'block'
//     close.style.display = 'block'
// })

// close.addEventListener('click', () => {
//     content.style.display = 'none'
//     close.style.display = 'none'
// })

// let btn = document.getElementsByClassName('btn')[0]
// let p = document.getElementsByClassName('p')[0]
// btn.addEventListener('click', () => {
//     p.innerHTML = 'Hello World!!!'
// })
