function revapp() {
    let array = [];
    for(var i = arguments.length-1, j = 0; i >= 0; i--, j++) {
        array[j] = arguments[i];
    }
    return array.reduce((acc,cur) => acc.concat(cur), "");
}

exports.revapp = revapp;