# Conclusion

[Back: Evaluation](evaluation.md) | [Chapters](../README.md#Chapters)

---

## Where to go from here
There are many things to improve or to extend for this project:
- strings, booleans and other data types
- more operators/multichar operators (`<`, `>`, `<=`, `>=`, `&&`, `||`, ...)
- fixing the whitespace<br>
Since we are skipping whitespaces, `sin(x)` is equivalent to `s i n ( x )`!
This is not an issue during normal operation, but it might become one later.
- proper runtime error support with formatting (hint: store the current start and end index (the `span`) inside the AST nodes and use it to make an exception similar to `ParseException`)
- Ast to string (hint: override `__str__` or create a similar method which you can call recursively, similar to `eval`)
- variable assignments and multiple (multiline) statements
- [**hard**] a lexer/tokenizer so that you dont ahve to operate on raw chars
- [**hard**] conditions and loops
- [**hard**] functions definitions

### Bonus
<details>
<summary>Advanced Precedence</summary>

_This is left out of the main tutorial intentionally to keep things as simple as possible._

In this case, evaluating the operator precedence was easy, since there are only two cases. 
But what if there are more than 2 precedence classes?

Let's explore the following example:
- `*`, `/` binds highest
- `+`, `-` after that
- `<`, `>` after that 
- `|`, `&` the lowest (pretend that this is the logical `or` and `and`, our parser in its current state is not able to handle multichar operators)

To correctly detemine the precedence, we create a precedence table with integer values
representing the "binding force", which we then compare against each other. This also allows us to check
whether something is an operator more easily, without relying on some inline value.

```py
OP_PRECEDENCE = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '<': 1, '>': 1,
    '|': 0, '&': 0
}

class Parser:
    ...
    def parse_expression(self) -> AST:
        ...
        if self.has_current() and self.current() in OP_PRECEDENCE:
        # instead of
        if self.has_current() and self.current() in '+-*/%':
        ...
    ...
    def parse_binary_op(self, left: AST, op: str) -> BinaryOp:
        right = self.parse_expression()
        if isinstance(right, BinaryOp):
            # compare precedences
            if OP_PRECEDENCE[right.op] > OP_PRECEDENCE[op]: # right is strictly higher binding than left
                return BinaryOp(left, right, op)
            # otherwise, we switch to have left-to-right evaluation
            return BinaryOp(BinaryOp(left, right.left, op), right.right, right.op)
        return BinaryOp(left, right, op)
```
</details>


### Return to [README](../README.md)

### Check out the [code](../calculator/)

---

[Back: Evaluation](evaluation.md) | [Chapters](../README.md#Chapters)
