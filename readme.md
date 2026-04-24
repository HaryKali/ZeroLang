# ZeroLang

ZeroLang is a small interpreted programming language implemented in Python. It is expression-oriented, dynamically typed, and designed for learning language implementation fundamentals.

## Highlights

- Simple syntax with familiar operators
- Variables, strings, lists, and user-defined functions
- Control flow including if, for, while, return, break, and continue
- Built-in functions for input/output and list manipulation
- REPL support via shell.py
- Ability to execute scripts using the built-in run function

## Requirements

- Python 3.10 or higher

## Quick Start

Run the interactive shell:

```bash
python shell.py
```

Execute code from Python:

```python
import ZeroLang

value, error = ZeroLang.run("<stdin>", 'print("Hello World")')
if error:
    print(error.as_string())
else:
    print(value)
```

## Program Structure

ZeroLang programs are parsed as sequences of statements. Statements can be separated by semicolons (;) or physical newlines. Both are supported.

Example:

```plaintext
var x = 1
var y = 2
print(x + y)
```

Single-line comments begin with #.

## Keywords

```
var and or not if then elif else for to step while func end return continue break
```

## Data Types

- Number (integer or float)
- String
- List
- Function
- NULL
- Boolean-like values (TRUE, FALSE, True, False)

## Operators

### Arithmetic

+ - * / % ^

### Comparison

== != < > <= >=

### Logical

and or not

## Variables

```plaintext
var x = 10
var name = "ZeroLang"
var arr = [1, 2, 3]
```

## Control Flow

### If Expression

```plaintext
if x > 0 then 1 elif x == 0 then 0 else -1
```

Block form:

```plaintext
if x > 0 then
    print("positive")
else
    print("not positive")
end
```

### For Loop

```plaintext
for i = 0 to 5 then print(i)
for i = 10 to 0 step -2 then print(i)
```

### While Loop

```plaintext
var i = 0
while i < 3 then var i = i + 1
```

## Functions

Single expression:

```plaintext
func add(a, b) -> a + b
print(add(2, 3))
```

With block and return:

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

List access uses division syntax:

```plaintext
var seq = [10, 20, 30]
print(seq / 1)
```

## Built-in Functions

Core functions:

- print(value)
- print_ret(value)
- input()
- input_int()
- clear() / cls()

Type checking:

- is_number(value)
- is_string(value)
- is_list(value)
- is_function(value)

List operations:

- append(list, value)
- pop(list, index)
- extend(listA, listB)
- len(list)
- sort(target_list, reverse)

Script execution:

- run(filename)

Compatibility aliases (is_sum, is_str, is_fun, exetend) are also registered.

## Running Scripts from Shell

From within the REPL (python shell.py):

```plaintext
run("examples/test_fibonacci.zero")
```

Launcher scripts are also supported:

```plaintext
# examples/run_fibonacci.zero
run("examples/test_fibonacci.zero")
```

Then run:

```plaintext
run("examples/run_fibonacci.zero")
```

## Examples

The examples directory includes:

- hello_world.zero
- test_arithmetic.zero
- test_if.zero
- test_loops.zero
- test_function.zero
- test_lists.zero
- test_builtins.zero
- test_comments_newlines.zero
- test_fibonacci.zero
- test_fibonacci_iterative.zero
- run_fibonacci.zero

## Error Reporting

ZeroLang provides detailed error reporting for:

- Lexical errors
- Syntax errors
- Runtime errors (with traceback)

Errors include source location information using arrows to point to the offending code.

## Project Structure

- ZeroLang.py: Public API and backward compatibility layer
- zerolang/: Main implementation package
  - errors.py: Error classes and formatting
  - tokens.py: Token definitions and Position class
  - lexer.py: Tokenizer
  - nodes.py: Abstract Syntax Tree node definitions
  - parser.py: Recursive descent parser
  - rtresult.py: Runtime result and control flow handling
  - values.py: Runtime value types (Number, String, List, Function, etc.)
  - builtins.py: Built-in functions implementation
  - globals.py: Global symbol table initialization
  - interpreter.py: AST visitor and evaluation logic
  - run.py: Main execution driver
- shell.py: Interactive REPL
- strings_with_arrows.py: Source code error pointer visualization
- examples/: Test scripts and examples

## Notes

- Debug messages for lexical and syntax analysis are currently enabled
- All variables share a single global symbol table
- The implementation prioritizes educational clarity over performance optimizations

This project does not declare a specific license.
