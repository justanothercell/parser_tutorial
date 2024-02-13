# AST Nodes Parsing

[Back: Parser Implementation](implementation.md) | [Chapters](../README.md#Chapters) | [Next: Evaluation](evaluation.md)

---

Parsing the individual nodes is easy. Just figure out _where exactly_ we are, what we need to check and which
other parsing methods we need to call. Feel free to implement any of those yourself as an exercise.

It is important that the parser points to the index just after the end of the thing we are parsing once we are done.
We also need to make sure to not call `self.current()` if we are past the end of the input. We should also make sure
that a `ParseException` is the only exception which can be thrown.

<details>
<summary>parse_value</summary>

```py
class Parser:
    ...
    def parse_value(self) -> Value:
        value = ''
        while self.has_current() and self.current() in '0123456789_.':
            value += self.current()
            self.next()
        try:
            return Value(float(value))
        except ValueError: # not an int/float
            raise ParseException(f'Invalid number literal `{value}`', self)

```
</details>

<details>
<summary>parse_variable</summary>

```py
class Parser:
    ...
    def parse_variable(self) -> Variable:
        variable = ''
        while self.has_current() and (self.current().isalnum() or self.current() == '_'):
            variable += self.current()
            self.next()
        return Variable(variable)
```
</details>

<details>
<summary>parse_func_call</summary>

```py
class Parser:
    ...
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
```
</details>

Let's not implement any operator precedence for binary operations yet, let's get this working first:

<details>
<summary>parse_binary_op</summary>

```py
class Parser:
    ...
    def parse_binary_op(self, left: AST, op: str) -> BinaryOp:
        right = self.parse_expression()
        # TODO: check precedence
        return BinaryOp(left, right, op)
```
</details>

<details>
<summary>parse_unary_op</summary>

```py
class Parser:
    ...
    def parse_unary_op(self) -> UnaryOp:
        op = self.current()
        self.next()
        item = self.parse_Expression()
        return UnaryOp(item, op)
```
</details>

If we now [run](../main.py) the program we get...
```
    result = ast.eval(variables, functions)
             ^^^^^^^^
AttributeError: 'FuncCall' object has no attribute 'eval'
```
Yes! All the parsing steps are now implemented and only the evaluation is missing. Let's quickly fix the operator precedence and then get going with that.

Currently, the way parsing is set up, binary operators are grouped right to left:<br>
`BinaryOp(a, BinaryOp(b, BinaryOp(c, ..., "+"), "+"), "+")`<br>
We now _only_ want this to be the case if the right binary operator is strictly higher in precedence than the left one,
which means we now have to check:
- whether the right value even is a binary operator
- whether it is equal or less in precedence

If both conditions are true we swap them.

<details>
<summary>parse_binary_op</summary>

```py
class Parser:
    ...
    def parse_binary_op(self, left: AST, op: str) -> BinaryOp:
        right = self.parse_expression()
        # TODO: check precedence
        if isinstance(right, BinaryOp):
            if right.op in '*/%' and op in "+-" # right is strictly higher binding than left
                return BinaryOp(left, right, op)
            # otherwise, we switch to have left-to-right evaluation
            BinaryOp(BinaryOp(left, right.left, op), right.right, right.op)
        return BinaryOp(left, right, op)
```
</details>

Now we are truly done and can evaluate the AST.

---

[Back: Parser Implementation](implementation.md) | [Chapters](../README.md#Chapters) | [Next: Evaluation](evaluation.md)


    