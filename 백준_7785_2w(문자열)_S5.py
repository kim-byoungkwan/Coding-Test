###.1
#
# N = int(input())
#
# log_box = []
#
# for i in range(N):
#
#     log_box.append(input())
#
# log_box = ' '.join(log_box)
#
# log_box = log_box.split(' ')
#
# log_box = [x for x in log_box if x != "enter" and x != "leave"]
#
# for i in log_box:
#
#     if log_box.count(i) % 2 == 0:
#
#         log_box = [x for x in log_box if x != i]
#
#     else:
#
#         continue
#
# log_box = set(log_box)
#
# for i in log_box:
#
#     print(i)

###.2

# N = int(input())
#
# log_box = []
#
# for i in range(N):
#
#     x,y = input().split()
#
#     log_box.append(x)
#
#
# for i in log_box:
#
#     if log_box.count(i) % 2 == 0:
#
#         log_box = [x for x in log_box if x != i]
#
#     else:
#
#         continue
#
# log_box = set(log_box)
#
# for i in log_box:
#
#     print(i)


###.3

N = int(input())

dict = {}

for i in range(N):

    x,y = input().split()

    dict[x] = y

result = [a for a,b in dict.items() if b == "enter"]

result.sort(reverse=True)

for i in result:

    print(i)








