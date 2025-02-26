b = [1, 2, 1, 4, 5, 7, 5, 7, 8, 9, 10, 5]
def unique_list(input_list):
    result = []
    for item in b:
        if item not in result:
            result.append(item)
    return result
print(unique_list(b))