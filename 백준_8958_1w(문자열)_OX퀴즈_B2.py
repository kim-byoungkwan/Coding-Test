n = int(input())

stack = []

num = 0

stack_final = []


for m in range(n):

    word = input()

    for i in range(len(word)):

        if word[i] == "O":

            stack.append(word[i])

        else:

            if stack:

                for j in range(1,len(stack)+1):

                    num = num + j

                stack = []

                stack_final.append(num)

                num = 0

            else:

                continue

    if stack:

        for j in range(1, len(stack) + 1):
            num = num + j

        stack = []

        stack_final.append(num)

        num = 0

    print(sum(stack_final))

    stack_final = []










