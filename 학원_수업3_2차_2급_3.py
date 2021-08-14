def solution(n,m):

    box = []

    count = 0

    for i in range(n,m+1):

        if i % 2 == 0:

            box.append(i)

        else:

            continue

    for j in box:

        count = count + j**2

    return count


print(solution(4,7))
