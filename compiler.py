# compiler.py
def compile_code(code):
    return f"Compiling: {code}"

if __name__ == "__main__":
    code_to_compile = "print('Hello, World!')"
    print(compile_code(code_to_compile))
