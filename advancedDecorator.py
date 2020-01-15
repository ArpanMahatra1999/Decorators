def function1(function):
    def wrapper(*args, **kwargs):
        print("Hello ")
        function(*args, **kwargs)
        print(" Welcome to Python Learning.")
    return wrapper

@function1
def function2(name):
    print(f"{name}")

function2("Pythonista")