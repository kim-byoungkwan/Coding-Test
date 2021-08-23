from collections import deque

N = int(input())

M = int(input())


matrix = [[0]*(N+1) for i in range(N+1)]

for i in range(M):

    a,b = map(int,input().split())

    matrix[a][b] = matrix[b][a] = 1


queue = deque([1])

visited_list = [0]*(N+1)

visited_list[1] = 1


while queue:

    current = queue.popleft()

    for i in range(1,N+1):

        if visited_list[i] == 0 and matrix[current][i] == 1:

            queue.append(i)

            visited_list[i] = 1


print(sum(visited_list)-1)


