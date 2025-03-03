from functools import reduce
import time
import math

#1
def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)

#2
def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

#3
def is_palindrome(s):
    return s == s[::-1]

#4
def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

#5
def all_true(tpl):
    return all(tpl)


print(multiply_list([1, 2, 3, 4]))  # 24
print(count_case("Hello World"))  # (2, 8)
print(is_palindrome("madam"))  # True
print(f"Square root: {delayed_sqrt(25100, 2123)}")  # Square root of 25100 after 2123ms
print(all_true((True, True, False)))  # False