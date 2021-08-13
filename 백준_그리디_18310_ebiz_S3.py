# ###.1 처음 완전탐색방식
#
# N = int(input())
#
# position = list(map(int,input().split()))
#
# selection = 0
#
# box = []
#
# final = []
#
# for i in position:
#
#     selection = i
#
#     for j in position:
#
#         box.append(abs(selection - j))
#
#     final.append(sum(box))
#
#     box = []
#
# index = final.index(min(final))
#
# print(position[index])


###.2

# N = int(input())
#
# position = list(map(int,input().split()))
#
# middle = sum(position)/len(position)
#
# box = []
#
# for i in range(N):
#
#     box.append(abs(position[i] - middle))
#
# index = box.index(min(box))
#
# print(position[index])


###.3

def midvalue_low(list):

    return [i for i in sorted(list)][len(list) // 2 if len(list) %2 != 0 else (len(list) // 2)-1]

N = int(input())

position = list(map(int,input().split()))

print(midvalue_low(position))



