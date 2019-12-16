let Student = require("../student.js").Student;

describe("json", function () {
    let bob = new Student("bob",42);
    let dylan = new Student("dylan",1)

    it("roundtrip", function() {
        let filename = "test-roundtrip.json";
        bob.write(filename);
        expect(dylan.read(filename)).toEqual(bob);
    })});