# ZeroLang

## 0. Overview

ZeroLang is a small interpreted programming language implemented in Python.  
It is expression-oriented, dynamically typed, and designed for learning and experimentation with language implementation.

### Important Syntax Rule

**ZeroLang programs are written as a single logical line.**

* The semicolon (`;`) represents a newline.
    
* Physical line breaks are ignored by the parser.
    
* All multi-statement programs must use `;` explicitly.
    

Conceptually, this program:

```plaintext
var x = 1;
var y = 2;
x + y
```

is treated as **one single line of code** by the language.

* * *

## 1. Running ZeroLang

Start the interactive shell:

```bash
python3 shell.py
```

Or execute code using the `run` function in Python.

* * *

## 2. Lexical Elements

### 2.1 Keywords

The following keywords are reserved:

```
var
and
or
not
if
then
elif
else
for
to
step
while
func
end
return
continue
break
```

* * *

### 2.2 Identifiers

Identifiers consist of letters, digits, and underscores, and must not start with a digit.

Examples:

```plaintext
x
counter
temp_value
```

* * *

### 2.3 Literals

#### Numbers

```plaintext
10
3.14
0.25
```

#### Strings

Strings use double quotes.

```plaintext
"hello"
"line1\nline2"
```

#### Lists

```plaintext
[1, 2, 3]
["a", "b", "c"]
```

* * *

## 3. Operators

### 3.1 Arithmetic Operators

| Operator | Meaning |
| --- | --- |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulo |
| `^` | Power |

Example:

```plaintext
2 + 3 * 4
```

* * *

### 3.2 Comparison Operators

```plaintext
==  !=  <  >  <=  >=
```

Example:

```plaintext
x >= 10
```

* * *

### 3.3 Logical Operators

```plaintext
and  or  not
```

Example:

```plaintext
x > 0 and x < 10
```

* * *

## 4. Statement Model

### 4.1 Single-Line Program Model

ZeroLang does **not** use real newlines.

Instead:

* `;` separates statements
    
* The entire program is parsed as a single sequence of statements
    

Valid program:

```plaintext
var x = 10; var y = 20; x + y
```

Invalid program:

```plaintext
var x = 10
var y = 20
```

* * *

## 5. Grammar (EBNF-style)

### 5.1 Program Structure

```ebnf
program        ::= statement (";" statement)* EOF
statement      ::= return_stmt
                 | continue_stmt
                 | break_stmt
                 | expr
```

* * *

### 5.2 Expressions

```ebnf
expr           ::= var_assign
                 | logic_expr

var_assign     ::= "var" IDENTIFIER "=" expr

logic_expr     ::= comp_expr (("and" | "or") comp_expr)*

comp_expr      ::= arith_expr
                 | "not" comp_expr
                 | arith_expr (("==" | "!=" | "<" | ">" | "<=" | ">=") arith_expr)

arith_expr     ::= term (("+" | "-") term)*

term           ::= factor (("*" | "/" | "%") factor)*

factor         ::= ("+" | "-") factor
                 | power

power          ::= call ("^" factor)*

call           ::= atom ("(" (expr ("," expr)*)? ")")?

atom           ::= INT
                 | FLOAT
                 | STRING
                 | IDENTIFIER
                 | list_expr
                 | if_expr
                 | for_expr
                 | while_expr
                 | func_def
                 | "(" expr ")"
```

* * *

## 6. Control Flow (We still got bug in this) 

### 6.1 If Expression

All branches are written inline using `;`.

Single expression (no `end` required):

```plaintext
if x > 0 then 10 else 20
```

Multiple statements (requires `end`):

```plaintext
if x > 0 then; var y = x * 2; y; end
```

With elif:

```plaintext
if x > 0 then 10 elif x == 0 then 0 else -x
```

The `if` expression always returns a value.

* * *

### 6.2 While Loop

Single expression (no `end` required):

```plaintext
var x = 0; while x < 5 then x
```


* * *

### 6.3 For Loop

Single expression (no `end` required):

```plaintext
for i = 0 to 5 then i
```

Multiple statements (requires `end`):

```plaintext
for i = 0 to 5 then; print(i); end
```

With step:

```plaintext
for i = 10 to 0 step -1 then i
```

* * *

## 7. Functions

### 7.1 Function Definition

Single-expression function:

```plaintext
func add(a, b) -> a + b
```



* * *

### 7.2 Function Call

```plaintext
add(2, 3)
```

Functions are first-class values.

* * *

## 8. Control Statements

### 8.1 Return

```plaintext
return x * 2
```

* Valid only inside functions
    
* Immediately exits the current function
    

* * *

### 8.2 Break

```plaintext
break
```

* Exits the nearest enclosing loop
    

* * *

### 8.3 Continue

```plaintext
continue
```

* Skips to the next loop iteration
    

* * *

## 9. Built-in Functions

Example usage (single line):

```plaintext
var l = [3, 1, 2]; sort(l,0); print(l)
```

Available built-ins include:

```
print
print_ret
input
input_int
clear
cls
is_number
is_string
is_list
is_function
append
pop
extend
add
abs
min
max
sort
```

* * *


This entire program is parsed as **one single logical line**.

* * *

## 10. Error Handling

ZeroLang reports:

* Lexical errors
    
* Syntax errors
    
* Runtime errors
    

Errors include precise source positions.

* * *

## 12. Current Limitations

* No real newline support
    
* Semicolon is mandatory
    
* No block-level scope
    
* No optimizations
    

* * *

If you want, the next logical steps would be:

* Adding real newline tokens
    
* Making semicolons optional
    
* Introducing block scopes
    
* Generating a formal language specification
    

Just tell me what you want to do next.

* * *