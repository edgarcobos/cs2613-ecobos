revapp=require("../revapp.js").revapp;
describe("revapp", function () {
    it("letters", function () {
        expect(revapp("a","b","c","d")).toEqual("dcba");
    })});