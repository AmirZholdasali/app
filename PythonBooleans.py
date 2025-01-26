#The bool() function allows you to evaluate any value, and give you True or False in return
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))