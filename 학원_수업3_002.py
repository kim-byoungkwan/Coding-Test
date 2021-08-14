T = int(input())

box = []

stack = []

que = []

for i in range(T):

    out = 0

    result = 0

    num_reverse = 0

    box_reverse = []

    num = input()

    for j in num:

        box.append(j)

    while box:

        box_reverse.append(box.pop())

    num_reverse = "".join(box_reverse)

    num_reverse = int(num_reverse)

    result = int(num) + num_reverse

    for m in str(result):

        stack.append(m)

        que.append(m)

    while stack:

        if stack.pop() == que.pop(0):

            continue

        else:

            out = "No"

    if out == "No":

        print(out)

    else:

        print("Yes")


