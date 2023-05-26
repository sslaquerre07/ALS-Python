'''Create a system that sorts any amount of words in alphabetical order (assume all lowercase)'''

word_list = []
word = input("Please enter the first word to be in your list!: ")
word_list.append(word)

while word != 'quit':
    word = str(input("Please enter a lowercase word to enter sort alphabetically with previous, or quit to exit: "))
    if word != 'quit':
        word_list.append(word)
        word_list.sort()
    else:
        continue

print(word_list)