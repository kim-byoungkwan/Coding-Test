n = int(input())

dict = {}

for i in range(n):

    a,b = input().split()

    dict[b] = dict.get(b,[]) + [a]


print(dict)



