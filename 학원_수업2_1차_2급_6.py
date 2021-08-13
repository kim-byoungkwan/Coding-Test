###.1

def solution(number):

    count = 0

    for i in range(number):

        i = str(i)

        if i.count("3"):

            count = count + i.count("3")

        if i.count("6"):

            count = count + i.count("6")

        if i.count("9"):

            count = count + i.count("9")

    return count

num = 40

print(solution(num))

