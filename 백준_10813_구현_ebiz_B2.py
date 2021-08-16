N,M = map(int,input().split())

box = [i+1 for i in range(N)]

for _ in range(M):

    a,b = map(int,input().split())

    temp = box[b-1]

    box[b-1] = box[a-1]

    box[a-1] = temp

for i in range(N):

    print(box[i],end=' ')
