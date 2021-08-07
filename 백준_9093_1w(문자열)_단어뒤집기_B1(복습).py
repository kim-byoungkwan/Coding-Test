n = int(input())

for i in range(n):

    string=input()

    string = string + " "

    stack = []

    stack_final = []

    for j in string:

        if j !=" ":

            stack.append(j)

        else:

            while stack:

                stack_final.append(stack.pop())

            stack_final.append(" ")


    for m in range(len(stack_final)):

        print(stack_final[m],end='')











