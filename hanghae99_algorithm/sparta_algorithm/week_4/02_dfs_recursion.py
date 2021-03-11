# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!

# 딕셔너리 자료형의 키와 값의 쌍 반복- 개념 몰라서 공부.
# https://datascienceschool.net/01%20python/02.11%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%20%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%20%EC%9E%90%EB%A3%8C%ED%98%95%20%EB%8B%A4%EB%A3%A8%EA%B8%B0.html

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

# 1. 시작 노드(루트 노드)인 1부터 탐색합니다.
# 2. 현재 방문한 노드를 visited_array에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드에 방문합니다.
# visited_array = [1,2,3...10]

# cur_node = 시작하는 노드
def dfs_recursion(adjacent_graph, cur_node, visited_array): # 시작노드로 출발해서 노드들을 방문하는 함수
    visited_array.append(cur_node)
    for adjacent_node in adjacent_graph:        # 1,2,3
        if adjacent_node not in visited_array:  # 방문객 명단에 노드가 없으니까 다시 방문하는 노드 함수를 써야해.
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)

    return


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!