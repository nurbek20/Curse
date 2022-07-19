// let word = "Hello"
// console.log(word.slice(0, 4))
// let i="Privet"
// for(let i = 0; i<=50; i++) {
//     console.log(i)
// }
// console.log(i)

// let u=0;
// while(u<=50 ) {
//     console.log(u);
//     i++
// }
// let i ="Privet"

// console.log(i)
// for(let i=100; i >= 0; i--) {
//     console.log(i)
//     if(i==0) {
//         console.log("hello")

//     }
// }


// for( let i=0; i <= 100; i++) {
//     console.log(i)
//     if (i ==100) {
//         console.log("Privet")
//     }
// }
// let i="Hello"
// for (let i=100; i>=0; i--) {
//     console.log(i)
// }
// console.log(i)

// for (let i=0; i<=100; i++) {
//     console.log(i)
// }
// i="Privet"
// console.log(i)

// const i={
//     fName: 'abzi'
// }
// i.fName='bayel'
// console.log(i.fName) // в такой момент можно изменить
// * 1 Создание переменного
// * 2 Условие с исп-ен переменного
// * 3 Инкремент переменного

// let vegetables = ["tomato", "potato", "carrot"]

// for (let i=0; i<vegetables.length; i++) {
//     console.log(vegetables[i])
// }

// *   Циклы
// ? while      JS deprecated -устаревшие
// ? for 3      JS В основном
// ? for in     JS Иногда
// ? for of     JS Иногда
// ? foreach    JS Редко
// ? map        React

// let vegetables = ["Monday", "Tuesday", "Wednesday"]
// let fruits = ["banana", "apple", "orange"]

// for (let i=0; i<3; i++) {
//     // * Конкантинация = +
//     console.log("On "+vegetables[i] +" i will eat "+ fruits[i])
//     // * Интерполяция = ${}
//     console.log(`On ${vegetables[i]} i will eat ${fruits[i]}`)
// }

// let sName = 'word1 word2 word3'
// let words = sName.split(' ')

// for (let i = 0; i < words.length; i++) {
//         words[i] = words[i].slice(0, 2).toUpperCase()+words[i].slice(2);
//         let result=words.join(' ');
//         console.log(result);
// }

// let str = ['asan', 'uson', 'esen', 'isin', 'usun']
// for (let i = 0; i < str.length; i++) {
//     // console.log(`${str[i].slice(0, 1)}${str[i].slice(1, 2).toUpperCase()}${str[i].slice(2)}`)
//     console.log(`${str[i].slice(0, 3)}${str[i].slice(3).toUpperCase()}`)
//     // console.log(`${str[i].slice(0,1)}${str[i].slice(1,2).toUpperCase()}${str[i].slice(2,3)}${str[i][3].toUpperCase()}`)
// }

// let sNames = ["Пугачева", "Жапаров", "Гаджиева", "Салижанов", "Асанов"]

// for (let i = 0; i < sNames.length; i++) {
//     if (sNames[i].slice(-1) == "а") {
//         console.log("Привет миссис", sNames[i])
//         // }else if (sNames[i].slice(-1)=="в") {
//         //     console.log("Привет мисстер", sNames[i])
//     }else {
//         console.log("Привет мисстер", sNames[i])
//     }
// }

// const myAwesomeArray =[1, 2, 3, 4, 5]
// console.log(myAwesomeArray.reduce((total, value)=>total * value))

// setInterval(() => {
//     console.log('hello')
// }, 1000);
// setTimeout(() => {
//     console.log('Privet');
// }, 5000);

// setTimeout(() => {
//     setInterval(() => {
//         console.log('good moning')
//     }, 1000);
// }, 5000);

