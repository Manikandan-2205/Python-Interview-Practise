# Day 3: Decorators in Python
# Topics: Function Decorators, Class Decorators, Timing Decorator
# This file provides a tutorial, the main task (timing decorator), and practice problems with solutions.

# Tutorial Section
# 1. Decorators: Functions that modify other functions, add functionality without changing code.
# Example:
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# say_hello()  # This will print Before, Hello!, After

# 2. Decorators with arguments: Using *args and **kwargs.
# Example:
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Args:", args)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

# add(1, 2)  # Prints args and result

# 3. Class Decorators: Classes that act as decorators.
# Example:
class MyClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Class decorator before")
        return self.func(*args, **kwargs)

@MyClassDecorator
def greet(name):
    print(f"Hello {name}")

# greet("Alice")

# Main Task: Write a decorator for timing function execution
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"

# slow_function()  # Will print the timing

# Practice Problems with Solutions

# Problem 1: Create a decorator that logs function calls.
# Solution:
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logging_decorator
def multiply(a, b):
    return a * b

# multiply(3, 4)

# Problem 2: Decorator that caches results (memoization).
# Solution:
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))  # Cached for efficiency

# Problem 3: Class decorator that counts function calls.
# Solution:
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CallCounter
def test_func():
    print("Test function called")

# test_func()
# test_func()

# Problem 4: Decorator with parameters (e.g., repeat function n times).
# Solution:
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

# say_hi()  # Prints Hi! three times

# Problem 5: Decorator that checks if user is authenticated (simulated).
# Solution:
def authenticate(func):
    def wrapper(*args, **kwargs):
        # Simulate authentication check
        authenticated = True  # In real code, check session/token
        if not authenticated:
            raise PermissionError("Not authenticated")
        return func(*args, **kwargs)
    return wrapper

@authenticate
def secure_function():
    print("Secure function executed")

# secure_function()