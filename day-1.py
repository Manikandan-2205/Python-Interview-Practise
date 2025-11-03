# Day 1: Advanced Data Types in Python
# Topics: tuple, set, dict comprehension, namedtuple, Counter
# This file provides a tutorial, the main task (log analyzer using Counter), and practice problems with solutions.

# Tutorial Section
# 1. Tuple: Immutable sequences, can be used as keys in dicts, faster than lists.
# Example:
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)

# 2. Set: Unordered collection of unique elements, fast membership tests.
# Example:
my_set = {1, 2, 3, 3}  # Duplicates removed
print("Set:", my_set)

# 3. Dict Comprehension: Create dicts from iterables.
# Example:
squares = {x: x**2 for x in range(5)}
print("Dict Comprehension:", squares)

# 4. Namedtuple: Like tuples but with named fields, from collections module.
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("Namedtuple:", p.x, p.y)

# 5. Counter: Counts hashable objects, useful for frequency analysis.
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c'])
print("Counter:", counts)

# Main Task: Rebuild a small log analyzer using collections.Counter
# Assume we have log lines like "IP: 192.168.1.1", "IP: 192.168.1.2", etc.
# We need to count occurrences of each IP.

def analyze_logs(log_lines):
    ips = [line.split(": ")[1] for line in log_lines if line.startswith("IP:")]
    return Counter(ips)

# Example usage:
log_lines = [
    "IP: 192.168.1.1",
    "IP: 192.168.1.2",
    "IP: 192.168.1.1",
    "IP: 10.0.0.1",
    "IP: 192.168.1.1"
]
result = analyze_logs(log_lines)
print("Log Analysis Result:", result)

# Practice Problems with Solutions

# Problem 1: Create a tuple from a list and demonstrate immutability.
# Solution:
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("Tuple from list:", my_tuple)
# Immutability: my_tuple[0] = 4  # This would raise TypeError

# Problem 2: Use set to remove duplicates from a list.
# Solution:
dupe_list = [1, 2, 2, 3, 3, 3]
unique_set = set(dupe_list)
print("Unique set:", unique_set)

# Problem 3: Dict comprehension to create a dict of word lengths.
# Solution:
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)

# Problem 4: Use namedtuple for a simple Person class.
# Solution:
Person = namedtuple('Person', ['name', 'age'])
person = Person('Alice', 30)
print("Person:", person.name, person.age)

# Problem 5: Use Counter to find most common elements in a list.
# Solution:
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(items)
print("Most common:", counter.most_common(2))