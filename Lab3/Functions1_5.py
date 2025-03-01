from itertools import permutations

def print_permutations():
    user_input = input("Enter a string: ")
    perm_list = permutations(user_input)
    for perm in perm_list:
        print("".join(perm))

print_permutations()
