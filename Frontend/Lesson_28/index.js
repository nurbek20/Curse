'use strict'

// let inp = document.querySelector('input')
// let btn = document.querySelector('button')
// let h1 = document.querySelector('h1')

// let obj = {
//     name: 'Abzi',
//     age: 18,
//     married: false
// }
// let object = JSON.parse(localStorage.getItem('flex'))
// h1.innerHTML = object.age


// btn.addEventListener('click', () => {
//     // JSON.stringify(localStorage.setItem('text', obj));
//     localStorage.setItem('flex', JSON.stringify(obj))
//     // localStorage.setItem('text', obj.age)
//     h1.innerHTML = inp.value
//     inp.value = ''
// })
// console.log(str);
// let str = "Hello";

// let b = nomberOfBoolean(false)
// let b1 = false

// console.log( !!b, b?true:false, b==true)
// console.log( !!b1, b1?true:false, b1==true)

// console.log(Number(43)===Number(43)) 
// console.log(Boolean(1)===Boolean(true))
// console.log(BigInt("str")===BigInt("str"))

// const funcX=(arr, num=3)=>{
//     if (num==0) 
//     return arr
//     for(let i=0; i<num; i++){
//         let a=arr.pop()
//         arr.unshift(a)
//     }
//     return arr

// }
// console.log(funcX())

const func=(num)=>{
    return num?num+num-1:0
}
console.log(func())