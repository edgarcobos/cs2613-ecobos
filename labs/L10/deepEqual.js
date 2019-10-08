function deepEqual(x, y) {
    if(x === null && y === null) {
        return true;
    }
    if(x === null || y === null) {
        return false;
    }
    if(typeof(x) == "object" && typeof(y) == "object") {
        //let props = Object.keys(x);
        //for(let i = 0; i < props.length; i++) {
        //    if(!(props[i] in y) || !(deepEqual(x[props[i]], y[props[i]]))) {
        //        return false;
        //    }
        //}
        for(let prop in x) {
            if(!(prop in y) || !(deepEqual(x[prop], y[prop]))) {
                return false;
            }
        }
        return true;
    }
    else {
        return (x === y);
    }
}

exports.deepEqual = deepEqual;