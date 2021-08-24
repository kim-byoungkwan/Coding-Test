import sys

def change(N):

    if N == 0:

        N = 1

    else:

        N = 0

    return N


N = int(sys.stdin.readline())

state = list(map(int,sys.stdin.readline().split()))

state.insert(0,9999)

Num_student = int(sys.stdin.readline())



for i in range(Num_student):

    stu_sex = list(map(int,sys.stdin.readline().split()))

    if stu_sex[0] == 1:

        count = (len(state)-1) // stu_sex[1]

        for i in range(1,count+1):

            state[stu_sex[1]*i] = change(state[stu_sex[1]*i])

    else:

        box = []

        for i in range(1,stu_sex[1]+1):

            if state[stu_sex[1]-i] == state[stu_sex[1]+i]:

                box.append(stu_sex[1]-i)

                box.append(stu_sex[1])

                box.append(stu_sex[1]+i)

            else:

                box.append(stu_sex[1])

        box = set(box)

        for i in box:

            state[i] = change(state[i])

for k in range(1,len(state)):

    print(state[k],end=' ')

