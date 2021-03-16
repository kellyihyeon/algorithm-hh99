# BFS와 DFS의 개념을 확실히 모르고 있어서 정리해보는 코드

# 트리 모양
#                A
#                B
#           C        H
#         D       I  J  M
#         E  G       K
#         F          L

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def bfs(graph, start_node):
    visited = []
    waiting_list = []

    waiting_list.append(start_node)

    while waiting_list:
        node = waiting_list.pop(0)

        if node not in visited:
            visited.append(node)
            waiting_list.extend(graph[node])

    return visited




# queue를 import한 코드
# from queue import Queue
#
# def bfs(graph, start_node):
#     visit = set() # 아래 댓글에서도 지적했듯이 dictionary나 set으로 구현하는 것이 더 효율적입니다.
#     q = Queue()
#
#     q.put(start_node)
#
#     while q.qsize() > 0:
#         node = q.get()
#         if node not in visit:
#             visit.add(node)
#         for nextNode in graph[node]:
#             q.put(nextNode)
#
#     return visit

