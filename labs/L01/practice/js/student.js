let fs = require("fs");

class Student {
    constructor(name, id) {
        this.name = name;
        this.id = id;
    }
    read(filename) {
        return JSON.parse(fs.readFileSync(filename));
    }
    write(filename) {
        fs.writeFileSync(filename,JSON.stringify(this));
    }
}

exports.Student = Student;