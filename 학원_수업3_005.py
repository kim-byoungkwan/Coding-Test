num = int(input())

box = []

for i in range(1,num+1):

    if num % i == 0:

       box.append(i)

    else:

        continue

print(sum(box))


