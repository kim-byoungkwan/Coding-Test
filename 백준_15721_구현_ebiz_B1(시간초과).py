import sys




num_student = int(sys.stdin.readline())

num_tofind = int(sys.stdin.readline())

num_founded = int(sys.stdin.readline())



index_student = [i for i in range(num_student)]


queue_full = []

queue_zero = []

queue_one = []


num_str =''


for i in range(2,num_tofind+1):

    num_str = num_str + "0101"+"0"*i +"1"*i


for i in num_str:

    queue_full.append(i)

queue_full = list(map(int,queue_full))


count_full = 0

count_stack_zero = 0

count_stack_one = 0

result = 0


while queue_full:

    count_full = count_full + 1

    if num_founded == 0:

        value_pop = queue_full.pop(0)

        if value_pop == 0:

            queue_zero.append(value_pop)


        if len(queue_zero) == num_tofind:

            result = count_full-1

            break

    else:

        value_pop = queue_full.pop(0)

        if value_pop == 1:

            queue_one.append(value_pop)


        if len(queue_one) == num_tofind:

            result = count_full-1

            break


print(index_student[(result % num_student)])

