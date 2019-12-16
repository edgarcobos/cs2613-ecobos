function revapp() {
    let arr = [];
    for(var i in arguments) {
        arr[i] = arguments[i];
    }
    arr = arr.reverse();
    return arr.reduce((acc, curr) => acc.concat(curr));
}

exports.revapp = revapp;