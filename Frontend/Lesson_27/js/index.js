// let h1 = document.querySelector('h1');
let btn = document.querySelector('button')
let box = document.querySelector('.box1')
let box2 = document.querySelector('.box2')

let h1 = document.querySelector('h1')

// h1.classList.add('text');



btn.addEventListener('click', () => {
    h1.classList.toggle('h1')
    box.classList.toggle('box1');
    box2.classList.toggle('box2');
})
