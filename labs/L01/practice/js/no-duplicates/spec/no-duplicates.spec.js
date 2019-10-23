
let no_dups=require("../no-duplicates.js").no_dups;

describe("merge ",
    function () {
        it("id checks",
            function () {
                expect(no_dups({},{})).toEqual(null);
                expect(no_dups({id:0, name:"bob"},
                    {id:1, occupation: "builder"}))
                    .toEqual(null);
            });

        it("basic merge",
            function () {
                expect(no_dups({id:0, name:"bob"},
                    {id:0, occupation: "builder"}))
                    .toEqual({id:0, name:"bob",
                        occupation: "builder"});
            });
        
        it("no_dups",
            function () {
                expect(no_dups({id:0, name:"bob", favColor: "red"},
                    {id:0, occupation: "builder", favColor: "red"}))
                    .toEqual({id:0, name:"bob",
                        occupation: "builder", favColor: "red"});
            });    
});