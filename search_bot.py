from search_functions import*

filename = "puzzle.txt"
seperater = "\t"
f = open(filename, "r")
data = f.read()
f.close()

#create letter list
row_list = data.split("\n")
letter_list = []
for i in row_list:
    b_list = i.split(seperater)
    letter_list = letter_list + b_list

#determine width and height

height = len(row_list)
width = len(row_list[0].split(seperater))
directions = [-width -1, -width, -width +1, -1, 1, width -1, width, width + 1]



target_word = "JON"
current_letter = 0
target_word_list = []


first_letter = []

for i in range(len(letter_list)):
    if letter_list[i] == target_word[0]:
        first_letter.append(i)

for i in first_letter:
    x = 0 
    blist = [i + directions[0], i + directions[1], i + directions[2], i + directions[3], i + directions[4], i + directions[5], i + directions[6], i + directions[7]]

    for j in blist:
        if letter_list[j] == target_word[1]:
            target_word_list.append((i, x))
        x += 1
    


for beep in target_word_list:
    word_code = [beep[0]]
    for i in range(len(target_word)-1):
        word_code.append(word_code[-1] + directions[beep[1]])
    word = ""
    x = 0
    for i in word_code:
        word += letter_list[word_code[x]]
        x += 1
    if word == target_word:
        print(word_code)

    

