###.1 깊이 우선 탐색(DFS; Depth-First Search)

# 한 정점에서 인접한 모든(아직 방문하지 않은) 정점을 방문하되, 각 인접 정점을 기준으로 깊이 우선 탐색을 끝낸 후 다음 정점으로 진행하는 방식을 깊이 우선 탐색(DFS)방식 이라고 한다.

# 이러한 DFS 방식을 구현하기 위해서는 어느 정점에서 DFS를 진행하고 있는지를 기억해야 하므로 스택을 이용하는 것이 필요하다.

###.2 너비 우선 탐색(BFS; Breadth-First search)

# 한 정점에서 인접한 모든(아직 방문하지 않은) 정점을 방문하고, 방문한 각 인접 정점을 기준으로(방문한 순서에 따라) 또 다시 너비 우선 탐색을 행한다.

# 이러한 BFS 방식을 구현하기 위해서는 어느 정점에서 BFS를 해야하는 지를 기록하고 진행해야 하기 때문에 큐를 이용하는 것이 필요하다.

def solution(tickets):

    routes = {}

    for t in tickets:

        routes[t[0]] = routes.get(t[0],[]) + [t[1]]

# routes 라는 딕셔너리에 key 값이 출발하는 공항이 할당되고, value 값에는 도착하는 공항이 리스트의 형태로 할당되어있는 딕셔너리가 생성된다.

    for r in routes:

        routes[r].sort(reverse=True)

# r변수에는 딕셔너리인 routes의 key가 할당된다. 즉, routes[r]은 키 r에 대한 value를 표현하고 그 value를 알파벳 순서의 반대방향으로 정렬하는 것이다. 이때 sort 메소드를 사용하는 이유는 value는 이경우 리스트형태이기 때문이다.

    stack = ["ICN"]

    path = []

    while len(stack) >0:

        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:

# top가 표현하는 공항이 딕셔너리인 routes에 속하지 않는다는 것은 routes 딕셔너리의 키에 top 공항이 표현하는 것과 같은 key가 존재하지 않는다는 것이다. 그리고 만약 top가 표현하는 공항이 routes 딕셔너리의 키에 포함되어 routes[top] 동작이 가능할 경우 위와 같이 표현할 수 있는 위의 경우는 출발공항을 표현하는 top 공항에 대하여 도착하는 공항이 존재하지 않음을 표현하는 경우이다.

            path.append(stack.pop())

        else:

            stack.append(routes[top][-1])

            routes[top] = routes[top][:-1]

    return path[::-1]






