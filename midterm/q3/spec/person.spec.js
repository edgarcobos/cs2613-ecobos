let Person = require("../person.js").Person;

describe("person",
    function () {
        let bob=new Person("bob", 42);
        it("constructor",
            function () {
                expect(bob.name).toEqual("bob");
                expect(bob.age).toEqual(42);
            });

        it("birthday does not mutate",
            function (){
                let newbob = bob.birthday();

                expect(bob.age).toEqual(42);
                expect(newbob.age).toEqual(43);
            });
             
    });