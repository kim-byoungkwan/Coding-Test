def solution(left_gloves,right_gloves):

    count = 0

    left_gloves.sort()

    right_gloves.sort()

    for i in left_gloves:

        if i in right_gloves:

            index = right_gloves.index(i)

            right_gloves.pop(index)

            count = count + 1

    return count

left_gloves = [2,1,2,2,4]

right_gloves = [1,2,2,4,4,7]


print(solution(left_gloves,right_gloves))