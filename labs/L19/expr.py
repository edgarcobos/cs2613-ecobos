from copy import deepcopy

class Expr:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return vars(self) == vars(other)
        else:
            return NotImplemented

    def eval(self):
        def recur(branch):
            if isinstance(branch, Expr):
                return branch.eval()
            else:
                return branch
        
        left = recur(self.left)
        right = recur(self.right)
        
        if self.op == '+':
            return left + right
        elif self.op == '*':
            return left * right

if __name__ == '__main__':
    six_plus_nine = Expr('+', 6, 9)
    print(six_plus_nine == deepcopy(six_plus_nine))