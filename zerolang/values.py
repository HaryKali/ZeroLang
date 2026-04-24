import math

from zerolang.errors import RTError
from zerolang.rtresult import RTResult


class Value:
    def __init__(self):
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def added_to(self, other):
        return None, self.illegal_operation()

    def subbed_by(self, other):
        return None, self.illegal_operation()

    def multed_by(self, other):
        return None, self.illegal_operation()

    def dived_by(self, other):
        return None, self.illegal_operation()

    def modded_by(self, other):
        return None, self.illegal_operation()

    def powed_by(self, other):
        return None, self.illegal_operation()

    def get_comparison_eq(self, other):
        return None, self.illegal_operation()

    def get_comparison_ne(self, other):
        return None, self.illegal_operation()

    def get_comparison_lt(self, other):
        return None, self.illegal_operation()

    def get_comparison_gt(self, other):
        return None, self.illegal_operation()

    def get_comparison_lte(self, other):
        return None, self.illegal_operation()

    def get_comparison_gte(self, other):
        return None, self.illegal_operation()

    def anded_by(self, other):
        return None, self.illegal_operation()

    def ored_by(self, other):
        return None, self.illegal_operation()

    def notted(self):
        return None, self.illegal_operation()

    def copy(self):
        raise Exception("No copy method deined")

    def is_true(self):
        return False

    def illegal_operation(self, other=None):
        if not other:
            other = self
        return RTError(
            self.pos_start, other.pos_end,
            "Illegal operation",
            self.context
        )


class List(Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def added_to(self, other):
        new_list = self.copy()
        new_list.elements.append(other)
        return new_list, None

    def subbed_by(self, other):
        if isinstance(other, Number):
            new_list = self.copy()
            try:
                new_list.elements.pop(other.value)
                return new_list, None
            except Exception:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    "Element at this index could not be remove from the list because index is not correct",
                    self.context
                )
        return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        if isinstance(other, Number):
            try:
                return self.elements[other.value], None
            except Exception:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    "Element at this index could not be retrieved from the list because index is not correct",
                    self.context
                )
        return None, Value.illegal_operation(self, other)

    def copy(self):
        copy = List(self.elements[:])
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def multed_by(self, other):
        if isinstance(other, List):
            new_list = self.copy()
            new_list.elements.extend(other.elements)
            return new_list, None
        return None, Value.illegal_operation(self, other)

    def __str__(self):
        return f'{",".join([str(x) for x in self.elements])}'

    def __repr__(self):
        return f'[{",".join([str(x) for x in self.elements])}]'


class String(Value):
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def added_to(self, other):
        if isinstance(other, String):
            return String(self.value + other.value).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def multed_by(self, other):
        if isinstance(other, Number):
            return String(self.value * other.value).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def copy(self):
        copy = String(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return self.value


class Number(Value):
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def dived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Division by zero',
                    self.context
                )
            return Number(self.value / other.value).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def modded_by(self, other):
        if isinstance(other, Number):
            return Number(self.value % other.value).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def powed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def get_comparison_eq(self, other):
        if isinstance(other, Number):
            return Number(int(self.value == other.value)).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def get_comparison_ne(self, other):
        if isinstance(other, Number):
            return Number(int(self.value != other.value)).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def get_comparison_lt(self, other):
        if isinstance(other, Number):
            return Number(int(self.value < other.value)).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def get_comparison_gt(self, other):
        if isinstance(other, Number):
            return Number(int(self.value > other.value)).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def get_comparison_lte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value <= other.value)).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def get_comparison_gte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value >= other.value)).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def anded_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def ored_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).set_context(self.context), None
        return None, self.illegal_operation(self.pos_start, other.pos_end)

    def notted(self):
        return Number(1 if self.value == 0 else 0).set_context(self.context), None

    @staticmethod
    def math_PI():
        return math.pi

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.value != 0

    def __repr__(self):
        return str(self.value)


Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)


class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None


class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def get(self, name):
        value = self.symbols.get(name, None)
        if value is None and self.parent:
            return self.parent.get(name)
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]


class BaseFunction(Value):
    def __init__(self, name):
        super().__init__()
        self.name = name or "<anonymous>"

    def generate_new_context(self):
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        return new_context

    def check_args(self, arg_names, args):
        res = RTResult()
        if len(args) > len(arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(args) - len(arg_names)} too many args passed into {self.name}",
                self.context
            ))
        if len(args) < len(arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(arg_names) - len(args)} need more args passed into {self.name}",
                self.context
            ))
        return res.success(None)

    def populate_args(self, arg_names, args, exec_ctx):
        for i in range(len(args)):
            arg_name = arg_names[i]
            arg_value = args[i]
            arg_value.set_context(exec_ctx)
            exec_ctx.symbol_table.set(arg_name, arg_value)

    def check_and_populate_args(self, arg_names, args, exec_ctx):
        res = RTResult()
        res.register(self.check_args(arg_names, args))
        if res.error:
            return res
        self.populate_args(arg_names, args, exec_ctx)
        return res.success((None))


class Function(BaseFunction):
    def __init__(self, name, body_node, arg_names, should_return_null):
        super().__init__(name)
        self.body_node = body_node
        self.arg_names = arg_names
        self.should_return_null = should_return_null

    def execute(self, args):
        from zerolang.interpreter import Interpreter

        res = RTResult()
        interpreter = Interpreter()
        exec_ctx = self.generate_new_context()
        res.register(self.check_and_populate_args(self.arg_names, args, exec_ctx=exec_ctx))
        if res.should_return():
            return res
        value = res.register(interpreter.visit(self.body_node, exec_ctx))
        if res.should_return() and res.func_return_value is None:
            return res
        return_value = Number.null if self.should_return_null else value
        if res.func_return_value is not None:
            return_value = res.func_return_value
        return res.success(return_value)

    def copy(self):
        copy = Function(self.name, self.body_node, self.arg_names, self.should_return_null)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<function {self.name}>"
