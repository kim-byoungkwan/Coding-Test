str1 = input("영어단어입력: ")

str2 = ""

length = len(str1)

for i in range(length):

    str2 = str2 + str1[length-1-i]

print(str2)