from zerolang.globals import global_symbol_table
from zerolang.interpreter import Interpreter
from zerolang.lexer import Lexer
from zerolang.parser import Parser
from zerolang.values import Context


def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error
    print("\033[32m" + "DEBUG: Lexical Analysis OK！" + "\033[39m")
    print(tokens)
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error
    print("\033[32m" + "DEBUG: Syntax Analysis OK！" + "\033[39m")

    interpreter = Interpreter()
    context = Context("<program>")
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error