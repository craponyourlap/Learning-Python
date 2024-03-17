####################################################
## 6.2 Multiple Inheritance
####################################################

# Another class definition
# bat.py
class Bat:

    species = 'Baty'

    def __init__(self, can_fly = True):
        self.fly = can_fly

    # This class also has a say method
    def say(self, msg):
        msg = "... ... ..."
        return msg

    # And its own method as well
    def sonar(self):
        return '))) ... ((('

if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)

# And yet another class definition that inherits from Superhero and Bat
# superhero.py

# Define Batman as a child that inherits from both Superhero and Bat

# Typically to inherit attributes you have to call super:
# super(Batman, self).__init__(*args, **kwargs)
# However we are dealing with multiple inheritance here, and super()
# only works with the next base class in the MRO list.
# So instead we explicitly call __init__ for all ancestors.
# The use of *args and **kwargs allows for a clean way to pass
# arguments, with each parent "peeling a layer of the onion".
# override the value for the name attribute




# The Method Resolution Order
# => (<class '__main__.Batman'>,
# => <class 'superhero.Superhero'>,
# => <class 'human.Human'>,
# => <class 'bat.Bat'>, <class 'object'>)

# Calls parent method but uses its own class attribute
# => Superhuman

# Calls overridden method
# => nan nan nan nan nan batman!

# Calls method from Human, because inheritance order matters
# => Sad Affleck: I agree

# Call method that exists only in 2nd ancestor
# => ))) ... (((

# Inherited class attribute
# => 100

# Inherited attribute from 2nd ancestor whose default value was overridden.
# => Can I fly? False



####################################################
## 7. Advanced
####################################################

# Generators help you make lazy code.

# Generators are memory-efficient because they only load the data needed to
# process the next value in the iterable. This allows them to perform
# operations on otherwise prohibitively large value ranges.
# NOTE: `range` replaces `xrange` in Python 3.
# `range` is a generator.

# Just as you can create a list comprehension, you can create generator
# comprehensions as well.
# prints -1 -2 -3 -4 -5 to console/terminal

# You can also cast a generator comprehension directly to a list.
# => [-1, -2, -3, -4, -5]


# Decorators are a form of syntactic sugar.
# They make code easier to read while accomplishing clunky syntax.

# Wrappers are one type of decorator.
# They're really useful for adding logging to existing functions without needing to modify them.


# equivalent:
# def my_function(x,y):
#   return x+y
# my_function = log_function(my_function)
# The decorator @log_function tells us as we begin reading the function definition
# for my_function that this function will be wrapped with log_function.
# When function definitions are long, it can be hard to parse the non-decorated
# assignment at the end of the definition.

# => "Entering function my_function"
# => "3"
# => "Exiting function my_function"

# But there's a problem.
# What happens if we try to get some information about my_function?

# => 'wrapper'
# => 0. The argcount is 0 because both arguments in wrapper()'s signature are optional.

# Because our decorator is equivalent to my_function = log_function(my_function)
# we've replaced information about my_function with information from wrapper

# Fix this using functools


# this ensures docstring, function name, arguments list, etc. are all copied
# to the wrapped function - instead of being replaced with wrapper's info


# => "Entering function my_function"
# => "3"
# => "Exiting function my_function"

# => 'my_function'
# => 2