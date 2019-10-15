let by_name=require("./by_name.js").by_name;
let names=require("./read_all.js").names;
let shuffle=require("./shuffle.js").shuffle;

let reps = 3;

for (let i=0; i< reps; i++){
    shuffle (names);
    for (let j=0; j<names.length; j++) {
        let test_name=i+","+j;
        console.time(test_name);
        let dummy=by_name(names[i]);
        console.timeEnd(test_name);
    }
}