# Chapter 2: Structure & AST

[Back: Goas](goals.md) | [Overview](../README.md#Overview) | [Next: Parser Layout](parser.md)

---
Let's use this expression as an example: <br> 
`2 * 7 + 4 * (5 + 6) + (sin(4 - 4) - 4)`

If we were to solve this manually - ignoring term manipulation - it would look something like this:

```rs
2 * 7 + 4 * (5 + 6) + (sin(4 - 4) - 4)
  |     |      |        |    |      |
  |     4-[*]--11      sin ( 0 )    |
  |        |               |        |
  14-[+]---44              0---[-]--4
      |                         |
      58-----------[+]--------(-4)
                    |
                   54
```

From this we can see a few patterns emerging:
- First we solve the brackets and functions (applying the other rules in the smaller environment there)
- then we resolve multiplication/division
- then we resolve addition/subtraction

In fact this looks like a tree structure! This is why this is also referred to as an Abstract Syntax Tree (AST).
We can represent this structure with some classes, the AST nodes.

| Class (extending AST) | Fields                         |
|-----------------------|--------------------------------|
| Value                 | value: int|float               |
| Variable              | name: str                      |
| FuncCall              | name: str, args: list[AST]     |
| BinaryOp              | left: AST, right: AST, op: str |
| UnaryOp               | item: AST, op: str             |

You may have noticed that there is no correspondign class for Bracketed expressions.
This is because brackets simply change the shape of the tree:
```
a * (b + c) | BinaryOp with: left = a,     right = b + c, op = "*"
(a * b) + c | BinaryOp with: left = a * b, right = c    , op = "+"
```
You may also have noticed that these structures are recursive: Multiple AST nodes hold AST nodes themselves.
This means that the parser, aswell as the evaluation also needs to be recursive!

Let's start by implementing the AST structures. While we may not know yet how we generate those, it'll 
help us implement the right structures.

<details>
<summary>AST</summary>

```py
# Just a dummy base class.
# In other languages, you would put 
# your abstract methods here.
class AST:
    pass
```
</details>

<details>
<summary>Value</summary>

```py
class Value(AST):
    def __init__(self, value: int|float):
        self.value = value
```
</details>

<details>
<summary>Variable</summary>

```py
class Variable(AST):
    def __init__(self, name: str):
        self.name = name
```
</details>

<details>
<summary>FuncCall</summary>

```py
class FuncCall(AST):
    def __init__(self, name: str, args: list[AST]):
        self.name = name
        self.args = args
```
</details>

<details>
<summary>BinaryOp</summary>

```py
class BinaryOp(AST):
    def __init__(self, left: AST, right: AST, op: str):
        self.left = left
        self.right = right
        self.op = op
```
</details>

<details>
<summary>UnaryOp</summary>

```py
class UnaryOp(AST):
    def __init__(self, item: AST, op: str):
        self.item = item
        self.op = op
```
</details>

---

[Back: Goals](goals.md) | [Chapters](../README.md#Chapters) | [Next: Parser Layout](parser.md)