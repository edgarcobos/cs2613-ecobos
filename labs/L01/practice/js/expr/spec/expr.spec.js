let Expr=require("../expr.js").Expr;

describe("expr",
         function() {
             let six_plus_nine = new Expr('+', 6, 9);
             let six_times_nine = new Expr('*', 6, 9);
             it("addition",
                function() {
                    expect(six_plus_nine.eval()).toBe(15);
                });
             it("multiplication",
                function() {
                    expect(six_times_nine.eval()).toBe(54);
                });
             it("compound",
                function() {
                    expect(new Expr('+', six_times_nine,
                                    six_plus_nine).eval()).toBe(69);
                });});