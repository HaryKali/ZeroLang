import ZeroLang
while True:

    text = input("ZeroLang (Debug) >")
    result, error = ZeroLang.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result.elements))

