let deepEqual = require("../deepEqual.js").deepEqual;

describe("equal", function () {
    let obj = {here: {is: "an"}, object: 2};
    it("self", function () {
        expect(deepEqual(obj,obj)).toBe(true);
    });
    it("null", function () {
        expect(deepEqual(null,null)).toBe(true);
    });
    it("one null", function () {
        expect(deepEqual(null,{key: 1})).toBe(false);
    });
    it("different", function () {
        expect(deepEqual(obj, {here: 1, object: 2})).toBe(false);
    });
    it("more keys in A", function () {
        expect(deepEqual(obj, {x: 1, y: 2, z: 3}, {x: 1, y: 2})).toBe(false);
    });
    it("equivalent", function () {
        expect(deepEqual(obj, {here: {is: "an"}, object: 2})).toBe(true);
    });
});