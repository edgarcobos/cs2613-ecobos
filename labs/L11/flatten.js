function flatten(array) {
    return array.reduce((acc,cur) => acc.concat(cur), []);
}

exports.flatten = flatten;