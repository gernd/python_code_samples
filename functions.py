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

print('Docs for myfunction:')
print(my_function.__doc__) # print the function's documentation
