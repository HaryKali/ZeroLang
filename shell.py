import basic
import sys




while True:

    text = input("ZeroLang (Debug) >")
    result, error = basic.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        print(result)


