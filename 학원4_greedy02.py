# 큰수의 법칙

N,M,K = map(int,input().split())

box= list(map(int,input().split()))

box.sort()

first = box[N-1]

second = box[N-2]

result = 0

while True:

    for i in range(K):

        if M == 0:

            break

        else:

            result = result + first

            M = M -1

    if M == 0:

        break

    else:

        result = result + second

        M = M -1

print(result)

