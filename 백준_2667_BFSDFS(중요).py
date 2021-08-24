###.1

N = int(input())

adjacency_matrix = [list(map(int,input())) for i in range(N)]

def dfs(x,y):

    global count

    if x < 0 or x > N-1 or y < 0 or y > N-1:

        return False

    if adjacency_matrix[x][y] == 1:

        adjacency_matrix[x][y] = 0

        count = count + 1

        dfs(x+1,y)

        dfs(x-1,y)

        dfs(x,y+1)

        dfs(x,y-1)

        return True

    return False

count = 0

result = 0

box = []

for i in range(N):

    for j in range(N):

        if dfs(i,j) == True:

            result = result + 1

            box.append(count)

            count = 0

print(result)

box.sort()

for i in box:

    print(i)

# return이 발생하는 순간 전역변수에 저장된 값은 초기화 시키지 않는 이상 그대로 유지된다.



