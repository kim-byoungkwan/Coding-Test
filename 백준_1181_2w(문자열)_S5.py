N = int(input())

word_box = []


for i in range(N):

    word_box.append(input())


word_box = set(word_box)

word_box = list(word_box)


word_box.sort(key = lambda x:(len(x),x))


for i in range(len(word_box)):

    print(word_box[i])


