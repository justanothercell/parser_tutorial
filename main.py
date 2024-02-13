from math import sin, pi
from calculator import parse

variables = {
    'pi': pi,
    'sin': sin,
    'x': 3
}

expression = 's i n(pi + 4) * x'
ast = parse(expression)
result = ast.eval(variables)
print(result)