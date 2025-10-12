
# ZeroLang

## 0. Introduction
A simple programing language based on basic 

* Still working on it
* Now is a simpile interpreter which support basic arithmetic operations

## 1. Try ZeroLang in terminal

      python3 shell.py 


## 🔤 Basic Elements

### Variable Declaration

Use the `var` keyword to declare a variable:

```plaintext
var x = 10
```

---

### Number Types

Supports both integers and floats:

```plaintext
x = 5
y = 3.14
```

---

### Operators

#### Arithmetic Operators

| Operator | Meaning | Example |
| --- | --- | --- |
| `+` | Addition | `2 + 3` |
| `-` | Subtraction | `5 - 1` |
| `*` | Multiplication | `4 * 2` |
| `/` | Division | `10 / 2` |
| `%` | Modulo | `7 % 3` |
| `^` | Power | `2 ^ 3` |

#### Comparison Operators

| Operator | Meaning | Example |
| --- | --- | --- |
| `==` | Equals | `x == 5` |
| `!=` | Not equals | `x != 0` |
| `<` | Less than | `x < 10` |
| `>` | Greater than | `x > 3` |
| `<=` | Less than or equal | `x <= 5` |
| `>=` | Greater or equal | `x >= 2` |

#### Logical Operators

| Keyword | Meaning | Example |
| --- | --- | --- |
| `and` | Logical AND | `x > 0 and y < 10` |
| `or` | Logical OR | `x == 0 or y == 5` |
| `not` | Logical NOT | `not x == 0` |

---

### Strings

Defined using double quotes, with support for escape characters:

```plaintext
msg = "Hello\nWorld"
```

---

### Lists

Lists are enclosed in square brackets:

```plaintext
arr = [1, 2, 3]
```

- Access element: `arr / 1` → returns element at index 1
- Remove element: `arr - 0` → removes element at index 0

---

## 🔁 Control Flow

### If Expression

```plaintext
if x > 0 then "positive"
elif x == 0 then "zero"
else "negative"
```

---

### For Loop

```plaintext
for i = 1 to 5 then i * 2
```

With optional step:

```plaintext
for i = 1 to 10 step 2 then i
```

---

### While Loop

```plaintext
while x < 5 then x = x + 1
```

---

## 🧩 Functions

### Define a Function

```plaintext
func add(a, b) -> a + b
```

### Anonymous Function

```plaintext
var square = func(x) -> x * x
```

### Function Call

```plaintext
add(2, 3)  # Returns 5
```

---

## ⚙️ Built-in Functions

ZeroLang provides several built-in functions for common operations:

### `print(value)`

Prints the value to the console.

```plaintext
print("Hello, World!")
```

---

### `print_ret(value)`

Returns the string representation of the value (does not print).

```plaintext
var msg = print_ret(123)
```

---

### `input()`

Prompts user for input as a string.

```plaintext
var name = input()
```

---

### `input_int()`

Prompts user for input until a valid integer is entered.

```plaintext
var age = input_int()
```

---

### `clear()` / `cls()`

Clears the terminal screen (cross-platform).

```plaintext
clear()
cls()
```

---

### `is_num(value)`

Returns `True` if value is a number, otherwise `False`.

```plaintext
is_num(10)      # True
is_num("abc")   # False
```

---

### `is_str(value)`

Returns `True` if value is a string.

```plaintext
is_str("hello")  # True
```

---

### `is_list(value)`

Returns `True` if value is a list.

```plaintext
is_list([1, 2, 3])  # True
```

---

### `is_fun(value)`

Returns `True` if value is a function.

```plaintext
var f = func(x) -> x + 1
is_fun(f)  # True
```

---

### `append(list, value)`

Appends a value to the end of the list.

```plaintext
var l = [1, 2]
append(l, 3)
# l is now [1, 2, 3]
```

---

### `pop(list, index)`

Removes and returns the element at the given index.

```plaintext
var l = [5, 6, 7]
pop(l, 1)  # returns 6, l becomes [5, 7]
```

---

### `extend(listA, listB)`

Extends `listA` by appending all elements from `listB`.

```plaintext
var a = [1]
var b = [2, 3]
extend(a, b)
# a becomes [1, 2, 3]
```

---

## 🔍 Example Program

```plaintext
var square = func(x) -> x * x
square(4)  
```

---

## ⚠️ Error Handling

Lexical and syntax errors are handled by classes like `IllegalCharError`, `InvalidSyntaxError`, and `RTError`. They provide clear messages with line numbers and context arrows.

---
