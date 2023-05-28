# Code Wars Solutions - Python
Solutions to [Code War Katas](https://www.codewars.com) written in Python.

## Katas

### 6kyu
* [Find Cracker](https://www.codewars.com/kata/59f70440bee845599c000085)
* [Flip Your Stack (of Pancakes)](https://www.codewars.com/kata/6472390e0d0bb1001d963536)

### 8kyu
* [Pillars](https://www.codewars.com/kata/5bb0c58f484fcd170700063d)

## Test
```
source venv/bin/activate
pytest
```

## Build
```
flake8 code_wars_python tests
mypy --disallow-untyped-defs code_wars_python tests
```
