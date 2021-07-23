#
# def solution(L,x):
#
#     L.append(x)
#
#     L.sort()
#
#     return L
#
#
# print(solution([20,37,58,72,91],65))



def solution(L,x):

    final_index = []

    for i in range(len(L)):

        if L[i:][0] == x:

            final_index.append(i)

        else:

            continue

    if len(final_index) == 0:

        final_index.append(-1)

    return final_index


print(solution([64,72,83,72,54],72))

## 핵심은 슬라이싱을 변화하면서 할 수 있는 개념