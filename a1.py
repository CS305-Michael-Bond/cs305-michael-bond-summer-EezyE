import math

# 1. Function definitions

# define a function called rectangle_area with one required parameter (width) and
# one optional parameter (height). This function should compute and return the area
# of a rectangle with the given width and height. If height is not provided, the
# function should assume that both width and height are equal and compute the area
# accordingly. Make sure to include a docstring describing this function in your
# definition below.


def rectangle_area(width, height=False):
    """
    Return the area of a rectangle

    Parameter
    ----------
    width : int64
        width in integer format.

    height : int64
        height in integer format. If not provided, defaults to value of width

    Returns
    ----------
    int64
        area of a rectangle

    """

    if height == False:
        height = width

    return width * height


# 2. lambda definitions

# Alter the statement below to assign a function value to circle_area using a
# lambda expression. The function you create should have one parameter (the
# radius of a circle) and should compute and return the circle's area. Your
# function must be correct to 5 decimal places to pass the tests.
circle_area = lambda r: math.pi * r ** 2  # TODO: replace None with your lambda


# 3. Collections / Comprehensions
# part 1: use a comprehension to create a list of the first 10 perfect squares
# (starting with 1). Then convert this list to a tuple and assign it to
# the variable perfect_squares below.

# TODO: replace None with your tuple
perfect_squares = tuple([x**2 for x in range(1, 11)])

# part 2: Now convert the tuple in to a set. Use set operations to exclude
# any numbers that fall within the set 'exclusions' below and assign the
# resulting set to the variable squares_set below.

exclusions = set(range(5, 50))
# TODO: replace None with your set
squares_set = set(perfect_squares) - exclusions

# 4. generators
# Write a generator function called 'gen_squares' that generates perfect squares.
# Rather than starting with the first perfect square, generate the i-th perfect
# square, one at a time, where start <= i < stop.


def gen_squares(start, stop):
    # TODO: replace with function body for generator
    for i in range(start, stop):
        yield i**2
