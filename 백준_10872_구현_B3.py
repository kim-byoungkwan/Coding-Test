###.1
#
# def factorial(N):
#
#     if N <= 1:
#
#         return 1
#
#     return N * factorial(N-1)
#
# print(factorial(10))
#

###.2

N = int(input())

result = 1

for i in range(1,N+1):

    result = result * i

print(result)