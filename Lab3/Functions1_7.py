nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]

def has_33(arg):
    for i in range(len(arg)-1):
        if arg[i]==3 and arg[i+1]==3:
            return True
    return False

print(has_33(nums))