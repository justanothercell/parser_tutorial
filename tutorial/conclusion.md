# Conclusion

[Back: Evaluation](evaluation.md) | [Chapters](../README.md#Chapters)

---

## Where to go from here
There are many things to improve or to extend for this project:
- strings, booleans and other data types
- proper runtime error support with formatting (hint: store the current start and end index, called `span` inside the AST nodes)
- Ast to string (hint: override `__str__` or create a similar method which you can call recursively, similar to `eval`)
- variable assignments and multiple (multiline) statements
- [**hard**] a lexer/tokenizer so that you dont ahve to operate on raw chars
- [**hard**] conditions and loops
- [**hard**] in-language functions
---
### Return to [README](../README.md)

### Check out the [code](../calculator/)

[Back: Evaluation](evaluation.md) | [Chapters](../README.md#Chapters)
