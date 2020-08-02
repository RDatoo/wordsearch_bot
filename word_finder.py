
filename = "puzzle.txt"
f = open(filename, "r")
data = f.read()
f.close()

#create letter list
seperater = "\t"
row_list = data.split("\n")
letter_list = []
for i in row_list:
    b_list = i.split(seperater)
    letter_list = letter_list + b_list

#determine width, height, and edges
height = len(row_list)
width = len(row_list[0].split(seperater))
edges = []
for i in range(len(letter_list)):
    if i < width or i%width == 0 or i%width == width-1 or i > len(letter_list)-width-1:
        edges.append(i)

directions = [-width -1, -width, -width +1, -1, 1, width -1, width, width + 1]

#find word function
def find_word(tword):

    target_word = tword.upper()
    target_word_list = []

    first_letter = []
    for i in range(len(letter_list)):
        if letter_list[i] == target_word[0]:
            first_letter.append(i)

    for i in first_letter:
        x = 0
        y = 0
        second_letter = [i + directions[0],
                        i + directions[1],
                        i + directions[2],
                        i + directions[3],
                        i + directions[4],
                        i + directions[5],
                        i + directions[6],
                        i + directions[7]]

        for b in second_letter:
            if b > len(letter_list)-1:
                second_letter[y] = 1
            y += 1

        for j in second_letter:
            if letter_list[j] == target_word[1]:
                target_word_list.append((i, x))
            x += 1

    for pair in target_word_list:
        word_code = [pair[0]]
        for i in range(len(target_word)-1):
            word_code.append(word_code[-1] + directions[pair[1]])
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
        if word == target_word and out_of_bounds == False:
            return[word_code, f"word starts in column {word_code[0]%width +1} row {word_code[0]//width + 1} and ends at column {word_code[-1]%width +1} row {word_code[-1]//width +1}"]


