printed_strings = set()

def modern_print(s):
    if s not in printed_strings:
        print(s)
        printed_strings.add(s)

modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")