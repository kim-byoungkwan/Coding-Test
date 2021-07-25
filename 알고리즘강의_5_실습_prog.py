def solution(L, x, l, u):

    if l > u:

        return -1

    mid = (l + u) // 2

    if x == L[mid]:

        return mid

    elif x < L[mid]:

        return solution(L,x,l,u-1)

    else:

        return solution(L,x,l+1,u)




