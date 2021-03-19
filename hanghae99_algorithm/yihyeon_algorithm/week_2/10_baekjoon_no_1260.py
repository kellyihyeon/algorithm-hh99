# 백준 1260번 (DFS와 BFS)

n, m, start_node = map(int, input().split())
# 연결 여부를 체크해 놓을 리스트 준비(0부터 넣어서 좌표처럼 활용)
tool = [[0 for _ in range(n+1)] for _ in range(n+1)]
# visited_node = list()

# 왜 m을 써야 하는지?
# 번호를 받고, 딕셔너리로 만든 후 -> 연결된 번호들을 좌표로 넣어서 1로 체크 해놓자.
for _ in range(m):
    x, y = map(int, input().split())
    tool[x][y] = tool[y][x] = 1

# requirement: stack=[], visited_node=[]
def dfs(s_node, visited_node):
    # visited_node = []       # visited_node = [3,1,2,5,4 ]
    stack = [s_node]          # stack = []

    while stack:
        target_node = stack.pop()
        visited_node.append(target_node)
        for i in range(n+1):    # i = 0 1 2 3 4 5
            if tool[target_node][i] == 1 and i not in visited_node:
                dfs(i, visited_node)

    return visited_node


# bfs 구현
def bfs(s_node, visited_node):
    # temp = [], visited_node = []
    temp = [s_node]                            # temp = [, , , , ,'5']

    while temp:
        target_node = temp.pop(0)
        visited_node.append(target_node)       # visited_node = [3,1,4,2,5,5]
        for i in range(n+1):
            if tool[target_node][i] == 1 and i not in visited_node and i not in temp:
                # temp.append(tool[target_node])
                temp.append(i)

    return visited_node


print(" ".join(map(str, dfs(start_node, list()))))
print(" ".join(map(str, bfs(start_node, list()))))


# print(dfs(start_node, list()))
# print(bfs(start_node, list()))
# print("fin")


# mistake 1: visited_node 전역변수?
# 리스트에서 대괄호 빼고 출력?