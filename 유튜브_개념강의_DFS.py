vertexList = ['0','1','2','3','4','5','6']

# 그래프에 존재하는 모든 노드들을 표현하는 리스트이다.

edgeList = [(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(4,6),(5,2),(6,4)]

# 존재하는 모든 노드의 간선을 통한 연결상태를 표현하는 리스트이다.

adjacencyList = [[] for vertex in vertexList]

# 존재하는 모든 노드의 개수 만큼 [] 리스트를 생성해준다.(인접행렬에서의 노드수가 행의 수로 표현되는 것과 동일하다)
# 이와 같은 형태가 인접리스트와 인접행렬의 형태이다.

for edge in edgeList:

    adjacencyList[edge[0]].append(edge[1])

# adjacencyList에는 현재 7개의 노드를 표현하는 7개의 [] 가 존재하는데, 이때 edge[0] = 0 이므로, adjacencyList의 0번째 인덱스가 표현하는 [] 리스트를 adjacencyList[edge[0]] = [] 이와 같이 표현한다.
# 즉, 0번째 []에 edge[1] = 1 이므로, 1이 할당되어 첫번째 for문의 결과
# [ [1],[],[],[],[],[],[] ] 이와 같은 형태의 리스트가 된다. 즉, 0번째 노드와 연결된 1번째 노드의 상태를 이와 같은 리스트로 표현하는 것이다.
# 이렇게 리스트 안에 리스트를 원소로 하고 그 리스트가 표현하는 인덱스를 출발노드로 규정한 리스트를 인접리스트 라고한다.
# 최종적으로 인접리스트의 형태는
# [ [1,2],[0,3],[0,4,5],[1],[2,6],[2],[4] ] 이와 같이 결정된다.


def dfs(vertexList,edgeList,start):

    visitedVertex = []

    stack = [start]

# 이경우 0번째 노드가 존재하고, 0번째 노드부터 DFS를 시작하기 위해서 스택에 초기값 0을 할당한 것이다. 즉, 최초로 0번째 노드부터 방문하여 dfs를 시작하기 위해 앞으로 방문할 노드를 표현하는 stack에 0 노드를 할당하는 것이다.

    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:

        adjacencyList[edge[0]].append(edge[1])

    while stack:

# 스택에 현재 0의 값이 존재하므로 while 조건문이 실행된다.

        current = stack.pop()

# 현재 탐색한 노드 0을 스택에서 출력하여 current 변수에 할당한다.

        for neighbor in adjacencyList[current]:

# 인접리스트 adjacencyList에는 모든 인덱스가 표현하는 노드에 대해서 연결된 인접노드가 원소로 할당되어 있는데 현재 방문한 current 노드와 인접한 모든 노드가 neighbor에 할당되게 된다.

            if not neighbor in visitedVertex:

                stack.append(neighbor)

# current 노드와 인접한 노드가 현재 방문하지 않은 상태라면, dfs에서는 인접한 노드를 방문하는 것이 가장 우선순위가 높으므로, neighbor 노드를 곧 방문할 것이라는 의미로 stack에 할당한다.
# 즉, 위의 코드를 통해서 current와 인접한 노드중에 아직 방문하지 않아서 앞으로 방문해야하는 neighbor 노드를 stack에 모두 할당한다. 따라서, 이 결과 stack에는 항상 current 노드와 인접하지만 아직 방문하지 않아서 앞으로 방문해야하는 모든 노드들이 존재하게 된다.

        visitedVertex.append(current)

# 내가 최종적으로 출력해야할 것은 dfs원칙에 따라 방문한 노드를 순서대로 출력하는 것이므로, 현재 방문한 current 노드를 방문한 노드를 순서대로 저장하는 visitedVertex 리스트에 저장한다.

    return visitedVertex


print(dfs(vertexList,edgeList,0))