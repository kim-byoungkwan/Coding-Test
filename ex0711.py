str1 = "Good morning jack"

word = ""

result_str = ""

list1 = []

for i in range(0,len(str1)):

    if str1[i] != " ":

        word = word + str1[i]

        if i == len(str1)-1:

            list1.append(word)

    else:

        list1.append(word)

        word = ""

print(list1)


for m in range(0,len(list1)):

    if list1[m] == "jack":

        list1[m] = "Tom"

    if m != len(list1)-1:

        result_str = result_str + list1[m] + " "

    else:

        result_str = result_str + list1[m]

print(result_str)



