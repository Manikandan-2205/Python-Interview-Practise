# Day 2: Iterators & Generators in Python
# Topics: Iterators, Generators, Custom Iterator
# This file provides a tutorial, the main task (custom iterator for large files), and practice problems with solutions.

# Tutorial Section
# 1. Iterators: Objects that implement __iter__ and __next__, allow iteration over data.
# Example:
my_list = [1, 2, 3]
my_iter = iter(my_list)
print("Iterator next:", next(my_iter))

# 2. Generators: Functions that yield values, memory efficient for large data.
# Example:
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print("Generator next:", next(gen))

# 3. Generator Expressions: Like list comprehensions but for generators.
# Example:
gen_expr = (x**2 for x in range(5))
print("Generator expression:", list(gen_expr))

# Main Task: Build a custom iterator that reads large files line-by-line
# This iterator should handle large files without loading everything into memory.

class FileIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __next__(self):
        if self.file is None:
            raise StopIteration
        line = self.file.readline()
        if line == '':
            self.file.close()
            raise StopIteration
        return line.strip()

# Example usage:
# Assuming 'large_file.txt' exists with some lines.
# For demo, we'll create a small file in code, but in practice, use a large file.
# with open('large_file.txt', 'w') as f:
#     for i in range(10):
#         f.write(f"Line {i}\n")

# file_iter = FileIterator('large_file.txt')
# for line in file_iter:
#     print(line)

# Practice Problems with Solutions

# Problem 1: Create a simple iterator class for a range.
# Solution:
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Usage:
# my_range = MyRange(0, 5)
# for num in my_range:
#     print(num)

# Problem 2: Write a generator function to generate Fibonacci numbers.
# Solution:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage:
# fib_gen = fibonacci(10)
# print(list(fib_gen))

# Problem 3: Use generator expression to filter even numbers.
# Solution:
numbers = [1, 2, 3, 4, 5, 6]
even_gen = (x for x in numbers if x % 2 == 0)
print("Even numbers:", list(even_gen))

# Problem 4: Create an iterator that yields lines from a string (simulating file).
# Solution:
class StringIterator:
    def __init__(self, text):
        self.lines = text.split('\n')
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lines):
            raise StopIteration
        line = self.lines[self.index]
        self.index += 1
        return line

# Usage:
# text = "Line 1\nLine 2\nLine 3"
# str_iter = StringIterator(text)
# for line in str_iter:
#     print(line)

# Problem 5: Generator for prime numbers up to n.
# Solution:
def primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(2, n + 1):
        if is_prime(i):
            yield i

# Usage:
# prime_gen = primes(20)
# print(list(prime_gen))