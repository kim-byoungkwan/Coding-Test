number_str = input()

share = len(number_str) //2

part_first = []

part_second = []

for i in range(share):

     part_first.append(number_str[i])

for j in range(share,2*share):

     part_second.append(number_str[j])


part_first = map(int,part_first)

part_second = map(int,part_second)


if sum(part_first) == sum(part_second):

    print("LUCKY")

else:

    print("READY")

