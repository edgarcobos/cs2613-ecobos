let merge_row=require("../merge-row.js").merge_row;

describe("merge_row",
    function () {
        it("id checks",
            function () {
                expect(merge_row({},{})).toEqual(null);
                expect(merge_row({id:0, name:"bob"},
                    {id:1, occupation: "builder"}))
                    .toEqual(null);
            });

        it("basic merge",
            function () {
                expect(merge_row({id:0, name:"bob"},
                    {id:0, occupation: "builder"}))
                    .toEqual({id:0, name:"bob",
                        occupation: "builder"});
            });
});