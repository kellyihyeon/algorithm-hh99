# 백준 15649번 (N과 M 1)

n, m = map(int, input().split())
visited = [False] * n
result = list()

def sequence(depth, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            result.append(i + 1)
            sequence(depth+1, n, m)      # 재귀 때문에 막힌다.
            visited[i] = False
            result.pop()

sequence(0, n, m)

