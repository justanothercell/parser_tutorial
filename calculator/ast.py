class AST:
    pass

class Value(AST):
    def __init__(self, value: int|float):
        self.value = value
    
    def eval(self, variables):
        return self.value

class Variable(AST):
    def __init__(self, name: str):
        self.name = name
    
    def eval(self, variables):
        return variables[self.name]

class FuncCall(AST):
    def __init__(self, name: str, args: list[AST]):
        self.name = name
        self.args = args
    
    def eval(self, variables):
        args = [arg.eval(variables) for arg in self.args]
        return variables[self.name](*args)

class BinaryOp(AST):
    def __init__(self, left: AST, right: AST, op: str):
        self.left = left
        self.right = right
        self.op = op
    
    def eval(self, variables):
        left = self.left.eval(variables)
        right = self.right.eval(variables)
        if self.op == '+':
            return left + right
        if self.op == '-':
            return left - right
        if self.op == '*':
            return left * right
        if self.op == '/':
            return left / right
        if self.op == '%':
            return left % right

class UnaryOp(AST):
    def __init__(self, item: AST, op: str):
        self.item = item
        self.op = op

    def eval(self, variables):
        item = self.item.eval(variables)
        if self.op == '+':
            return +item # redundant, but ey why not
        if self.op == '-':
            return -item