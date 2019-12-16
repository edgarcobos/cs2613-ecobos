class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    birthday() {
        return new Person(this.name, this.age + 1);
    }
}

exports.Person = Person;

let fs = require("fs");

class People {
    constructor(filename) {
        let people = JSON.parse(fs.readFileSync(filename));
        this.length = people.length;
        /*for(var i = 0; i < people.length; i++) {
            this[people[i].name] = new Person(people[i].name, people[i].died - people[i].born + 1);
        }*/
        people.forEach(person => {
            this[person.name] = new Person(person.name, person.died - person.born + 1);
        });
    }
}

exports.People = People;