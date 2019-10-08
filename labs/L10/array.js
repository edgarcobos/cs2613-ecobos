/*function range(start, end) {
    let range = end - start;
    let array = [];
    for(let i = 0; i <= range; i++) {
        array[i] = start + i;
    }
    return array;
}*/

function sum(array) {
    let sum = 0;
    for(let i = 0; i < array.length; i++) {
        sum += array[i];
    }
    return sum;
}

function range(start, end, step = 1) {
    let array = [];
    if(step < 0) {
        for(let i = start; i >= end; i+=step) {
            array.push(i);
        }
    }
    else {
        for(let i = start; i <= end; i+=step) {
            array.push(i);
        }
    }
    return array;
}

exports.range = range;
exports.sum = sum;