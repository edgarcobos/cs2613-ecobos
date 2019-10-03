var arith=require ("../loop-arith.js");
var arith2=require ("../loop-arith2.js");

describe("add",
    function() {
    it("1 + 1 = 2",
        function() {
            expect(arith.plus(1,1)).toBe(arith2.plus(1,1));
        });
    it("0 + x = x",
        function() {
            expect(arith.plus(0,1234567)).toBe(arith2.plus(0,1234567));
        });
    });

describe("mult",
    function() {
        it("0 * 2 = 0",
            function() {
                expect(arith.mult(0,2)).toBe(arith2.mult(0,2));
            });
        it("1 * 2 = 2",
            function() {
                expect(arith.mult(1,2)).toBe(arith2.mult(1,2));
            });
        it("2 * 2 = 4",
            function() {
                expect(arith.mult(2,2)).toBe(arith2.mult(2,2));
            });
    });