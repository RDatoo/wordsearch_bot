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
edges = []
for i in range(len(letter_list)):
    if i < width or i%width == 0 or i%width == width-1 or i > len(letter_list)-width-1:
        edges.append(i)


target_word = "SMALL"
target_word_list = []


first_letter = []
for i in range(len(letter_list)):
    if letter_list[i] == target_word[0]:
        first_letter.append(i)

for i in first_letter:
    x = 0
    y = 0
    blist = [i + directions[0], i + directions[1], i + directions[2], i + directions[3], i + directions[4], i + directions[5], i + directions[6], i + directions[7]]
    for b in blist:
        if b > len(letter_list)-1:
            blist[y] = 1
        y += 1
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
    y = 0
    
    for j in word_code:
        if j > len(letter_list)-1:
            word_code[y] = 1
        y += 1
    
    for i in word_code:
        word += letter_list[word_code[x]]
        x += 1
    out_of_bounds = False
    for i in word_code[1:-1]:
        if i in edges:
            out_of_bounds = True
    if word == target_word:
        print(word_code)

        print("word starts in column", word_code[0]%width +1,
            "row", word_code[0]//width + 1,
            "and ends at column", word_code[-1]%width +1,
            "row", word_code[-1]//width +1)


