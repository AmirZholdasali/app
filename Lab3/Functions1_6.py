sentence = input("Enter a sentence: ")
words_list = sentence.split()
def output(arg):
    for i in reversed(arg):
        print(i, end=' ')

output(words_list)