str1 = input("문장 입력:")

ch = input("개수를 셀 알파벳 입력:")

count = 0

for i in str1:

    if i == ch:

        count = count + 1

print(count)

