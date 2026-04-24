import os

from zerolang.errors import RTError
from zerolang.rtresult import RTResult
from zerolang.values import BaseFunction, Number, String, List, Function


class BuiltInFunction(BaseFunction):
    def __init__(self, name):
        super().__init__(name)

    def execute(self, args):
        res = RTResult()
        exec_ctx = self.generate_new_context()
        method_name = f"execute_{self.name}"
        method = getattr(self, method_name, self.no_visit_method)

        res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
        if res.error:
            return res

        return_value = res.register(method(exec_ctx))
        if res.error:
            return res
        return res.success(return_value)

    def no_visit_method(self, exec_ctx):
        raise Exception(f"No execute_{self.name} method defined")

    def copy(self):
        copy = BuiltInFunction(self.name)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<Built-in function {self.name}>"

    def execute_len(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        return RTResult().success(Number(len(list_.elements)))

    execute_len.arg_names = ["list"]

    def execute_print(self, exec_ctx):
        print(str(exec_ctx.symbol_table.get("value")))
        return RTResult().success(Number.null)

    execute_print.arg_names = ["value"]

    def execute_print_ret(self, exec_ctx):
        return RTResult().success(String(str(exec_ctx.symbol_table.get("value"))))

    execute_print_ret.arg_names = ["value"]

    def execute_input(self, exec_ctx):
        text = input()
        return RTResult().success(String(text))

    execute_input.arg_names = []

    def execute_input_int(self, exec_ctx):
        while True:
            value = input()
            try:
                value = int(value)
                break
            except ValueError:
                print(f"'{value}' should be int , try again")
        return RTResult().success(Number(value))

    execute_input_int.arg_names = []

    def execute_clear(self, exec_ctx):
        os.system("cls" if os.name == "nt" else "clear")
        return RTResult().success(Number.null)

    execute_clear.arg_names = []

    def execute_is_number(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get("value"), Number)
        return RTResult().success(Number.true if is_number else Number.false)

    execute_is_number.arg_names = ["value"]

    def execute_is_string(self, exec_ctx):
        is_string = isinstance(exec_ctx.symbol_table.get("value"), String)
        return RTResult().success(Number.true if is_string else Number.false)

    execute_is_string.arg_names = ["value"]

    def execute_is_function(self, exec_ctx):
        is_func = isinstance(exec_ctx.symbol_table.get("value"), (Function, BuiltInFunction))
        return RTResult().success(Number.true if is_func else Number.false)

    execute_is_function.arg_names = ["value"]

    def execute_is_list(self, exec_ctx):
        is_list = isinstance(exec_ctx.symbol_table.get("value"), List)
        return RTResult().success(Number.true if is_list else Number.false)

    execute_is_list.arg_names = ["value"]

    def execute_append(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        value = exec_ctx.symbol_table.get("value")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        list_.elements.append(value)
        return RTResult().success(Number.null)

    execute_append.arg_names = ["list", "value"]

    def execute_pop(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        index = exec_ctx.symbol_table.get("index")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        if not isinstance(index, Number):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be int",
                exec_ctx
            ))
        try:
            element = list_.elements.pop(index.value)
        except Exception:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Out of index!!!",
                exec_ctx
            ))
        return RTResult().success(element)

    execute_pop.arg_names = ["list", "index"]

    def execute_extend(self, exec_ctx):
        listA = exec_ctx.symbol_table.get("listA")
        listB = exec_ctx.symbol_table.get("listB")
        if not isinstance(listA, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))
        if not isinstance(listB, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be list",
                exec_ctx
            ))
        listA.elements.extend(listB.elements)
        return RTResult().success(Number.null)

    execute_extend.arg_names = ["listA", "listB"]

    def execute_sort(self, exec_ctx):
        target_list = exec_ctx.symbol_table.get("target_list")
        if not isinstance(target_list, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "argument must be list",
                exec_ctx
            ))

        reverse_param = exec_ctx.symbol_table.get("reverse")
        reverse = False
        if isinstance(reverse_param, Number):
            reverse = reverse_param.value != 0

        def get_sort_key(element):
            if isinstance(element, Number):
                return element.value
            if isinstance(element, String):
                return str(element.value)
            return element

        target_list.elements.sort(key=get_sort_key, reverse=reverse)
        return RTResult().success(Number.null)

    execute_sort.arg_names = ["target_list", "reverse"]

    def execute_run(self, exec_ctx):
        from zerolang.run import run

        fn = exec_ctx.symbol_table.get("fn")

        if not isinstance(fn, String):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Argument must be string",
                exec_ctx
            ))
        fn = fn.value

        try:
            with open(fn, "r", encoding="utf-8") as f:
                script = f.read()
        except Exception as e:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"File {fn} not found\n" + str(e),
                exec_ctx
            ))
        _, error = run(fn, script)
        if error:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to finish executing script" + str(error),
                error.as_string(),
            ))
        return RTResult().success(Number.null)

    execute_run.arg_names = ["fn"]


BuiltInFunction.print = BuiltInFunction("print")
BuiltInFunction.print_ret = BuiltInFunction("print_ret")
BuiltInFunction.input = BuiltInFunction("input")
BuiltInFunction.input_int = BuiltInFunction("input_int")
BuiltInFunction.clear = BuiltInFunction("clear")
BuiltInFunction.is_number = BuiltInFunction("is_number")
BuiltInFunction.is_string = BuiltInFunction("is_string")
BuiltInFunction.is_list = BuiltInFunction("is_list")
BuiltInFunction.is_function = BuiltInFunction("is_function")
BuiltInFunction.append = BuiltInFunction("append")
BuiltInFunction.pop = BuiltInFunction("pop")
BuiltInFunction.extend = BuiltInFunction("extend")
BuiltInFunction.len = BuiltInFunction("len")
BuiltInFunction.sort = BuiltInFunction("sort")
BuiltInFunction.run = BuiltInFunction("run")
