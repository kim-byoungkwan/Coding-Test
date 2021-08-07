n = 5

first = [[None]*15 for i in range(n)]

final = []

word_len_total = 0

for i in range(5):

    word = input()

    word_len = len(word)

    for j in range(word_len):

        first[i][j] = word[j]

    word_len_total = word_len_total + word_len


while True:

    for m in range(5):

        if first[m][0] != None:

            final.append(first[m].pop(0))

        else:

            continue

    if len(final) == word_len_total:

        break

for i in range(len(final)):

    print(final[i],end='')






















