def solution(arr):

    arr_reverse = []

    for i in range(len(arr)):

        arr_reverse.append(arr.pop())

    return arr_reverse


list = [1,4,2,3]

print(solution(list))