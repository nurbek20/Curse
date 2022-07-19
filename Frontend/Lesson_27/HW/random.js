// let number =Math.ceil( Math.random() * 100);
// alert(number);

// let sName = prompt('Привет как тебя завут? ');
// while (sName == '' || sName == null) {
//     sName = prompt('Привет как тебя завут?')
// }
// alert(sName + ', я загадал число от 1 до 100. Попробуй отгадать его за наименьшее количество попыток. После каждой попытки я скажу "мало", "много" или "угадал".');
// let number = Math.ceil( Math.random() * 100);
// let q = prompt('какое число я загадал? ');
// let numberOFGuesses = 0;
// while (q != number) {
//     if (q > number) {
//         q = prompt('Много. Попробуй еще раз');
//         numberOFGuesses = numberOFGuesses + 1;
//     }
//     if (q < number) {
//         q = prompt('Мало. Попробуй еще раз');
//         numberOFGuesses = numberOFGuesses + 1;
//     }
// }
// alert('Ты угудал! Это число ' + number + '. Тебе понадобилось ' + numberOFGuesses + ' Попыток.')

let btn = document.querySelector('.btn');

btn.addEventListener('click', () => {
    let number1 = Math.ceil(Math.random() * 6);
    let number2 = Math.ceil(Math.random() * 6);
    let img = './images/dice' + number1 + '.png'
    let img1 = './images/dice' + number2 + '.png'
    let diec1 = document.querySelector('.img__dice1');
    let diec2 = document.querySelector('.img__dice2');
    let h1 = document.querySelector('h1')
    diec1.src = img
    diec2.src = img1
    if (number1 == number2) {
        h1.innerHTML = 'ничья'
    } else if (number1 > number2) {
        h1.innerHTML = 'Первый игрок выйграл'
    } else {
        h1.innerHTML = 'Второй игрок выйграл'
    }
})