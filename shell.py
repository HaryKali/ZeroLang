import ZeroLang

def run_repl():
    print("\033[1;36m")
    print(r"""
 ________                       __                                   
/\_____  \                     /\ \                                  
\/____//'/'     __   _ __   ___\ \ \         __      ___      __     
     //'/'    /'__`\/\`'__\/ __`\ \ \  __  /'__`\  /' _ `\  /'_ `\   
    //'/'___ /\  __/\ \ \//\ \L\ \ \ \L\ \/\ \L\.\_/\ \/\ \/\ \L\ \  
    /\_______\ \____\\ \_\\ \____/\ \____/\ \__/.\_\ \_\ \_\ \____ \ 
    \/_______/\/____/ \/_/ \/___/  \/___/  \/__/\/_/\/_/\/_/\/___L\ \
                                                              /\____/
                                                              \_/__/ 
""")
    print("\033[0m")
    print("ZeroLang Debug Console - Version 0.1")
    print("Type 'exit', 'quit' or 'bye' to exit")
    print("=" * 60)

    while True:
        try:
            text = input("\033[1;32mZeroLang (Debug) > \033[0m")
        except EOFError:
            print("\n\033[1;33mExiting ZeroLang debug console. Happy coding!\033[0m")
            break

        if text.strip().lower() in ["exit", "quit", "bye"]:
            print("\033[1;33mClosing ZeroLang debug session. Keep exploring!\033[0m")
            break

        if text.strip() == "":
            continue

        result, error = ZeroLang.run("<stdin>", text)

        if error:
            print("\033[1;31m" + error.as_string() + "\033[0m")
        elif result:
            if len(result.elements) == 1:
                print("\033[1;36m" + repr(result.elements[0]) + "\033[0m")
            else:
                print("\033[1;36m" + repr(result.elements) + "\033[0m")


if __name__ == "__main__":
    run_repl()