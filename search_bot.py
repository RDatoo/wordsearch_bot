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


target_word = "NOB"
current_letter = 0
target_word_list = []



def adjacent_list(current_let):
    return [current_let - width -1,
            current_let - width,
            current_let - width +1,
            current_let - 1, 
            current_let + 1,
            current_let + width -1,
            current_let + width,
            current_let + width + 1]


first_letter = []

for i in range(len(letter_list)):
    if letter_list[i] == target_word[0]:
        first_letter.append(i)


for i in first_letter[0:1]:
    current_letter = i
    target_word_list.append(i)
    target_letter = target_word[1]
    for i in adjacent_list(current_letter):
        if letter_list[i] == target_letter:
            target_word_list.append(i)
            current_letter = i
            break
    
print(target_word_list)











'''

def adjacent_list(current_let):
    return [current_let - width -1,
            current_let - width,
            current_let - width +1,
            current_let - 1, 
            current_let + 1,
            current_let + width -1,
            current_let + width,
            current_let + width + 1]

for i in adjacent_list(current_letter):
    if letter_list[i] == target_letter:
        target_word_list.append(i)
        current_letter = i
        break

print(current_letter)

print(target_word_list)
    




'''