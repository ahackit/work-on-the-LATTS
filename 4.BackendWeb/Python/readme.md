# Python

## Variables
- Dynamically Typed
```
width = 50
width = 'Hello'
```
- Arithmetic is all your fundamentals.

### Strings
- Use \ to escape special characters.
- use r'' to specify raw string
- Use """ for multi line strings
- Can slice strings using [0:5]

### Lists
- ```squares = [1, 4, 9]```
- Can be indexed and sliced ```squares[0] - squares[2:3]```


## Control Flow
- if/elif/else:
- for x in iterable:
- break/continue statements

## Functions
- ```def function_name(variable):```
- defaults arguements ```def function_name(variable='Austin):```
- Arbitrary number of arguements ```def function_name(variable, *args, **kwargs):```

## Classes
```
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```