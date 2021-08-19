N =int(input())

count = 0

arr = [None for i in range(N)]

for i in range(N):

    index,value = map(int,input().split())

    if arr[index-1] == None:

        arr[index-1] = value

    else:

        if arr[index-1] != value:

            arr[index-1] = value

            count = count + 1

        else:

            continue

print(count)


