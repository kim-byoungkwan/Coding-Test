###.1

def solution(data):

    count = 0

    data.sort()

    average = sum(data)/len(data)

    for i in data:

        if i <= average:

            count += 1

        else:

            continue

    return count


data = [1,2,3,4,5,6,7,8,9,10]


print(solution(data))