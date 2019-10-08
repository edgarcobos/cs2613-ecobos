function makemap () {
    let map = {};
    if(arguments.length %2 != 0)
        return map;
        
    for(let i=0; i<arguments.length; i+=2) {
        map[arguments[i]]=arguments[i+1];
    }

    return map;

}

console.log(makemap("x",1,"y",2,"z",3));

function brag(name,...args){
    console.log(name + " has");
    for (let i=0; i<args.length; i++) {
        console.log("\t"+args[i]);
    }
}

brag("attila", "throne of gold", "nice horse", "inlayed bow");

function win(person,thing="a brick"){
    console.log(person + " won " + thing);
}

console.log(win("nick"));
console.log(win("oprah","car"));