b = [0, 0, 7]
a = []
nums = [1,0,2,4,0,5,7]
def if_007(arg):
    for i in arg:
        if i==0 or i==7:
            a.append(i)
    if a == b:
        return True
    else:
        return False
    
print(if_007(nums))