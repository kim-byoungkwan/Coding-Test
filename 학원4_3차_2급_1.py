###.1

def solution(n,scores):

    scores_rank = sorted(scores,reverse=True)

    for rank,value in enumerate(scores_rank):

        if scores[n] == value:

            result = rank+1

    return result


scores = [20,60,98,59]

n = 3

print(solution(n,scores))


###.sol

def func_a(scores,score):

    rank = 1

    for s in scores:

        if s == score:

            return rank

        rank += 1

    return 0

def func_b(arr):

    arr.sort(reverse=True)

def func_c(arr,n):

    return arr[n]

def solution(scores,n):

    s = func_c(scores,n)

    func_b(scores)

    answer = func_a(scores,s)

    return answer


scores = [20,60,98,59]

n = 3

ret = solution(scores,n)

print(ret)








