T = int(input())

box = []

for i in range(T):

    box.append(int(input()))

print(max(box))

index_max = box.index(max(box))

print(index_max+1)