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

//applies flatten to json file with mailing list and returns a list of mails with the specified properties
function summarize_mail(filename) {
    let data = flatten(read_json_file(filename));
    let lst = [];
    if(arguments.length < 2) {
        for(let i in data) {
            lst[i] = {};
        }
        return lst;
    }
    let curr;
    for(let j in data) {
        curr = {};
        for(var k = 1; k < arguments.length; k++) {
            curr[arguments[k]] = data[j].headers[arguments[k]];
        }
        lst[j] = curr;
    }
    return lst;
}

exports.summarize_mail = summarize_mail;


