###.1 이진탐색


L = [2,3,5,6,9,11,15]

x = 6



def solution(L,x):

    lower = 0

    upper = len(L)-1


    while lower <= upper:

        middle = (lower + upper) // 2

        if L[middle] < x:

            lower = middle + 1

        elif L[middle] > x:

            upper = middle - 1

        else:

            break

    if L[middle] != x:

        middle = -1

    return middle



