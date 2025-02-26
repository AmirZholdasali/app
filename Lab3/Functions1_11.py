def palindrome():
    word = input("your word to check: ")
    word_list = []
    reversed_list = []

    for i in word:
        word_list.append(i)

    for i in reversed(word_list):
        reversed_list.append(i)

    if word_list == reversed_list:
        return True
    else:
        return False
    
print(palindrome())