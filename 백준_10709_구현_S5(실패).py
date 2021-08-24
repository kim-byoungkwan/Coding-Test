N,M = map(int,input().split())

matrix = [list(map(str,input())) for i in range(N)]



for i in range(N):

    for j in range(M):

        if matrix[i][j] == "C":

            matrix[i][j] = 0

        else:

            matrix[i][j] = -1


for m in range(N):

    for n in range(M):

        while True:

            if matrix[m][n] == 0:

                continue




