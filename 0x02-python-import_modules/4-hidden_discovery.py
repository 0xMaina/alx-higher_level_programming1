#!/usr/bin/python3
import dis

if __name__ == "__main__":
    # Open the compiled module hidden_4.pyc in binary mode
    with open("hidden_4.pyc", "rb") as file:
        # Read the file contents
        code = file.read()

    # Disassemble the code and extract names
    names = set()
    code_obj = compile(code, "hidden_4.pyc", "exec")
    for instr in dis.get_instructions(code_obj):
        if instr.opname == "LOAD_NAME" and not instr.arg.startswith("__"):
            names.add(instr.arg)

    # Print the names in alphabetical order
    for name in sorted(names):
        print(name)