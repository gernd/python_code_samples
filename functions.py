# function related sample code

# simple function that receives one argument and returns argument * 2

# style guides described by https://www.python.org/dev/peps/pep-0008/:
# * 4 space indentation
# * 4 wrap lines so they do not exceed 79 characters
# * when possible, put comments on a line of their own

# Docstring format is described here: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings

def my_function(arg):
    """  This function receives one argument and doubles it
    :param arg: The argument that should be multiplied by two
    :return: The provided argument *
    """
    return arg * 2

double_of_five = my_function(5)
print("Double of 5 is " + str(double_of_five))

print(my_function.__doc__) # print the function's documentation
