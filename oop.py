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


# class vs instance variables

class MyClass:

    # class variable shared by all instances
    common_attribute = "Common to all instances"

    def __init__(self, specific):
        """Constructor with a parameter for a specific attribute"""
        # instance variable
        self.instance_attribute = specific


first_instance = MyClass("attribute of first class")
second_instance = MyClass("attribute of second class")

print("Common attribute aka class variable of first instance: " + first_instance.common_attribute)
print("Common attribute aka class variable of second instance: " + second_instance.common_attribute)
print("Specific attribute aka instance variable of first instance: " + first_instance.instance_attribute)
print("Specific attribute aka instance variable of second instance: " + second_instance.instance_attribute)
