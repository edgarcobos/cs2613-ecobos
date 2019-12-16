let fs = require("fs");

class Student {
    constructor(name, id) {
        this.name = name;
        this.id = id;
    }
    write(filename) {
        fs.writeFileSync(filename,JSON.stringify(this));
    }
    read(filename) {
        let student = JSON.parse(fs.readFileSync(filename));
        return new Student(student.name, student.id);
    }
}

exports.Student = Student;