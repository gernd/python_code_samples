# function related sample code

# simple function that receives one argument and returns argument * 2

# style guides described by https://www.python.org/dev/peps/pep-0008/:
# * 4 space indentation
# * 4 wrap lines so they do not exceed 79 characters
# * when possible, put comments on a line of their own

# Docstring format is described here: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings

# default value for the function "my_function"
arg_default_value = 3
def my_function(arg=arg_default_value): # default value for arg is evaluated when function is defined -> 3
    """  This function receives one argument and doubles it
    :param arg: The argument that should be multiplied by two
    :return: The provided argument *
    """
    return arg * 2

# this doesn't have any effect on the default value for arg in my_function
arg_default_value = 10

double_of_five = my_function(5)
print("Double of 5 is " + str(double_of_five))

double_of_three = my_function()
print("Double of 3 is " + str(double_of_three))


# function are first class citizens
print("my_function: " + str(my_function))

print('Docs for myfunction:')
print(my_function.__doc__) # print the function's documentation

# in general function parameters are passed by object-reference

# this does not work with primitive types likes strings and ints, as there are immutable
# in this case new objects are created dynamically

def change_string(param_to_change):
    """Attempts to modify the given string"""
    param_to_change = param_to_change + "blablabla"

a = "hallo"
print('a before attempt to change it ' + a)
change_string(a)

# still prints "hallo"
print('a after attempt to change it ' + a)

# dicts, list and custom objects can be changed using their mutators

def change_my_dict(param_to_change):
    """Adds another key to the given dictionary"""
    param_to_change['key_from_method'] = 'value_from_method'

b = dict()
b['myKey'] = 'myVal'
print('b before attempt to change it ' + str(b))
change_my_dict(b)
print('b after attempt to change it ' + str(b))

# it is not possible to assign a new instance to an argument passed into a method
def assign_new_dict(dictionary):
    """Tries to assign a new (empty) dict to the variable that is given as parameter"""
    dictionary = dict()

c = dict()
c['colour'] = 'yellow'

assign_new_dict(c)

# still prints yellow
print(c['colour'])


# function annotations
# https://www.python.org/dev/peps/pep-3107/
# https://docs.python.org/3/reference/compound_stmts.html#function

# arbitrary python expressions can be associated with various parts of a function at compile time
# this does not change the semantics of a function
# can be used for third party libraries (e.g. typechecking)


def my_annotated_function(a : "string", b : "int") -> "something_else":
    pass # does nothing

print('Annotations of my function: ' + str(my_annotated_function.__annotations__))

# lambdas
# a simple add function in curried form
add = lambda x : lambda y : x + y
add_5 = add(5)
add_5_8 = add_5(8)
print(add_5_8)
