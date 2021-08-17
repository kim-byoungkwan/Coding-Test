import itertools

N = int(input())

box = []

for i in range(1,N+1):

    box.append(i)

nPr = list(itertools.permutations(box,N))

for i in nPr:

    i = list(map(str,i))

    result =" ".join(i)

    print(result)