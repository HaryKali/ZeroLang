class RTResult:
    def __init__(self):
        self.value = None
        self.error = None
        self.func_return_value = None
        self.loop_should_continue = False
        self.loop_should_break = False

    def register(self, res):
        if res.error:
            self.error = res.error
        self.func_return_value = res.func_return_value
        self.loop_should_continue = res.loop_should_continue
        self.loop_should_break = res.loop_should_break
        return res.value

    def success(self, value):
        self.value = value
        self.error = None
        self.func_return_value = None
        self.loop_should_continue = False
        self.loop_should_break = False
        return self

    def success_return(self, value):
        self.value = None
        self.error = None
        self.func_return_value = value
        self.loop_should_continue = False
        self.loop_should_break = False
        return self

    def success_continue(self):
        self.value = None
        self.error = None
        self.func_return_value = None
        self.loop_should_continue = True
        self.loop_should_break = False
        return self

    def success_break(self):
        self.value = None
        self.error = None
        self.func_return_value = None
        self.loop_should_continue = False
        self.loop_should_break = True
        return self

    def failure(self, error):
        self.error = error
        self.value = None
        self.func_return_value = None
        self.loop_should_continue = False
        self.loop_should_break = False
        return self

    def should_return(self):
        return (
            self.error or
            self.func_return_value or
            self.loop_should_continue or
            self.loop_should_break
        )
