str1 = input("문자열 입력:")

str2 = []

str2.append(str1[0])


for i in range(1,len(str1)):

    count = 0

    for j in range(0,i):

        if str1[i] == str1[j]:

            count = count + 1

    if count <1:

        str2.append(str1[i])


for m in range(0,len(str2)):

    count2 = 0

    for n in range(0,len(str1)):

        if str2[m] == str1[n]:

            count2 = count2 + 1

    print(str2[m],"의 개수",count2)

    
