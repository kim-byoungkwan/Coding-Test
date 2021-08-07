word = input()

box = []

for i in range(len(word)):

     box.append(word[i:])

box.sort()

for i in range(len(box)):

     print(box[i])