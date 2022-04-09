document.body.style.cssText = 'height: 100vh';

// create title
const title = document.createElement('h3');
title.innerHTML = 'REVERSE WORD';
title.style.cssText = 'text-align: center; margin-top: 5%;overflow:hidden; color:#098f9c;';
document.body.appendChild(title);

// create text box
const input = document.createElement('input');
input.setAttribute('type', 'text');
input.setAttribute('id', 'inputs');
input.setAttribute('placeholder', 'type a word you want to reverse');
input.style.cssText = 'width: 40%; height: 30px;font-size: 15px;margin-left: 25%;margin-top:1%;border:1px solid;';
document.body.appendChild(input);

// create a button
const reverse = document.createElement('button');
reverse.innerHTML = 'REVERSE!';
reverse.style.cssText = 'margin-left:10px;background-color:#098f9c; border:1px solid #098f9c; color:white;height: 30px; width: 80px;';
document.body.appendChild(reverse);

// create function to reverse words
function reverse_word(str) {
    let s = '';
    for (let i = str.length - 1; i >= 0; i--) {
        s += str[i];
    }
    return s;
}

// create p tag
const reversed_result = document.createElement('p');
reversed_result.setAttribute('id', 'resersed_result');
reversed_result.style.cssText = 'text-align: center;font - weight: bold; margin-top:10px;';
document.body.appendChild(reversed_result);

// click event
function myclick() {
    if (input.value == '') {
        reversed_result.textContent = 'you need to enter a least a word :)';
    } else {
        reversed_result.textContent = reverse_word(input.value);
    }
}

reverse.addEventListener('click', myclick);


//line break
document.body.appendChild(document.createElement('br'));

// create title for 20 multiples
const title2 = document.createElement('h3');
title2.innerHTML = '20 MULTIPLES';
title2.style.cssText = 'text-align:center;margin-top:5%;color:#098f9c;';
document.body.appendChild(title2);

// create input box
const input2 = document.createElement('input');
input2.style.cssText = 'width: 40%; height: 30px;font-size: 15px;margin-left: 25%;margin-top:1%;margin-bottom:1%;border:1px solid';
input2.setAttribute('placeholder', 'enter a number');
document.body.appendChild(input2);

// create button
const calculate = document.createElement('button');
calculate.innerHTML = 'SHOW!';
calculate.style.cssText = 'margin-left:10px;background-color:#098f9c; border:1px solid #098f9c; color:white;height:30px; width: 80px;';
document.body.appendChild(calculate);

//create a table
const table = document.createElement('table');
table.style.cssText = 'margin-left:20%;width:60%;border:1px solid #098f9c; margin-top:10px;';

// create 5x4 table

for (let i = 0; i < 5; i++) {
    const tr = document.createElement('tr');
    tr.style.cssText = 'text-align:center;border:1px solid #098f9c;';
    table.appendChild(tr);

    for (let j = 0; j < 4; j++) {
        const td = document.createElement('td');
        td.style.cssText = 'text-align:center;border:1px solid #098f9c; color:white;'
        td.setAttribute('class', 'tds')
        tr.appendChild(td);
    }
}
document.body.appendChild(table);



function cal_multiples() {
    n = parseInt(input2.value);
    if (!Number.isInteger(n)) {
        window.alert('you need to enter an integer');
    } else {

        let collection = document.getElementsByClassName('tds');
        let m = 1;
        for (let i = 0; i < collection.length; i++) {
            collection[i].innerHTML = n * m;
            m++;
        }
    }
}

// function create_table() {

//     let n = input2.value;
//     if (!parseInt(n)) {
//         const warn = document.createElement('p');
//         warn.style.cssText = 'text-align:center;';
//         document.body.appendChild(warn);
//         warn.innerHTML = 'you must enter a number :)';
//     } else {
//         x = parseInt(n);
//         let m = 1;
//         for (let i = 0; i < 5; i++) {
//             const tr = document.createElement('tr');
//             tr.style.cssText = 'text-align:center;border:1px solid;';
//             table.appendChild(tr);
//             for (let j = 0; j < 4; j++) {
//                 const td = document.createElement('td');
//                 td.style.cssText = 'text-align:center;border:1px solid;'
//                 tr.appendChild(td);
//                 td.innerHTML = x * m;
//                 m++;
//             }
//         }
//         document.body.appendChild(table);
//     }

// }

calculate.addEventListener('click', cal_multiples);