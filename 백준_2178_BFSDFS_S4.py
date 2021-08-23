from collections import deque

N,M = map(int,input().split())

matrix = [list(map(int,input())) for i in range(N)]

dx = [1,-1,0,0]

# dx는 실제 matrix[dx][dy] 에서 matrix[1][dy]를 실행했을 때, 이전의 위치보다 아래방향으로 1만큼 이동시키므로, dx로 표기 되었지만, x축 방향으로의 이동이라고 생각하면 안되고, 좌표평면상의 y축 방향으로의 이동을 나타낸다는 것을 알아야 한다.

a,b = 0,0

dy = [0,0,-1,1]

# 마찬가지로 dy로 표현했지만, 좌표평면상에서 x축 방향으로의 이동을 표현한다.

queue = deque()

queue.append((a,b))

matrix[a][b] = 1

while queue:

    x,y = queue.popleft()

    if x == N-1 and y == M-1:

        break

    for i in range(4):

        new_x = x + dx[i]

        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < M:

            if matrix[new_x][new_y] == 1:

                queue.append((new_x,new_y))

                matrix[new_x][new_y] = matrix[x][y] + 1

print(matrix)


