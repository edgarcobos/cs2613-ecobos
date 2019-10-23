function no_dups(obj1, obj2) {
    var res = {};
    if(typeof(obj1) === typeof(obj2)) {
        if(obj1.id === obj2.id && typeof(obj1.id) === "number") {
            for(let key in obj1){
                //if(key !== undefined) {
                    res[key] = obj1[key];
                //}
                /*else {
                    res[key] = obj2[key];
                }*/
            }
            for(let key in obj2) {
                //if(key !== undefined) {
                    res[key] = obj2[key];
                //}
                /*else {
                    res[key] = obj1[key];
                }*/
            }
            return res;
        }
        else {
            return null;
        }
    }
}

exports.no_dups = no_dups;