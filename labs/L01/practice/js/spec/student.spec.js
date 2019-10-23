let Student = require("../student.js").Student;

describe("json", function () {
    let bob = new Student("bob",42);

    it("roundtrip", function() {
        let filename = "test-roundtrip.json";
        bob.write(filename);
        expect(bob.read(filename)).toEqual(bob);
    })});