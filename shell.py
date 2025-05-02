import ZeroLang
import sys




while True:

    text = input("ZeroLang (Debug) >")
    result, error = ZeroLang.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        print(result)


