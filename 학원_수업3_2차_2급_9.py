def solution(votes,N,K):

    dict = {}

    for i in range(1,N+1):

        dict[i] = dict.get(i,0)

    for j in votes:

        dict[j] = dict.get(j,0) + 1

    value_all = list(dict.values())

    result = value_all.count(K)

    return result


votes = [2,5,3,4,1,5,1,5,5,3]

N = 5

K = 2

print(solution(votes,N,K))


