import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

position = sorted(list(map(int,sys.stdin.readline().split())))

box = []

if K >= N:

    print(0)

else:

    for i in range(1,len(position)):

        box.append(position[i] - position[i-1])

    box.sort(reverse=True)

    for i in range(K-1):

        box.pop(0)

    print(sum(box))

