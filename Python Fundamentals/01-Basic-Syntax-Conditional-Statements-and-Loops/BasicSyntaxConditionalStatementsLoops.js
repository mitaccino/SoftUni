/*
Basic Syntax, Conditional Statements and Loops
=================================
Lab
=================================
 */
// 01. Multiply Number by 2
function multiplyBy2(num) {
    let result = num * 2;
    console.log(result);
}

// 02. Excellent grade
function excellentGrade(grade) {
    if (grade >= 5.5) {
        console.log('Excellent');
    } else {
        console.log('Not excellent');
    }
}
// 03. Numbers from 1 to 5
function numbersFromOneToFive() {
    for (let i=1; i<=5; i++) {
        console.log(i);
    }
}
// 04. Numbers from N to 1
function numbersFromNToOne(num) {
    let i = num;
    while (i >= 1) {
        console.log(i);
        i--;
    }
}
// 05. Numbers from M to N
function numbersFromMtoN(m, n) {
    for (let i = m; i >= n; i--) {
        console.log(i);
    }
}
// 06. Student Information
function studentInfo(name, age, grade) {
    console.log(`Name: ${name}, Age: ${age}, Grade: ${grade.toFixed(2)}`);
}
// 07. Month Printer
function monthPrinter(num) {
    switch (0 < num <= 12) {
        case num === 1:
            console.log('January');
            break;
        case num === 2:
            console.log('February');
            break;
        case num === 3:
            console.log('March');
            break;
        case num === 4:
            console.log('April');
            break;
        case num === 5:
            console.log('May');
            break;
        case num === 6:
            console.log('June');
            break;
        case num === 7:
            console.log('July');
            break;
        case num === 8:
            console.log('August');
            break;
        case num === 9:
            console.log('September');
            break;
        case num === 10:
            console.log('October');
            break;
        case num === 11:
            console.log('November');
            break;
        case num === 12:
            console.log('December');
            break;
        default:
            console.log('Error!')

    }
}
// 08. Foreign Languages
function foreignLanguages(language) {
    switch (language) {
        case 'USA':
        case 'England':
            console.log('English');
            break;
        case 'Spain':
        case 'Argentina':
        case 'Mexico':
            console.log('Spanish');
            break;
        default:
            console.log('unknown');

    }
}
// 09. Theatre Promotions