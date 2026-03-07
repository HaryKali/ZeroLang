# ZeroLang

ZeroLang is a small interpreted language written in Python.
It is expression-oriented, dynamically typed, and designed for learning language implementation fundamentals.

## Highlights

- Simple syntax with familiar operators
- Variables, strings, lists, and user-defined functions
- Control flow: `if`, `for`, `while`, `return`, `break`, `continue`
- Built-in utility functions for I/O and list operations
- REPL support through `shell.py`
- Script execution from code using the built-in `run("path.zero")`

## Requirements

- Python 3.10+

## Quick Start

Run the interactive shell:

```bash
python shell.py
```

Run from Python:

```python
import ZeroLang

value, error = ZeroLang.run("<stdin>", 'print("Hello World")')
if error:
    print(error.as_string())
else:
    print(value)
```

## Program Structure

A ZeroLang program is parsed as a sequence of statements.

Statement separators:

- `;`
- Physical newline

Both are valid, so these two styles are equivalent:

```plaintext
var x = 1; var y = 2; print(x + y)
```

```plaintext
var x = 1
var y = 2
print(x + y)
```

Single-line comments start with `#`.

## Keywords

```plaintext
var and or not if then elif else for to step while func end return continue break
```

## Data Types

- Number (int/float)
- String
- List
- Function
- Null-like value: `NULL`
- Boolean-like values: `TRUE`, `FALSE` (also `True`, `False`)

## Operators

Arithmetic:

```plaintext
+  -  *  /  %  ^
```

Comparison:

```plaintext
==  !=  <  >  <=  >=
```

Logical:

```plaintext
and  or  not
```

## Variables

```plaintext
var x = 10
var name = "ZeroLang"
var arr = [1, 2, 3]
```

## Control Flow

### If

```plaintext
if x > 0 then 1 elif x == 0 then 0 else -1
```

Block style:

```plaintext
if x > 0 then
print("positive")
else
print("not positive")
end
```

### For

```plaintext
for i = 0 to 5 then print(i)
for i = 10 to 0 step -2 then print(i)
```

### While

```plaintext
var i = 0
while i < 3 then var i = i + 1
```

## Functions

Expression form:

```plaintext
func add(a, b) -> a + b
print(add(2, 3))
```

Block form with `return`:

```plaintext
func sum_to(n)
var total = 0
for i = 1 to n + 1 then var total = total + i
return total
end
print(sum_to(5))
```

## Lists

```plaintext
var l = [3, 1, 2]
append(l, 5)
print(l)
print(pop(l, 1))
sort(l, 0)
print(l)
print(len(l))
```

List indexing uses `/` with a numeric index:

```plaintext
var seq = [10, 20, 30]
print(seq / 1)
```

## Built-in Functions

Core:

- `print(value)`
- `print_ret(value)`
- `input()`
- `input_int()`
- `clear()` / `cls()`

Type checks:

- `is_number(value)`
- `is_string(value)`
- `is_list(value)`
- `is_function(value)`

List operations:

- `append(list, value)`
- `pop(list, index)`
- `extend(listA, listB)`
- `len(list)`
- `sort(target_list, reverse)`

Script execution:

- `run(filename)`

Compatibility aliases are also available in the runtime:

- `is_sum`, `is_str`, `is_fun`, `exetend`

## Running `.zero` Files from Shell

Inside `python shell.py`, execute scripts with:

```plaintext
run("examples/test_fibonacci.zero")
```

You can also create launcher scripts:

```plaintext
# examples/run_fibonacci.zero
run("examples/test_fibonacci.zero")
```

Then execute:

```plaintext
run("examples/run_fibonacci.zero")
```

## Examples Included

The `examples` folder contains practical tests:

- `hello_world.zero`
- `test_arithmetic.zero`
- `test_if.zero`
- `test_loops.zero`
- `test_function.zero`
- `test_lists.zero`
- `test_builtins.zero`
- `test_comments_newlines.zero`
- `test_fibonacci.zero`
- `run_fibonacci.zero`

## Error Reporting

ZeroLang reports:

- Lexical errors
- Syntax errors
- Runtime errors with traceback context

Errors include source positions to help locate the failing code quickly.

## Current Notes

- The runtime currently prints debug tokens/parse success messages.
- Global names are shared through a single global symbol table.
- The project is focused on educational clarity over optimization.

## Project Files

- `ZeroLang.py`: lexer, parser, AST, interpreter, runtime values, built-ins
- `shell.py`: interactive console
- `strings_with_arrows.py`: error pointer rendering
- `examples/`: runnable language examples

