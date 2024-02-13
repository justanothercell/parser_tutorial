# Conclusion

[Back: Evaluation](evaluation.md) | [Chapters](../README.md#Chapters)

---

## Where to go from here
There are many things to improve or to extend for this project:
- strings, booleans and other data types
- fixing the whitespace<br>
Since we are skipping whitespaces, `sin(x)` is equivalent to `s i n ( x )`!
This is not an issue during normal operation, but it might become one later.
- proper runtime error support with formatting (hint: store the current start and end index (the `span`) inside the AST nodes and use it to make an exception similar to `ParseException`)
- Ast to string (hint: override `__str__` or create a similar method which you can call recursively, similar to `eval`)
- variable assignments and multiple (multiline) statements
- [**hard**] a lexer/tokenizer so that you dont ahve to operate on raw chars
- [**hard**] conditions and loops
- [**hard**] functions definitions
---
### Return to [README](../README.md)

### Check out the [code](../calculator/)

[Back: Evaluation](evaluation.md) | [Chapters](../README.md#Chapters)
