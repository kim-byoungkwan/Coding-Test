num_student = int(input())

num_tofind = int(input())

num_founded = int(input())



index_all = [i for i in range(num_student)]

queue_full = []

queue_zero = []

queue_one = []


num_str =''


for i in range(2,num_tofind):

    num_str = num_str + "0101"+"0"*i+"1"*i


for i in num_str:

    queue_full.append(i)

queue_full = list(map(int,queue_full))

count_full = 0


while queue_full:

    count_full = count_full + 1

    if num_founded == 0:

        value_pop = queue_full.pop(0)

        if value_pop == 0:

            queue_zero.append(value_pop)

        else:

            continue

    else:

        value_pop = queue_full.pop(0)














