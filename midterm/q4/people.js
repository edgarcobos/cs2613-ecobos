class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

exports.Person = Person;

let fs = require("fs");

class People {
    constructor(filename) {
        let people = JSON.parse(fs.readFileSync(filename));
        for(let i in people) {
            this[people[i].Name] = new Person(people[i].Name, people[i].Died);
        }
    }
    length() {
        return this.length();
    }
}

exports.People = People;