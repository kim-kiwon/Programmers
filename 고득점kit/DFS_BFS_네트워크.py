'''
컴퓨터 수 n.
comupters 연결 관련 2차배열
네트워크 개수 return.
-> dfs로 개수세자.
'''


def dfs(n, computers, a, visited):
    if visited[a] == 1:
        return False
    visited[a] = 1
    for i in range(n):
        now = computers[a][i]
        if now == 1 and visited[i] == 0:
            dfs(n, computers, i, visited)
    return True

def solution(n, computers):
    visited = [0] * (n)
    answer = 0
    for i in range(n):
        if dfs(n, computers, i, visited) == True:
            answer += 1
    return answer