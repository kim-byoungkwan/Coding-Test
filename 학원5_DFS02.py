adjacency_list = [[] for i in range(3)]


adjacency_list[0].append((1,7))

adjacency_list[0].append((2,5))

# 0번 노드임을 0번이라는 인덱스가 표현하고, 0번 인덱스의 원소값인 (1,7)는 0번 노드와 1번 노드의 거리가 7임을 의미하고, (2,5)는 0번 노드와 2번 노드의 거리가 5임을 의미한다.


adjacency_list[1].append((0,7))

# 1번 노드와 0번 노드의 거리가 7임을 의미한다.


adjacency_list[2].append((0,5))

# 2번 노드와 0번 노드의 거리가 5임을 의미한다.


print(adjacency_list)