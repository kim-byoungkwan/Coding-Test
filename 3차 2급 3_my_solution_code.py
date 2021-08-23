def solution(scores):

    return (sum(scores) - max(scores) - min(scores)) // (len(scores) - 2)

scores1 = [35,28,98,34,20,50,85,74,71,7]

ret1 = solution(scores1)

print(ret1)


scores2 = [1,1,1,1,1]

ret2 = solution(scores2)

print(ret2)
