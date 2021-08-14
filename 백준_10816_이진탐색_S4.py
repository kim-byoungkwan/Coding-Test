###.1

# def binary_search(box_B,box_A):
#
#     dict = {}
#
#     for m in box_B:
#
#         dict[m] = dict.get(m, 0)
#
#     box_B.sort()
#
#     for i in box_A:
#
#         start = 0
#
#         end = len(box_B) - 1
#
#         while start <= end:
#
#             mid = (start + end) // 2
#
#             if i < box_B[mid]:
#
#                 end = mid - 1
#
#             elif i > box_B[mid]:
#
#                 start = mid + 1
#
#             else:
#
#                 dict[i] = dict.get(i, 0) + 1
#
#                 break
#
#     original_value = list(dict.values())
#
#     return original_value
#
#
# num_A = int(input())
#
# box_A = list(map(int,input().split()))
#
# num_B = int(input())
#
# box_B = list(map(int,input().split()))
#
# result =" ".join(map(str,binary_search(box_B,box_A)))
#
# print(result)


###.2

# num_A = int(input())
#
# box_A = list(map(int,input().split()))
#
# num_B = int(input())
#
# box_B = list(map(int,input().split()))
#
# dict = {}
#
# for i in box_B:
#
#     dict[i] = dict.get(i,0)
#
# for j in box_A:
#
#     if j in dict:
#
#         dict[j] = dict.get(j) +1
#
#     else:
#
#         continue
#
#
# result = dict.values()
#
# for m in result:
#
#     print(m,end=' ')

###.3

num_A = int(input())

box_A = list(map(int,input().split()))

dict = {}

for i in box_A:

    if i in dict:

        dict[i] = dict[i] + 1

    else:

        dict[i] = 1


num_B = int(input())

box_B = list(map(int,input().split()))


for j in box_B:

    if j in dict:

        print(dict[j], end=' ')

    else:

        print(0,end=' ')



