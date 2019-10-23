function animate(iterations) {
    let i=0;
    let str="";
    let timer = null;
    function frame() {
        // add code here
        i++;
        str += "*";
        console.log('\033c');
        console.log(str);
        if (i>=iterations) {
            // and here
            console.log("all done");
            clearInterval(timer);
        }
    }
    timer=setInterval(frame,300);
}

animate(20);