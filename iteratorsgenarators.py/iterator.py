for item in [1, 2, 3]:
    print(item)
    
    
"""   1. What is an Iterator?
An iterator is an object in Python that:

Keeps track of its current position in a sequence.

Returns elements one at a time when you call next() on it."""

"""Can be looped over using a for loop.

It must implement:

__iter__() → returns the iterator object itself.

__next__() → returns the next item, and raises StopIteration when there are no more items.
    """

# What Python actually does:
my_list = [1, 2, 3]
iterator = iter(my_list)  # Get iterator from iterable
while True:
    try:
        item = next(iterator)  # Get next item
        print(item)
    except StopIteration:  # No more items
        break    
# Iterable: object that can be iterated over
# Has __iter__() method that returns an iterator

# Iterator: object that produces items one at a time
# Has __iter__() and __next__() methods

my_list = [1, 2, 3, 4, 5]  # This is iterable
print(hasattr(my_list, '__iter__'))  # True
print(hasattr(my_list, '__next__'))  # False

my_iterator = iter(my_list)  # This is an iterator
print(hasattr(my_iterator, '__iter__'))  # True
print(hasattr(my_iterator, '__next__'))  # True

# Using the iterator manually
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3


# Creating iterators from iterables
numbers = [10, 20, 30]
num_iter = iter(numbers)

# Getting items one by one
print(next(num_iter))  # 10
print(next(num_iter))  # 20
print(next(num_iter))  # 30

# This will raise StopIteration
try:
    print(next(num_iter))
except StopIteration:
    print("No more items!")

# Using default value with next()
empty_iter = iter([])
print(next(empty_iter, "Nothing here!"))  # "Nothing here!"

#Generator Functions and yield   
"""A generator is a special kind of iterator that:

Is created using a function with yield instead of return.

Produces values one at a time, only when needed.

Does not store all values in memory at once."""

#normal function
def numbers_list():
    return [1, 2, 3]

print(numbers_list())


#Generator function (returns values one by one):
def numbers_generator():
    yield 1
    yield 2
    yield 3

gen = numbers_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen) → StopIteration

