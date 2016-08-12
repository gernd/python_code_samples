# See https://docs.python.org/3/tutorial/classes.html Section 3

class SimpleClass:
    """Class name are CamelCase"""

    # attributes are public per default
    my_attr = 12

    def __init__(self):
        """ Constructor with instance as first param. As a
        convention the the param is always named self"""

    def my_func(self):
        return "My val is " + str(self.my_attr)


s = SimpleClass()
print(s.my_func())
print(s.my_attr)

