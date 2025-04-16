import basic
import signal
import sys

def signal_cplusz(signal, frame):
    print("Crtl+z:Quit ZeroLang ")
    sys.exit(1)

signal.signal(signal.SIGINT,signal_cplusz)

while True:

    text = input("ZeroLang (Debug) >")
    result, error = basic.run("<stdin>", text)
    if error:
        print(error.as_string())
    elif result:
        print(result)
