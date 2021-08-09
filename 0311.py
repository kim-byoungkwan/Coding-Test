array = input("공백을 구분자로 하는 숫자배열 입력:").split()

print(array)

max1 = int(array[0])

min1 = int(array[0])

for i in array:

    if int(i) > max1:

        max1 = int(i)

    if int(i) < min1:

        min1 = int(i)

print("최대값:",max1)
print("최소값:",min1)

