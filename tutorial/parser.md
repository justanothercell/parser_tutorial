# Chapter 3: Parser Layout

[Back: Structure&AST](structure.md) | [Chapters](../README.md#Chapters) | [Next: Parser Implementation](implementation.md)

---

Let's first define a parser structure, which helps us traverse the input, skipping whitespaces, aswell as generating a helpful error message
if we unexpectedly reach the end of input.


<details>
<summary>Parser</summary>

```py
class Parser:
    def __init__(self, text: str):
        self.text = text # the input text expression
        self.index = 0   # the index we are currently at
    
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

    # are we still in range?
    def has_current(self) -> bool:
        return self.index >= len(self.text)
```
</details>

We can now iterate over the input like this:
<details>
    <summary>Example</summary>

```py
from calculator.parser import Parser

parser = Parser('sin(pi * x + 4)')
out = ''
while parser.has_current():
    out += parser.current()
    parser.next()
print(out)
```
```
sin(pi+4)*x
```
</details>

We can also define an exception class to inform the user about syntax errors

<details>
<summary>ParseException</summary>

```py
class ParseException:
    def __init__(self, message: str, parser: 'Parser'):
        self.message = message
        # passing along the source will give us helpful metadata 
        # to format our exception (a task for later)
        self.parser = parser

    def __str__(self):
        return f'ParseException: {self.message}'
```
</details>

Our parser needs a parsing method for each AST node, aswell as a generic `parse_expression` node to switch between the node types.

<details>
<summary>Parser</summary>

```py
class Parser:
    ...
    def parse_expression(self) -> AST:
        raise ParseException('Unimplemented!', self)

    def parse_value(self) -> Value:
        raise ParseException('Unimplemented!', self)

    def parse_variable(self) -> Variable:
        raise ParseException('Unimplemented!', self)

    def parse_func_call(self) -> FuncCall:
        raise ParseException('Unimplemented!', self)

    def parse_binary_op(self) -> BinaryOp:
        raise ParseException('Unimplemented!', self)

    def parse_unary_op(self) -> UnaryOp:
        raise ParseException('Unimplemented!', self)
```
</details>

And finally with all that we can define the parsing entrypoint

<details>
<summary>parse</summary>

```py
def parse(text: str) -> AST:
    parser = Parser(text)
    ast = parser.parse_expression()
    if parser.has_more():
        raise ParseException('Still more to parse', parser)
    return ast
```
</details>

Now we can finally [run](../main.py) the parser.<br>
It, of course, fails immediately:<br>
```py
calculator.parser.ParseException: Unimplemented!
```

An immediate problem that we can see is that we dont know *where* we failed. This makes debugging, both when coding and using the parser very difficult.

Luckily, our exception class knows where we are since we give it our `Parser` object on construction.<br>
This makes it easy to adjust the `__str__` method.

<details>
<summary>ParseException</summary>

```py
class ParseException(Exception):
    ...
    def __str__(self):
        message = self.message
        text =  '| ' +self.parser.text
        arrow = '|-' + '-'*self.parser.index + '^'
        return f'{message}\n{text}\n{arrow}'
```
</details>

We now show the source text aswell as an arrow to the specific location where the error occured.

```py
calculator.parser.ParseException: Unimplemented!
| sin(pi * x + 4)
|-^
```

This is much better! Now we can actually implement the parsing.

---

[Back: Structure&AST](structure.md) | [Chapters](../README.md#Chapters) | [Next: Parser Implementation](implementation.md)