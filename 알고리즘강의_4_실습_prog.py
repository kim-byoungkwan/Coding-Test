###.1 피보나치수열

def solution (x):

    if x <= 1:

        return x

    else:

        return solution(x-1) + solution(x-2)

