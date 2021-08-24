###.1

def solution(arr):

    count = 0

    for i in range(len(arr)):

        portion = arr[i] / 2

        if portion in arr:

            count = count + 1

    return count

arr = [4,8,3,6,7]

print(solution(arr))

