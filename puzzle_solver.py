from word_finder import*
word_list = ["lorem", "ipsum", "dolor"]

for i in word_list:
    word_nums = find_word(i)[0]
    statement = find_word(i)[1]
    for j in word_nums:
        letter_list[j] = "*"
    print(statement)

solved_file = open("solved_puzzle.md","w") 
letter_list_string = ("\t".join(letter_list))
x = 0 
y = width*2

for i in range(height):
    solved_file.write(letter_list_string[x:y])
    solved_file.write("\n")
    x = y 
    y += width*2

solved_file.close()