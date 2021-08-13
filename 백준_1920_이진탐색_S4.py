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

def solution(num_A,box_A,num_B,box_B):

    box_A.sort()

    for i in box_B:

        result = 0

        start = box_A[0]

        end = box_A[-1]

        while start <= end:

            mid = (start + end) // 2

            if i > mid:

                start = mid + 1

            elif i < mid:

                end = mid - 1

            else:

                result = 1

                print(result)

                break

        if result == 1:

            continue

        else:

            print(result)


num_A = 5

box_A = [4,1,5,2,3]

num_B = 5

box_B = [1,3,7,9,5]


solution(num_A,box_A,num_B,box_B)


















