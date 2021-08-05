n = 5

box = []

answer = ''

for i in range(n):

    s = list(input())

    box.append(s)

print(box)



while len(box) != 0:

    for i in range(len(box)):

        s = box[i].pop(0)

        answer = answer + s

        if len(box[i]) == 0:

            box.pop(i)










    #
    # box[0][0]
    # box[1][0]
    # box[2][0]
    # box[3][0]
    # box[4][0]
    #
    # box[0][1]
    # box[1][1]
    # box[2][1]
    #
    #
    # box[0][5]
    # box[1][5] -> 존재 x
    # box[2][5] -> 존재 x
    # box[3][5]
    # box[4][5]
    #
    #



