###.1

# standard = []
#
# new_box = []
#
# for i in range(1,100):
#
#     standard.append(i)
#
# box = [111,123,135,147,159,222,234,246,258,333,345,357,369,444,456,468,555,567,579,666,678,777,789,888,999,210,321,432,420,543,531,654,642,630,765,753,741,876,864,852,840,987,975,963,951]
#
# for j in box:
#
#     standard.append(j)
#
#
# N = int(input())
#
# for m in range(1,N+1):
#
#     new_box.append(m)
#
# count = 0
#
#
# for i in new_box:
#
#     if i in standard:
#
#         count += 1
#
# print(count)
#
#
#
#
# print(list(str(99)))


###.2

N = int(input())

count_han = 0

for i in range(1,N+1):

    number = list(map(int,str(i)))

    if i < 100:

        count_han += 1

    else:

        if number[0]-number[1] == number[1]-number[2]:

            count_han += 1

        else:

            continue

print(count_han)