###.1

# num_A = int(input())
#
# box_A = list(map(int,input().split()))
#
# num_B = int(input())
#
# box_B = list(map(int,input().split()))
#
# for i in box_B:
#
#     if i in box_A:
#
#         print(1)
#
#     else:
#
#         print(0)


###.2

# def solution(num_A,box_A,num_B,box_B):
#
#     box_A.sort()
#
#     for i in box_B:
#
#         result = 0
#
#         start = box_A[0]
#
#         end = box_A[-1]
#
#         while start <= end:
#
#             mid = (start + end) // 2
#
#             if i > mid:
#
#                 start = mid + 1
#
#             elif i < mid:
#
#                 end = mid - 1
#
#             else:
#
#                 result = 1
#
#                 print(result)
#
#                 break
#
#         if result == 1:
#
#             continue
#
#         else:
#
#             print(result)
#
#
# num_A = 5
#
# box_A = [4,1,5,2,3]
#
# num_B = 5
#
# box_B = [1,3,7,9,5]
#
#
# solution(num_A,box_A,num_B,box_B)



###.3

# def binary_search(box_A,num):
#
#     box_A.sort()
#
#     start = 0
#
#     end = len(box_A)-1
#
#     while start <= end:
#
#         mid = (start + end)//2
#
#         if num > box_A[mid]:
#
#             start = mid +1
#
#         elif num < box_A[mid]:
#
#             end = mid -1
#
#         else:
#
#             return 1
#
#     return 0
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
#
# for i in box_B:
#
#     print(binary_search(box_A,i))


###.4

def binary_search(box_A,box_B):

    box_temp = []

    box_A.sort()

    for i in box_B:

        start = 0

        end = len(box_A) - 1

        result = 0

        while start <= end:

            mid = (start + end)//2

            if i > box_A[mid]:

                start = mid + 1

            elif i < box_A[mid]:

                end = mid - 1

            else:

                result = 1

                box_temp.append(result)

                break

        if result == 1:

            continue

        else:

            box_temp.append(result)

    return box_temp


num_A = int(input())

box_A = list(map(int,input().split()))

num_B = int(input())

box_B = list(map(int,input().split()))



for i in binary_search(box_A,box_B):

    print(i)
































