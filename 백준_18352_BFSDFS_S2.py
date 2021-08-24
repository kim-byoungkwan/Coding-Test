N,M,K,X = map(int,input().split())

matrix = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):

    x,y = map(int,input().split())

    matrix[x][y] = 1

visited = [0]*(N+1)

def dfs(X):

    visited[X] = 1

    print(X,end=' ')

    for i in range(1,N+1):

        if (visited[i] == 0 and matrix[X][i] == 1):

            dfs(i)

dfs(X)