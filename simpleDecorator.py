def function1(function):
    def wrapper():
        print("Hello ")
        function()
        print(" Welcome to Python Learning.")
    return wrapper

@function1
def function2():
    print("Pythonista!")

function2()