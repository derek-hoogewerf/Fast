def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
