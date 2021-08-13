word_box = list(input().split())

stack = []

print(word_box)

for i in word_box:

    for j in range(len(i)):

        if i[j] == "<":

           stack = word_box.pop(0)

           if

