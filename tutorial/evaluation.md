# Evaluation

[Back: Nodes Parsing](nodes.md) | [Chapters](../README.md#Chapters) | [Next: Conclusion](conclusion.md)

---

Add a method `def eval(self, variables)` to every AST node and 
recursively call `eval` until you reach the terminal leaves.

For now we will disregard all runtime errors.

<details>
<summary>Value</summary>

```py
class Value(AST):
    ...
    def eval(self, variables):
        return self.value
```
</details>

<details>
<summary>Variable</summary>

```py
class Variable(AST):
    ...
    def eval(self, variables):
        return variables[self.name]
```
</details>

<details>
<summary>FuncCall</summary>

```py
class FuncCall(AST):
    ...
    def eval(self, variables):
        args = [arg.eval(variables) for arg in self.args]
        return variables[self.name](args)
```
</details>

<details>
<summary>BinaryOp</summary>

```py
class BinaryOp(AST):
    ...
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
```
</details>

<details>
<summary>UnaryOp</summary>

```py
class UnaryOp(AST):
    ...
    def eval(self, variables):
        item = self.item.eval(variables)
        if self.op == '+':
            return +item # redundant, but ey why not
        if self.op == '-':
            return -item
```
</details>

And we are done!

```
%>py main.py
2.2704074859237844
```

---

[Back: Nodes Parsing](nodes.md) | [Chapters](../README.md#Chapters) | [Next: Conclusion](conclusion.md)