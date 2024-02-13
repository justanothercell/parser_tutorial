from .ast import *

def parse(text: str) -> AST:
    parser = Parser(text)
    ast = parser.parse_expression()
    if parser.has_current():
        raise ParseException('Still more to parse', parser)
    return ast

class ParseException(Exception):
    def __init__(self, message: str, parser: 'Parser'):
        self.message = message
        self.parser = parser

    def __str__(self):
        message = self.message
        text =  '| ' + self.parser.text
        arrow = '|-' + '-'*self.parser.index + '^'
        return f'{message}\n{text}\n{arrow}'

class Parser:
    def __init__(self, text: str):
        self.text = text
        self.index = 0
    
    def next(self):
        self.index += 1
        # let's skip the whitespaces - we do not have any need for those
        # and they just complicate parsing.
        while self.has_current() and self.current().isspace():
            self.index += 1

    def current(self) -> str:
        if not self.has_current():
            raise ParseException('Unexpected end of input', self)
        return self.text[self.index]

    def has_current(self) -> bool:
        return self.index < len(self.text)
    
    def parse_expression(self) -> AST:
        c = self.current()
        if c == '(':
            self.next() # skip opening bracket
            expr = self.parse_expression() # parse inner
            if self.current() != ')':
                raise ParseException('Expected closing bracket', self)
            self.next() # skip closing bracket
        elif c.isnumeric():
            expr = self.parse_value()
        elif c.isalpha() or c == '_':
            expr = self.parse_variable()
            if self.has_current() and self.current() == '(':
                # expr is a variable, so we can get the name, since we already parsed that.
                expr = self.parse_func_call(expr.name)
        elif c in '+-':
            expr = self.parse_unary_op()
        else:
            raise ParseException('Unimplemented!', self)
        if self.has_current() and self.current() in '+-*/%':
            op = self.current()
            self.next()
            expr = self.parse_binary_op(expr, op)
        return expr

    def parse_value(self) -> Value:
        value = ''
        while self.has_current() and self.current() in '0123456789_.':
            value += self.current()
            self.next()
        try:
            return Value(float(value))
        except ValueError: # not an int/float
            raise ParseException(f'Invalid number literal `{value}`', self)

    def parse_variable(self) -> Variable:
        variable = ''
        while self.has_current() and (self.current().isalnum() or self.current() == '_'):
            variable += self.current()
            self.next()
        return Variable(variable)

    def parse_func_call(self, name: str) -> FuncCall:
        self.next() # we know that's a opening bracket, skip!
        args = []
        while self.has_current():
            arg = self.parse_expression()
            args.append(arg)
            if self.current() not in ',)': # arguments should be comma separated
                raise ParseException('Function argument was not succeeded by comma or closing bracket', self)
            if self.current() == ')':
                self.next() # )
                return FuncCall(name, args)
            self.next() # ,        
        raise ParseException('Function call was not ended with closing bracket', self) 

    def parse_binary_op(self, left: AST, op: str) -> BinaryOp:
        right = self.parse_expression()
        return BinaryOp(left, right, op)

    def parse_unary_op(self) -> UnaryOp:
        op = self.current()
        self.next()
        item = self.parse_Expression()
        return UnaryOp(item, op)