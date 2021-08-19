N = int(input())

arr = []

dict = {}

count = 0

for i in range(N-1):

    people_W_T = list(map(int, input().split()))

    arr.append(people_W_T)

    for j in range(i+1,N-1):

        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:

            count = count + 1

            dict[i] = dict.get(i,0) + count

        else:

            continue


print(dict)





