###.1

from collections import deque


N,M,V = map(int,input().split())

dict = {}

box = []

for i in range(M):

    a,b = map(int,input().split())

    dict[a] = dict.get(a,[]) + [b]

    dict[b] = dict.get(b,[]) + [a]

    dict[a].sort()

    dict[b].sort()


dict = sorted(dict.items(),key= lambda item: item[0])

print(dict)


for i in dict:

    box.append(i[1])


graph = deque(box)

graph.appendleft([])

graph = list(graph)

visited = [False]*(N+1)


def dfs(graph,start,visited):

    visited[start] = True

    print(start, end=' ')

    for i in graph[start]:

        if not visited[i]:

            dfs(graph,i,visited)


dfs(graph,V,visited)

print()

visited = [False]*(N+1)


def bfs(graph,start,visited):

    queue = deque([start])

    visited[start] = True

    while queue:

        v = queue.popleft()

        print(v, end=' ')

        for i in graph[v]:

            if not visited[i]:

                queue.append(i)

                visited[i] = True

bfs(graph,V,visited)

