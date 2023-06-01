# Code Wars Solutions - Python
Solutions to [Code War Katas](https://www.codewars.com) written in Python.

## Katas

### 3kyu
* [The Lift](https://www.codewars.com/kata/58905bfa1decb981da00009e)

### 5kyu
* [Simple Fun #89: Boxes Packing](https://www.codewars.com/kata/58957c5041c979cf9e00002f)

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
