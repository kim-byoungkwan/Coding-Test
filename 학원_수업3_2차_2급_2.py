def solution(arr):

    count_3 = 0

    count_5 = 0

    for i in arr:

        if i % 3 == 0:

            count_3 = count_3 + 1

        if i % 5 == 0:

            count_5 = count_5 + 1

    if count_3 > count_5:

        return "Three"

    elif count_3 == count_5:

        return "same"

    else:

        return "Five"

arr = [2,3,6,9,12,15,10,20,22,25]

print(solution(arr))