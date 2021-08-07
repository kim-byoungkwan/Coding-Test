A = int(input())

B = int(input())

C = int(input())

result = A*B*C

result = str(result)

store = [0]*10

for i in result:

    i = int(i)

    store[i] = store[i] + 1

for i in range(len(store)):

    print(store[i])


