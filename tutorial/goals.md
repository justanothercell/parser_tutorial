# Chapter 1: Goals

[Chapters](../README.md#Chapters) | [Next: Structure&AST](structure.md)

---

WHat do we want to do and why do we want to do it?

Our goal is to create something similar to python's `eval()` function, but make it safe to use, as for example, a calculator.
Aoyone who has spent some time with python knows that eval is very much the opposite from safe-to-use.

Some evil eval:
- `eval('open("passwords.txt").read()')`

Removing builtin `open` by passing in an explicit `global` dict:
- `eval('__import__("os").system("rm passwords.txt")')`

The possibilites are truly endless!

Even if you manage to close all the countless loopholes, this still does not save you from [arbitrary bytecode execution](https://github.com/DragonFighter603/pybox?tab=readme-ov-file#known-bugsloopholes)
which at best crashes your program and at worst, well, excutes anything.
- [pybox](https://github.com/DragonFighter603/pybox), my attempt to create a semi-safe eval a few years ago
- If you would like to try this on your own, try to get some remote code execution on this [calculator](https://github.com/DragonFighter603/ctf_challenges/tree/main/calculator)

That is why we want our own, safe-to-use implementation of `eval`, where we an explicitly allow which functions the user should have access to.

## Example Usage:
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

## Goals
The parser/evaluator should be able to:
- parse bracketed expressions
- call functions
- use binary operators (with correct precedence)
- use unary operators
- evaluate variables and constants
- give helpful syntax error messages

While this may sound like a lot, this is actually rather doable in a limited amount of time.

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
