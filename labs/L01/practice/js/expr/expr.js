class Expr {
    constructor(op, first, second) {
        this.op = op;
        this.first = first;
        this.second = second;
    }
    eval() {
        if(typeof(this.first) === "object" && typeof(this.second) === "object") {
            return (this.first).first * (this.first).second + (this.second).first + (this.second).second;
        }
        else if(this.op === "+") {
            return this.first + this.second;
        }
        else if(this.op === "*") {
            return this.first * this.second;
        }
    }
}

exports.Expr = Expr;