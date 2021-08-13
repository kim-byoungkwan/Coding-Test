###.1

def solution(arr):

    dict = {}

    for i in range(len(arr)):

        dict[arr[i]] = dict.get(arr[i],0) + 1

    value_box = dict.values()

    max1 = max(value_box)

    min1 = min(value_box)

    result = max1//min1

    return result


arr = [1,2,3,3,1,3,3,2,3,2]

print(solution(arr))

