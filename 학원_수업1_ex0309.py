word = list(input("단어를 입력하시오: "))

box = []

for i in range(len(word)):

    out = word.pop()

    box.append(out)

for i in range(len(box)):

    print(box[i],end='')





