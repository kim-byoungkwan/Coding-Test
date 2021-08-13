list = [4,2,3,8,7,1]


for i in range(0,len(list)):

    for j in range(0,len(list)-1):

        if list[j] > list[j+1]:

            temp = list[j]

            list[j] = list[j+1]

            list[j+1] = temp

print(list)


