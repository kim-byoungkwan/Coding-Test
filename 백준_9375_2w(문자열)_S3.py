
big_n = int(input())

for _ in range(big_n):

    n = int(input())

    dict = {}

    num = 1

    for i in range(n):

        a,b = input().split()

        dict[b] = dict.get(b,[]) + [a]

    for a in list(dict.keys()):

        dict[a] = dict.get(a,[]) + [""]

    value_all = dict.values()

    value_all = list(value_all)

    value_count = []


    for b in range(len(value_all)):

        value_count.append(len(value_all[b]))

    for c in value_count:

        num = num * c

    print(num-1)


