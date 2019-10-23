join=require("../join.js").join;
describe("join", function () {
    it("empty", function () { expect(join([]), ""); });
    it("single", function () {
      expect(join(["holidays"]), "holidays");
    });
    it("several", function () {
      expect(join(["happy", " ", "holidays"]), "happy holidays");
    });
});