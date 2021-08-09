numbers = [5,16,27,33,41]

print(numbers)


f_num = int(input("찾을 숫자 입력:"))

idx = -1

for i in range(0,len(numbers)):

    if numbers[i] == f_num:

        idx = i

if idx == -1:

    print("찾는 숫자가 없습니다.")

else:

    print("찾는 숫자는 %d번 배열방에 있습니다."%idx)