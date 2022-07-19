//  *  Методды массивы
// let asd=()=> {}  стрелочный функция
// let arr = ["A", "B", "C", "D"]
// let arr1 = [1, 2, 4, 5, 6, 9, 7, 10, 3];
// arr.forEach((asd)=>{
//     console.log(asd);
// })
// for (let i=0; i<arr.length; i++){
//     console.log(arr[i])
// }
// console.log(arr.indexOf('G'));
// let arr = [
//     {
//         id: 1,
//         name: "Вася",
//         isMarried: false
//     },
//     {
//         id: 2,
//         name: "Петя",
//         isMarried: true
//     },
//     {
//         id: 3,
//         name: "Саня",
//         isMarried: false
//     }
// ];
// let x = arr.filter((hourse) => {
//     return hourse.isMarried == true
// })
// console.log(x);
// let arr = [1, 2];
// создать массив из: arr и [3,4]
// alert(arr.concat([3, 4])); // 1,2,3,4
// создать массив из: arr и [3,4] и [5,6]
// alert(arr.concat([3, 4], [5, 6])); // 1,2,3,4,5,6
// создать массив из: arr и [3,4], потом добавить значения 5 и 6
// alert(arr.concat([3, 4], 5, 6)); //
// map() Это функция считаеть вес список массива 
// arr.map((item) => {
//     console.log(item);
// })

// arr1.sort()                       // * Вызов arr1.sort() сортирует массив на месте, меняя в нём порядок элементов.
// console.log(arr1); 
// arr1.reverse();                   // * Метод arr.reverse меняет порядок элементов в arr на обратный.
// console.log(arr1)


// let names = 'Вася, Петя, Маша';  
// let x = names.split(',')                // * возврашаеть массив
// let q = [ "Вася"," Петя"," Маша" ]
// console.log(x)
// console.log(names);

// console.log(q.join(''))                // * вазврашаеть строку

// * DOM = Document Object Model   Это связка Html and Css
// ? например 
// * document.body.style.backgrauondColor='red'

// * Обычный фнукция
// function pokupka (){
//     console.log('Milk')
//     console.log('Potato')
//     console.log('Butter')
//     console.log('Bread')
//     console.log('Sugar')
//     console.log('Tomato')
//     console.log('Rice')
//     console.log('-----------------------')
// }
// pokupka()

// * Стрелочный функция
// let pokupka =()=>{
//     console.log('Milk')
//     console.log('Potato')
//     console.log('Butter')
//     console.log('Bread')
//     console.log('Sugar')
//     console.log('Tomato')
//     console.log('Rice')
//     console.log('-----------------------')
// }
// pokupka()

// let colors = ['green', 'red', 'blue', 'yellow', 'skyblue', 'pink', 'black', 'orange', 'white', 'gold', 'teal']
// let i =0
// setInterval(() => {
//     document.body.style.backgroundColor = colors[i]
//     i++
//     if (i >= 12){
//         i=0
//     }
//     console.log(i);
// }, 1000);

// let i =11
// setInterval(() => {
//     document.body.style.backgroundColor = colors[i]
//     i--
//     if (i ==0){
//         i=10
//     }
//     console.log(i);
// }, 1000);