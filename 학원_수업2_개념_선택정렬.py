list = [4,2,3,8,7,1]

for i in range(0,len(list)):

    min_i = i

    for j in range(i+1,len(list)):

        if list[min_i] > list[j]:

            min_i = j

    temp = list[min_i]

    list[min_i] = list[i]

    list[i] = temp

print(list)