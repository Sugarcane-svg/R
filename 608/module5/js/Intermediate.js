// method 1 title
const h3_1 = document.createElement('h3');
h3_1.innerHTML = 'SCOLL DOWN TO SEE MORE INFO';
document.body.appendChild(h3_1)

// create a div to store table
const table = document.createElement('div');
table.setAttribute('id', 'tableDiv');
document.body.appendChild(table);

// method 2 title
const h3_2 = document.createElement('h3');
h3_2.innerHTML = 'ENTER THE NAME OF PRESENT TO CHECK HIS INFO';
document.body.appendChild(h3_2);

// create input box
const input = document.createElement('input');
input.setAttribute('id', 'inputs');
input.setAttribute('placeholder', 'Caution: case sensitive');
input.style.cssText = 'margin-left:32%; width:500px; height: 30px; border: 1px solid #08282b;';
document.body.appendChild(input);

// create a button
const btn = document.createElement('button');
btn.innerHTML = 'Find!';
btn.setAttribute('id', 'btnFind');
btn.style.cssText = 'margin-left:20px;border:1px solid #08282b; color:white; background-color: #08282b;weight:40px; height: 30px;';
document.body.appendChild(btn);

// create p tag to show result
const p = document.createElement('p');
document.body.appendChild(p);






d3.csv('data/presidents.csv', function (rows) {

    // read table from csv file
    function unpack(rows, key) {
        return rows.map(function (row) {
            return row[key];
        });
    }

    let headerNames = d3.keys(rows[0]);
    let headerValues = [], cellValues = [];

    for (i = 0; i < headerNames.length; i++) {
        h = [headerNames[i]];
        headerValues[i] = h;
        c = unpack(rows, headerNames[i]);
        cellValues[i] = c;
    }


    let data = [{
        type: 'table',

        header: {
            values: headerValues,
            align: 'center',
            line: { width: 1, color: '#08282b' },
            font: { color: '#08282b' }
        },

        cells: {
            values: cellValues,
            align: 'center',
            line: { width: 1, color: '#08282b' },
            font: { color: '#08282b' }
        },
    }]

    let layout = {
        title: 'president height and weight'
    }

    Plotly.newPlot('tableDiv', data, layout);


    // get president name
    function getValue() {
        index = cellValues[0].indexOf(input.value);
        if (index == -1) {
            p.innerHTML = 'cannot find the name of president you entered';
        } else {
            p.innerHTML = 'name: ' + input.value + ' height: ' + cellValues[1][index] + ' weight: ' + cellValues[2][index];
        }
    }

    // get name to return his height and weight
    btn.addEventListener('click', getValue);

});