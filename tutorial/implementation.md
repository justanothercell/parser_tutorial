# Chapter 4: Parser Implementation

[Back: Parser Layout](parser.md) | [Chapters](../README.md#Chapters) | [Next: AST Nodes Parsing](nodes.md)

---

Parsing starts in `parse_expression`. From there we need to figure out which 
kind of AST node comes next in out input.
Let's gather some indicators by which we could differentiate them.

| Class (extending AST) | Indicator                                        |
|-----------------------|--------------------------------------------------|
| Value                 | starts with numeric digit                        |
| Variable              | starts with alphabetic digit or underscore       |
| FuncCall              | starts with variable, differentiation later!     |
| BinaryOp              | starts with any AST node, differentiation later! |
| UnaryOp               | starts with operator (+/-)                       |

While there is no AST node for bracketed expressions, we still need to parse it, so we also need to check for `(`.

Now that we more or less know what we are dealing with, 
we can switch to the correct node parser function accordingly.

<details>
<summary>Parser</summary>

```py
class Parser:
    ...
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
            # TODO: check for function call
        elif c in '+-':
            expr = self.parse_unary_op()
        else:
            raise ParseException('Unimplemented!', self)
        # TODO: check for binary op
        return expr
```
</details>

Now we can address the two nodes which we could not detect immediately.

### FuncCall

If the variable name is followed by `(`, its a function call. If not, its just a variable.

<details>
<summary>parse_func_call</summary>

```py
class Parser:
    ...
    def parse_expression(self) -> AST:
        ...
        elif c.isalpha() or c == '_':
            expr = self.parse_variable()
            # TODO: check for function call
            if self.has_current() and self.current() == '(':
                # expr is a variable, so we can get the name, since we already parsed that.
                expr = self.parse_func_call(expr.name)
        ...
    ...
    # this also means we need to adjust the signature here
    def parse_func_call(self, name: str) -> FuncCall:
        raise ParseException('Unimplemented!', self)
```
</details>

### BinaryOp

The binary operator is similar. If the current expression is followed by an operator, 
we parse it and immediately parse the next expression afterwards as the righhand value.

<details>
<summary>parse_binary_op</summary>

```py
class Parser:
    ...
    def parse_expression(self) -> AST:
        else:
            raise ParseException('Unimplemented!', self)
        # TODO: check for binary op
        if self.has_current() and self.current() in '+-*/%':
            op = self.current()
            self.next()
            expr = self.parse_binary_op(expr, op)
        return expr
    ...
    # this again means we need to adjust the signature here
    def parse_binary_op(self, left: AST, op: str) -> BinaryOp:
        raise ParseException('Unimplemented!', self)
```
</details>

And with that we already did most of the hard work!
All that is left to do now that we have the branching (for parsing at least) is implemented,
is coding all the more or less linear functions which implement the nodes.

---

[Back: Parser Layout](parser.md) | [Chapters](../README.md#Chapters) | [Next: AST Nodes Parsing](nodes.md)