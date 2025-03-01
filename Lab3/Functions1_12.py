def gisto(val):
    for item in val:
        for j in range(item):
            print('*', end='')
        print()

nums = [4, 9, 2]
gisto(nums)