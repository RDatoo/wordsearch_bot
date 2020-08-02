from search_bot import*
word_list = ["copy", "assignment", "small"]

for i in word_list:
    a = find_word(i)[0]
    b = find_word(i)[1]
    for j in a:
        letter_list[j] = "*"
    print(b)


file1 = open("solved.txt","w") 

e = ("\t".join(letter_list))

x = 0 
y = width*2

for i in range(height):
    file1.write(e[x:y])
    file1.write("\n")
    x = y 
    y += width*2


file1.close() 
