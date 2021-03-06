# def는 깊이우선탐색이다. 스택과 재귀함수를 사용한다. 
# 깊은 부분을 우선적으로 탐색해야한다. dfs는 노드와 간선으로 이루어져있다. (노드 = 정점)
# dfs는 인접행렬과 인접리스트로 나타낼 수 있는데
# 인접행렬은 2차원이고 인접리스트는 1차원이다. 

#dfs의 예제를 예를 들어보겠다.
def dfs(grahp, v, visited):
    # 현재 노드를 방문 처리 
    visited[v] = True
    # v는 노드다.
    print(v,end="")
    # 방문한 노드를 입력하려고 이렇게 써놓은듯 ?
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문해야한다.
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    
graph = [
    [],
    [2,3,8],    # 그래프의 노드와 연결된 것을 표시하는듯?
    [1,7],
    [1,4,5],
    [3,4],
    [3,5],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] *9 
# 일부러 하나 더 크게 했다는데 
dfs(graph,1,visited)