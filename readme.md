# ZeroLang(still woking on it!)

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

## 🔍 Example Program

```plaintext
var square = func(x) -> x * x
square(4)  
```

---

## ⚠️ Error Handling

Lexical and syntax errors are handled by classes like `IllegalCharError`, `InvalidSyntaxError`, and `RTError`. They provide clear messages with line numbers and context arrows.

---




