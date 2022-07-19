// const people = [{
//     name: 'Asan',
//     age: 29,
//     gender: 'male'
// },
// {
//     name: 'Anna',
//     age: 20,
//     gender: 'female'
// },
// {
//     name: 'Uson',
//     age: 40,
//     gender: 'male'
// },
// {
//     name: 'Selena',
//     age: 12,
//     gender: 'female'
// },
// {
//     name: 'Esen',
//     age: 60,
//     gender: 'male'
// },
// {
//     name: 'Alice',
//     age: 84,
//     gender: 'female'
// },
// ];
// console.log(people.filter(el=>el.age==40));
// console.log(people.indexOf(age));
// let user =people.filter(item=>item.age==84)
// let userr =people.filter(item=>item.age==60)
// let user1 =people.filter(item=>item.gender=='female')
// let user2 =people.filter(item=>item.gender=='male')

// console.log(`кол-во Женшин ${user1.length}`);
// console.log(`кол-во Мужчин ${user2.length}`);
// console.log(`самый старший из женщин ${user.length} года`);
// console.log(`самый старший из мужчин ${user.length} года`);
// let m = 0;
// let f = 0;
// let mMax = 0;
// let fMax = 0;
// for (let i = 0; i < people.length; i++) {
//     if (people[i].gender == 'male') {
//         // m = people.filter(item=> item.gender=='male')
//         m++
//         mMax = people[i].age   
//     }else if (people[i].gender == 'female') {
//         fMax = people[i].age
//         // f = people.filter(item=> item.gender=='male')
//         f++
//     }
// }
// console.log(`кол-во Мужчин ${m.length}`);
// console.log(`кол-во Женшин ${f.length}`);
// console.log(`кол-во Мужчин ${m}`);
// console.log(`кол-во Женшин ${f}`);
// console.log(`самый старший из мужчин ${mMax} года`);
// console.log(`самый старший из мужчин ${fMax} года`);

// let y = people.filter((hourse) => {
//     return hourse.age <= 40
// })
// console.log(y);

// people.sort();
// console.log(people);
// people.reverse();
// console.log(people);
// for (let i=0; i>people.length; i++) {
//     console.log(people[i]);
// }

// * стилы для HTML
// let text = document.getElementsByClassName('h1');
// let box = document.getElementsByClassName('box');
// let bd = document.body
// bd.style.height='100vh'
// bd.style.backgroundColor='green'
// bd.style.display='flex'
// bd.style.justifyContent='center'
// bd.style.alignItems='center'
// box[0].style.display='flex'
// box[0].style.justifyContent='center'
// box[0].style.alignItems='center'
// box[0].style.width='300px'
// box[0].style.height='300px'
// box[0].style.border='2px solid white'
// box[0].style.backgroundColor='red'
// text[0].style.color='red'
// console.log(text);

// ? events = события
// ? createElement - appendChild = Прочитат

// ! hw bankomat 
// let admins = [{                                 
//     name: 'asan',
//     age: 24,
//     balans: 20000,
//     user: 123
// },
// {
//     name: 'uson',
//     age: 24,
//     balans: 14000,
//     user: 1234
// },
// {
//     name: 'esen',
//     age: 27,
//     balans: 6000,
//     user: 12345
// }
// ];
// while (true) {
//     let n = prompt('Ведите логин:')
//     for (let i = 0; i < admins.length; i++) {
//         if (admins[i].name == n) {
//             alert(`Дабро пожаловать ${admins[i].name.toLocaleUpperCase().slice(0,1)+admins[i].name.slice(1)}`)
//             n = prompt(`Введите свой пароль цифрами`)
//             if (n == admins[i].user) {
//                 n = prompt(`${admins[i].name.toLocaleUpperCase().slice(0,1)+admins[i].name.slice(1)} Если хотите узнать свой баланс введите 1\nЕсли хотите снят баланс введите 2`)
//                 if (n == 1) {
//                     alert(`Ваш текушего баланс ${admins[i].balans} сом`);
//                 } else if (n == 2) {
//                     n = prompt(`Сколько вы хотите снят баланс`)
//                     if (n < admins[i].balans) {
//                         alert(`${admins[i].name.toLocaleUpperCase().slice(0,1)+admins[i].name.slice(1)}\nВаш баланс ${admins[i].balans} сом\nВы сняли ${n} сом \n${n} - ${admins[i].balans} \nостаток вашего баланса ${admins[i].balans - n} сом`)
                        // * console.log(admins[i].name.toLocaleUpperCase().slice(0,1)+admins[i].name.slice(1));
                        // * console.log(`Ваш баланс ${admins[i].balans} сом`);
                        // * console.log(`Вы сняли ${n} сом`);
                        // * console.log(`${n} - ${admins[i].balans}`);
                        // * console.log(`остаток вашего баланса ${admins[i].balans - n} сом`);
//                     } else {
//                         alert('У вас не достаточно средство')
//                     }
//                 }
//             } else {
//                 alert(`Вы написали не верный пароль`);
//             }
//         }
//     } n = prompt(`Для выхода введите 1 Хотите продолжить нажмите enter`)
//     if (n == 1) {
//         break
//     }
// }


// let text = document.getElementsByClassName('h3')
// for (let i = 0; i < text.length; i++) {
//     text[i].style.color = 'red';
//     text[i].style.backgroundColor = 'yellow';
//     text[i].style.fontSize = '30px';
//     text[i].style.border = '5px solid red';
//     text[i].style.textTransform = 'uppercase';
//     text[i].style.borderRadius = '20px'
//     text[i].style.textAlign = 'center'
// }
// let text1 = document.getElementsByClassName('h3')[1]
// let text2 = document.getElementsByClassName('h3')[2]
// let text3 = document.getElementsByClassName('h3')[3]
// let text4 = document.getElementsByClassName('h3')[4]
// let ts= text.style
// ts.color='red'
// ts.width='100px'
// ts.height='100px'
// ts.backgroundColor='aqua'
// let ts1 = text1.style
// ts1.color='red'
// ts1.width='100px'
// ts1.height='100px'
// ts1.backgroundColor='aqua'
// let ts2 = text2.style
// ts2.color='red'
// ts2.width='100px'
// ts2.height='100px'
// ts2.backgroundColor='aqua'
// text1.style.color='red'
// text2.style.color='red'
// text3.style.color='red'
// text4.style.color='red'
