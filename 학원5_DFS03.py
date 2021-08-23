visited = [False]*9

adjacency_list = [[],
                  [2,3,8],
                  [1,7],
                  [1,4,5],
                  [3,5],
                  [3,4],
                  [7],
                  [2,6,8],
                  [1,7]]

def dfs(adjacency_list,visited,v):

    print(v, end=' ')

    visited[v] = True

    for i in adjacency_list[v]:

        if not visited[i]:

           dfs(adjacency_list,visited,i)


dfs(adjacency_list,visited,1)







