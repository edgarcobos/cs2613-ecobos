function plus(a,b) {
    if (a === 0) {
        return b;
    } else {
        return plus(a-1, b+1);
    }
}

function mult(a,b) {
    if (a===0) {
        return 0;
    } else {
        return plus(mult(a-1, b), b);
    }
}

exports.plus = plus;
exports.mult = mult;