def solution(floors):

    box = []

    for i in range(1,len(floors)):

        box.append(abs(floors[i-1]-floors[i]))

    result = sum(box)

    return result


floors = [1,2,5,4,2]

print(solution(floors))
