let read_json_file=require("./read_json_file.js").read_json_file;

let cache = {};
let data = null;

function by_name(name){
    if (data===null)
        data=read_json_file("big.json");
    if (cache[name] != undefined)
        return cache[name];
    // loop goes here
    for(let i in data) {
        if(data[i] === name) {
            return data[i];
        }
    }
    return null;
}

exports.by_name=by_name;
