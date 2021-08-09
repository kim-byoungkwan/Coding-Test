list1 = [14,5,2,3,20,4,23]

max1 = list1[0]
min1 = list1[0]

for i in list1:

    if i > max1:

        max1 = i

    if i < min1:

        min1 = i

print("최대값:",max1)
print("최소값:",min1)

