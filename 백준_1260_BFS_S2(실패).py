# ###.1
#
# from collections import deque
#
#
# N,M,V = map(int,input().split())
#
# dict = {}
#
# box = []
#
# for i in range(M):
#
#     a,b = map(int,input().split())
#
#     dict[a] = dict.get(a,[]) + [b]
#
#     dict[b] = dict.get(b,[]) + [a]
#
#     dict[a].sort()
#
#     dict[b].sort()
#
#
# dict = sorted(dict.items(),key= lambda item: item[0])
#
# print(dict)
#
#
# for i in dict:
#
#     box.append(i[1])
#
#
# graph = deque(box)
#
# graph.appendleft([])
#
# graph = list(graph)
#
# visited = [False]*(N+1)
#
#
# def dfs(graph,start,visited):
#
#     visited[start] = True
#
#     print(start, end=' ')
#
#     for i in graph[start]:
#
#         if not visited[i]:
#
#             dfs(graph,i,visited)
#
#
# dfs(graph,V,visited)
#
# print()
#
# visited = [False]*(N+1)
#
#
# def bfs(graph,start,visited):
#
#     queue = deque([start])
#
#     visited[start] = True
#
#     while queue:
#
#         v = queue.popleft()
#
#         print(v, end=' ')
#
#         for i in graph[v]:
#
#             if not visited[i]:
#
#                 queue.append(i)
#
#                 visited[i] = True
#
# bfs(graph,V,visited)
#

###.2

# from collections import deque
#
# N,M,V = map(int,input().split())
#
# edgeList = []
#
# for i in range(M):
#
#     a,b = map(int,input().split())
#
#     edgeList.append((a,b))
#
#     edgeList.append((b,a))
#
#
# def dfs(edgeList,V,N):
#
#     visited = []
#
#     stack = [V]
#
#     adjacencyList = [[] for i in range(N + 1)]
#
#     for edge in edgeList:
#
#         adjacencyList[edge[0]].append(edge[1])
#
#
#     while stack:
#
#         current = stack.pop()
#
#         for i in sorted(adjacencyList[current],reverse=True):
#
#            if not i in visited:
#
#                stack.append(i)
#
#         if not current in visited:
#
#             visited.append(current)
#
#     return visited
#
#
# def bfs(edgeList,V,N):
#
#     visited = []
#
#     queue = deque([V])
#
#     adjacencyList = [[] for i in range(N + 1)]
#
#     for edge in edgeList:
#
#         adjacencyList[edge[0]].append(edge[1])
#
#         adjacencyList[edge[0]].sort()
#
#     while queue:
#
#         current = queue.popleft()
#
#         for i in adjacencyList[current]:
#
#             if not i in visited:
#
#                 queue.append(i)
#
#         if not current in visited:
#
#             visited.append(current)
#
#     return visited
#
# for i in dfs(edgeList,V,N):
#
#     print(i,end=' ')
#
# print()
#
# for i in bfs(edgeList,V,N):
#
#     print(i,end=' ')


###.3

N,M,V = map(int,input().split())

matrix = [[0]*(N+1) for i in range(N+1)]

# 행의 개수가 N+1, 열의 개수가 N+1 인 초깃값 0을 갖는 행렬을 생성한다. 이 문제에서는 0번째 노드가 존재하지 않고, 1번째 노드부터 시작하므로, 인덱스 0을 표현하는 공간을 행렬에 표현하여, 노드의 번호와 인덱스의 번호를 일치시켜 행렬을 통한 노드접근을 더 직관적이게 하기 위해 위와 같은 행렬로 초기화한 것이다.

for i in range(M):

    a,b = map(int,input().split())

    matrix[a][b] = matrix[b][a] = 1

# 간선의 개수가 M개 이고, 이 경우 필요한 최소 간선 수만 나타낸 경우이므로, 정확히 대칭관계에 있는 노드의 간선상태까지 표현하기 위해선 위와 같은 행렬의 형태로 노드 연결관계를 표현할 수 있다.

# matrix[a][b] 의 값이 1로 존재한다는 것은 노드 a와 노드 b가 연결관계에 있다는 것이고 그것은 곧, 노드 b와 노드 a가 연결관계에 있다는 것이므로 matrix[b][a]의 값도 1로 존재하게 된다.

# 따라서, 위의 코드에 의해 존재하는 모든 노드의 간선 상태가 행렬로 표현되게 되고, 이와 같은행렬을 인접행렬이라고 한다.

visit_list = [0]*(N+1)

# 마찬가지로 방문한 노드를 표시해주기 위해 visit_list를 생성할 때, 노드의 번호와 리스트의 인덱스가 일치하여 직관성을 높이기 위해 방문 리스트의 요소값을 N+1 개로 설정해준다.


def dfs(V):

    visit_list[V] = 1

# V 번째 노드부터 시작하므로, 방문 노드를 기록하는 리스트 visit_list의 V번째 요소 값을 1로 치환한다.

    print(V, end=' ')

# 방문한 노드를 V로 출력하여 표현한다.

    for i in range(1,N+1):

# 노드가 1번째 노드부터 N번째 노드까지 존재하므로 range를 1부터 N+1까지 설정하여 i가 1부터 N까지 표현될 수 있게 해서 존재하는 모든 노드를 순환할 수 있게 해준다.

        if (visit_list[i] == 0 and matrix[V][i]==1):

            dfs(i)

# 어떠한 i번째 노드를 방문하지 않은 상태이면서 첫번째 시작 노드 V 번째 노드와의 연결관계가 존재하는 상태라면, i를 방문해야한다.(이때 i는 1부터 시작하는 값이므로, 가장 작은 번호의 노드부터 방문할 수 있게 된다.)

# dfs(i)에 의해 시작 노드가 V 번째 노드인 상태에서 V 번째 노드와 연결된 i번째 노드를 방문하게 되는데, 이는 visit_list[i] = 1 로 표현되고, print(i, end=' ')로 표현된다.

# 이때 또 다시 if 문을 만나서, 이번엔 i가 V로 표현되게 되면서 i가 시작노드인 상태가 된다. 그런데 이번엔 i는 visit_list[i] 리스트에서 1 의 값으로 표현되므로, if 문은 시작되지 않는다.
# 그러나 i가 4일때 visit_list[4] == 0 이고 matrix[3][4] == 1 이므로, dfs(4)가 실행되게되고, 4번째 노드가 방문되게 된다.

from collections import deque


visit_list_2 = [0]*(N+1)


def bfs(V):

    queue = deque([V])

    visit_list_2[V] = 1

    while queue:

        V=queue.popleft()

        print(V, end=' ')

        for i in range(1,N+1):

            if(visit_list_2[i] == 0 and matrix[V][i] == 1):

# 시작 노드 V 와 연결관계를 갖지만 아직 방문하지 않은 모든 노드를 위의 if문에서 i가 표현한다.
# 즉 방문해야할 모든 i 노드는 아래의 append 동작에 의해 queue에 저장된다.
# 이때 다음 while 동작에서 출력되면서 방문하게 될 i는 시작 노드 V와 동일한 거리로 인접한 모든 노드를 표현하므로, 이러한 i노드를 queue에 저장하여 저장된 순서대로 출력하게 되면 V노드와 동일한 거리로 인접한 노드가 출력되게되고, 그 출력된 노드들은 i와 같은 거리로 인접한 노드들을 표현하게된다.

                queue.append(i)

# i 노드를 방문할 예정인 모든 노드를 저장해두는 역할을 하는 queue에 넣어준다.

                visit_list_2[i] = 1

# queue에 저장된 i 노드는 저장되자마자 방문처리를 위와 같이 해주는데, 아직 방문하여 출력되지 않았음에도, 이 바로 다음 동작에서 queue.pop(0)에 의해 출력되므로 미리 방문처리를 해주는 것이다.


dfs(V)

print()

bfs(V)


























































