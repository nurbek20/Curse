// let person = {
//     fName: "Alex",
//     lName: "Merser",
//     age: 16,
//     family: [{
//         child1: "Bob",
//         child2: "Alex",
//         child3: "Rose"
//     },
// ],
//     weight: 60,
//     height: 170,
//     married: false,
//     'skin color': 'brown'
// }

// console.log(person.family[0].child1)
// console.log(person['skin color'])
// console.log(person.height)

// let i=0;
// while (i <= 50) {
//     console.log(i);
//     ++i;
//     // break
// }

// let i=50;
// while (i >= 0) {
//     console.log(i);
//     i--;
//     // break
// }
// while (true) {
//     let sName = "ahiles"
//     if (sName == prompt("Ты кто воин? ")) {
//         console.log("Hello", sName)
//         break
//     }
// }

// let ask = prompt('who r u')
// while (ask !== 'nurbek') {
//     ask = prompt('who r u')
// }
// if (ask === 'nurbek') {
//     console.log(`hello, ${ask}`);
// }


// let user = {
//     login: 'nurbek',
//     password: 1234,
//   }

//   let counter = 2

//   while (true) {
//     if (prompt("Логин") == user.login && prompt('Пароль') == user.password && counter > 0) {
//       console.log('Hello', user.login);
//       break
//     } else if (prompt('Пароль') != user.password && counter > 0 || prompt("Логин") != user.login && counter > 0) {
//       counter--
//       alert(`У вас осталось ${counter+1} попыток`)
//     } else if (counter <= 0) {
//       alert('Ваш аккаунт заблокирован')
//       break
//     }
//   }

let i = 3
let arr = {
    login: "admin",
    password: "1234"
}
let q = prompt("Login")
let pass = prompt("password")

while (i >= 1) {
    q = prompt("Ваш логин, у вас осталось: " + i + "попытка")
    pass = prompt("Ваш пароль, у вас осталос: " + i + "попытка")
    if (q === arr.login && pass === arr.password) {
        let x = prompt("Как тебя завут???")
        console.log("Hello" + x)
        break
    } else {
        if (i == 1) {
            console.log("Ваш аккаунт заблокирован")
        }
    }
    i--
}