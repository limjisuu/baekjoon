import sys
computer_num = int(sys.stdin.readline())
connected_num = int(sys.stdin.readline())
pairs = [list(map(int, sys.stdin.readline().split())) for _ in range(connected_num)]
matrix = [[0 for _ in range(computer_num + 1)] for _ in range(computer_num + 1)]
visited = [0 for _ in range(computer_num + 1)]


def dfs(vertex):
    visited[vertex] = 1
    for num in range(1, computer_num + 1):
        if matrix[num][vertex] == 1 and visited[num] == 0:
            dfs(num)


for pair in pairs:
    matrix[pair[0]][pair[1]] = 1
    matrix[pair[1]][pair[0]] = 1

dfs(1)
print(visited.count(1) - 1)
