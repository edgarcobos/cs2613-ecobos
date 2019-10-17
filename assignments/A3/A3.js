//recursively “flattens” an array of arrays into a single array
function flatten(arr) {
    return arr.reduce((acc, curr) => acc.concat(((Array.isArray(curr))? flatten(curr) : curr)), []);
}

exports.flatten = flatten;

let fs = require('fs');

function read_json_file(filename) {
    let contents = fs.readFileSync(filename);

    return JSON.parse(contents);
}

exports.read_json_file=read_json_file;


