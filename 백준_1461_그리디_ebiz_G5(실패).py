###.1

# N,M = map(int,input().split())
#
# position = list(map(int,input().split()))
#
# box_minus = []
#
# box_plus = []
#
# result = []
#
# for i in position:
#
#     if i < 0:
#
#         box_minus.append(i)
#
#     else:
#
#         box_plus.append(i)
#
# box_minus.sort(reverse=True)
#
# box_plus.sort()
#
# max_plus = abs(box_plus.pop())
#
# max_minus = abs(box_minus.pop())
#
#
# if max_plus < max_minus:
#
#
#     if len(box_minus) % M == 0:
#
#         share = len(box_minus) // M
#
#         for i in range(1,share+1):
#
#             if i == share:
#
#                 result.append(abs(box_minus[(i * M)-1]))
#
#             else:
#
#                 result.append(abs(box_minus[(i * M) -1])*2)
#
#
#     else:
#
#         share = len(box_minus) // M
#
#         result.append(abs(box_minus[0])*2)
#
#         for i in range(1,share+1):
#
#             if i == share:
#
#                 result.append(abs(box_minus[(i * M)]))
#
#             else:
#
#                 result.append(abs(box_minus[(i * M)]*2))
#
#
#     if len(box_plus) % M == 0:
#
#         share = len(box_plus) // M
#
#         for i in range(1, share+1):
#
#             if i == share:
#
#                 result.append(abs(box_plus[i * M - 1] * 2))
#
#             else:
#
#                 result.append(abs(box_plus[i * M - 1]) * 2)
#
#
#     else:
#
#         share = len(box_plus) // M
#
#         result.append(abs(box_plus[0]) * 2)
#
#         for i in range(1, share+1):
#
#             if i == share:
#
#                 result.append(abs(box_plus[i * M -1] * 2))
#
#             else:
#
#                 result.append(abs(box_plus[i * M - 1] * 2))
#
#
# else:
#
#     if len(box_plus) % M == 0:
#
#         share = len(box_plus) // M
#
#         for i in range(1, share + 1):
#
#             if i == share:
#
#                 result.append(abs(box_plus[i * M - 1]))
#
#             else:
#
#                 result.append(abs(box_plus[i * M - 1]) * 2)
#
#
#     else:
#
#         share = len(box_plus) // M
#
#         result.append(abs(box_plus[0]) * 2)
#
#         for i in range(1, share + 1):
#
#             if i == share:
#
#                 result.append(abs(box_plus[i * M - 1] * 2))
#
#             else:
#
#                 result.append(abs(box_plus[i * M - 1] * 2))
#
#
#
#     if len(box_minus) % M == 0:
#
#         share = len(box_minus) // M
#
#         for i in range(1, share + 1):
#
#             if i == share:
#
#                 result.append(abs(box_minus[(i * M) - 1] * 2))
#
#             else:
#
#                 result.append(abs(box_minus[(i * M) - 1]) * 2)
#
#
#     else:
#
#         share = len(box_minus) // M
#
#         result.append(abs(box_minus[0]) * 2)
#
#         for i in range(1, share + 1):
#
#             if i == share:
#
#                 result.append(abs(box_minus[(i * M) *2]))
#
#             else:
#
#                 result.append(abs(box_minus[(i * M)] * 2))
#
# print(result)
#
# print(sum(result))
#

###.2

N,M = map(int,input().split())

position = list(map(int,input().split()))

box_minus = []

box_plus = []

result = []

for i in position:

    if i < 0:

        box_minus.append(i)

    else:

        box_plus.append(i)

box_minus.sort(reverse=True)

box_plus.sort()

max_plus = abs(box_plus.pop())

max_minus = abs(box_minus.pop())



if max_plus < max_minus:

    max_list = max_minus

    min_list = max_plus

else:

    max_list = max_plus

    min_list = max_minus




if len(max_list) % M ==0 and len(min_list) % M ==0:

    for i in range(1,len(max_list)+1):

        if i == len(max_list):


elif len(max_list) % M ==0 and len(min_list) % M !=0:


elif len(max_list) % M != 0 and len(min_list) % M ==0:


else:



###.3

































