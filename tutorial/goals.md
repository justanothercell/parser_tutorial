# Chapter 1: Goals

[Chapters](../README.md#Chapters) | [Next: Structure&AST](structure.md)

---

## Goals
The parser should be able to:
- parse bracketed expressions
- call functions
- use binary operators (with correct precedence)
- use unary operators
- evaluate variables and constants
- give helpful syntax error messages

While this may sound like a lot, this is actually rather doable in a limited amount of time.

### Example Usage:
```py
from math import sin, pi
from calculator import parse

variables = {
    'pi': pi,
    'sin': sin,
    'x': 3
}

expression = 'sin(pi + 4) * x'
ast = parse(expression)
result = ast.eval(variables)
print(result)
```

## Non-Goals
This is a tutorial for beginners, so we wont:
- have multiline input
- define our own functions
- use a lexer
- optimize, inline or otherwise change the AST
- typing or runtime error support

But once you are through this tutorial, you should be able to do that yourself!

---

[Chapters](../README.md#Chapters) | [Next: Structre&AST](structure.md)