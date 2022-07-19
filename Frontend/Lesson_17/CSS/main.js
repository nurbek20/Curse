// ! let fruits = ['banana', 'apple', ['avaqado', 'pineapple','ananas', 'orange'] ];
// ! console.log(fruits[1][1])
// ! console.log(fruits[2][1])

// ! let names = ['Abdulaziz', 'Shaabolot', 'Razzak', 'Baiel', 'Nurbek', 'Mubina']
// ! console.log(names)


// ! let num=14
// ! num=15               // можно изменять

// !const num= 14        //неизменяемый 
// !num=[];

// console.log(num)
// * && и
// * || или

// ! let qFirst = +prompt('Введитте первое число')
// ! let qSecond= +prompt('Введитте второе число')
// ! let arrNumber = [10, 27, 32, 54, 96]
// ! if (qFirst === arrNumber[2] || qSecond ===arrNumber[1]) {
// !     console.log(true)
// ! } else {
// !     console.log(false)
// ! }
// ! let data = ['admin', 123]
// ! let admin = prompt('Введите логинь: ')
// ! let parol = +prompt('Введите пароль: ')
// ! if (admin === data[0] && parol=== data[1]) {
// !     console.log('Дабро пажаловать')
// ! }else {
// !     console.log('Неверный логин или пароль')
// ! }

// * let myName = prompt('Напишите свое им или возразсть:')
// * if (+myName) {
// *     console.log(myName * myName)
// * }else {
// *     console.log('Hello', myName)
// * }

let age = +prompt('Введите ваш возрасть')
if (age >= 40) {
    console.log('ты стар')
}else if (age >=18) {
    console.log('доступ открыть')
}else if( age >= 1) {
    console.log('доступ закрыть')
}

// console.log('Hello', myName)
// console.log(+(myName **2))
// if (question==='3') {
//     console.log('Error')
// } else if (question===5) {
//     console.log('Success')
// }else {
//     console.log(null)
// }

// ! let myName='nurbek'
// ! console.log(+myName)    // ошибка
// ! console.log(myName.length+5)  // дабавляет