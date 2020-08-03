from word_finder import*
word_list = input("What words are we looking for (please seperate words by a space): ").split(" ")

for i in word_list:
    if find_word(i) == None:
        print("This word is not in the puzzle")
    else:
        word_nums = find_word(i)[0]
        statement = find_word(i)[1]
        for j in word_nums:
            letter_list[j] = "*"
        print(statement)

solved_file = open("solved_puzzle.txt","w")
letter_list_string = ("\t".join(letter_list))
x = 0 
y = width*2

for i in range(height):
    solved_file.write(letter_list_string[x:y])
    solved_file.write("\n")
    x = y 
    y += width*2

solved_file.close()

print("The solved puzzle has been stored in 'solved_puzzle.txt'")