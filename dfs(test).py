n,m = map(int,input().split()) # n,m 크기의 얼음판을 만든다.

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x>= n or y <= -1 or y >= m:
        return False
        # 주어진 범위를 넘어가면 종료한다.

    if graph[x][y] == 0 :
        # 해당 노드 방문 처리 
        graph[x][y] = 1

        dfs(x - 1 , y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

    result = 0 
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1

    print(result)